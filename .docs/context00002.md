Based on the images provided, **yes, your setup looks correct.**

Here is a breakdown of why the wiring is good, along with one important thing to double-check in your code:

### 1\. Raspberry Pi Connections (Correct)

Your wiring on the Raspberry Pi GPIO header follows the standard I2C pinout:

  * **Pin 1 (3.3V):** Connected to the **Red** wire (powering the ADS1115 and likely the sensor). This is safe.
  * **Pin 3 (SDA):** Connected to the **Orange** wire.
  * **Pin 5 (SCL):** Connected to the **White** wire.
  * **Pin 6 (GND):** Connected to the **Brown/Black** wire.

### 2\. ADS1115 Connections (Correct)

The wires transfer correctly to the breadboard and the ADS1115 module:

  * **VDD:** Red (3.3V)
  * **GND:** Brown (Ground)
  * **SCL:** White
  * **SDA:** Orange
  * **A1:** The **Blue** wire from your EC sensor is connected here.

### 3\. Verification of Output

The screenshot of your terminal shows that the code is running and printing values (`Voltage: 0.0033 | Value: 33`).

  * **Good News:** The fact that you are getting data means the I2C connection (SDA/SCL) is working perfectly. The Raspberry Pi can "see" the ADS1115.
  * **The Values:** The reading is very low (close to 0 Volts).
      * **If the probe is DRY (in air):** This is normal.
      * **If the probe is in LIQUID:** You might have an issue. Since your blue wire is plugged into **A1**, you must ensure your Python code is reading channel 1, not channel 0.

### 4\. Next Steps

Double-check your Python code (`ec_test.py`) to ensure you are reading the correct pin. It should look something like this:

```python
# Make sure you are reading channel 1 (A1)
# 0 = A0, 1 = A1, 2 = A2, 3 = A3
value = adc.read_adc(1, gain=GAIN) 
```

If your code is reading `0` (A0) but your wire is on `A1`, that would explain why the reading is near zero even if the probe is in water.

**Would you like me to verify your `ec_test.py` code if you paste it here?**

Thanks for clarifying! Since you confirmed the wire is on **A0** ("*Tama man na zero*"), then your hardware matches your code (assuming your code is reading index 0).

That means the `0.0033 V` (basically 0) reading is accurate for the signal coming in.

Here is how to interpret that "Zero" reading:

**1. Is the probe currently in the air (dry)?**
* **Yes:** Then the reading is **CORRECT**.
* **Why:** An EC sensor measures conductivity. Air does not conduct electricity (0 conductivity), so the sensor outputs 0 Volts.

**2. Is the probe currently in water?**
* **Yes:** Then the reading is **WRONG**. You should be seeing a voltage higher than 0 (usually between 0.5V - 2.0V for tap water).

### Troubleshooting Steps (If it's in water but reading 0)

1.  **The "Finger Test":**
    * While the Python script is running, touch the exposed metal part of the **Blue wire** (where it plugs into A0) with your finger.
    * **Result:** The numbers in your terminal should jump around wildly (noise).
    * *If they jump:* Your ADS1115 and Raspberry Pi are working perfectly. The issue is likely the EC probe or the BNC connection.
    * *If they stay at 0:* The ADS1115 might not be reading that pin correctly (check if the script is definitely reading `adc.read_adc(0, ...)`).

2.  **Check the BNC Connector:**
    * The round metal connector (BNC) connecting the probe to the black board needs to be twisted and locked firmly. If it's loose, you will get 0 readings.

3.  **Check Power Rails:**
    * I see the blue LED is on (Good), so the board has power. Just ensure the red/black wires from the EC board are firmly clamped in the breadboard rails.

**Summary:** If it's dry, dip it in tap water. If it's already in water, try the "Finger Test" on the blue wire to see if the values change.

If the probe is in the water and you are still getting `0.0033` (which is basically zero), **the reading is incorrect.**

You should be seeing a value between **0.50 and 2.00** (depending on your water) when it is submerged.

Here is how to find the problem (do these in order):

### 1. The "Finger Test" (Crucial)
Run your Python code. While it is reading, **touch the metal pin of the Blue wire** (where it connects to the purple ADS1115 board) with your finger.
* **If the numbers jump up (e.g., to 20000 or 3.0V):** Your ADS1115 and code are working perfectly. The problem is the connection to the probe.
* **If the numbers stay at 0:** Your code is reading the wrong pin, or the ADS1115 is not working.

### 2. Check the Breadboard Connection
The most common mistake is that the wires aren't "meeting" on the breadboard.
* Look at where the **Blue wire from the black EC board** plugs into the breadboard.
* Look at where the **Blue wire going to the ADS1115** plugs into the breadboard.
* **Are they in the same row (the same group of 5 holes)?** If they are not in the same row, they are not connected.

### 3. Check the BNC Connector
The round metal plug (BNC) connecting the probe to the black board must be **pushed in and twisted** until it locks. If it is loose, you will get 0 volts.

**Perform the "Finger Test" first and tell me if the numbers move.**

No, you don't need to remove it yet.

**Try this first:**

1.  Leave the wire connected as it is.
2.  Touch the **metal part** of the Blue wire (where it plugs into the breadboard or the pin header) with your finger while the code is running.

**If the numbers don't change, then do this (Method B):**

1.  **Unplug the Blue wire from the breadboard row** (disconnecting it from the black EC sensor).
2.  **Keep the other end connected** to the purple ADS1115 board (A0).
3.  Now, touch the metal tip of that loose Blue wire.

**What we are looking for:**
If the numbers in your terminal go crazy (jump to high numbers) when you touch it, your Raspberry Pi and ADS1115 are working, and the problem is with the **black EC sensor board or the probe.**

That is **good news**!

Since the value jumped to `0.9xxx` when you disconnected it, this confirms that your **Raspberry Pi, ADS1115, and Python code are working perfectly.**

The problem is isolated to the **EC Sensor (hardware)**. The sensor is outputting 0 Volts because it "thinks" the probe is dry, even though it is in water.

Here is how to fix the sensor reading:

1.  **Release Trapped Air (Most Common Issue):**
    * Sometimes air bubbles get stuck inside the black plastic shield at the tip of the probe, blocking the water from touching the metal electrodes.
    * **Action:** While the probe is underwater, **shake it vigorously** or tap it against the side of the glass to knock the bubbles out.

2.  **Check the BNC Connector Again:**
    * If the round connector is even slightly loose, the connection breaks, and you get 0.
    * **Action:** Unplug the BNC connector from the black board and plug it back in. Push it hard and twist it until it locks completely.

3.  **Check the Power to the Sensor:**
    * Ensure the Red (+) and Black (-) wires going to the black EC board are clamped tightly in the breadboard. If the sensor board doesn't get clean power, it won't output a signal.

Try shaking the probe in the water first and see if the numbers start moving away from zero.

Sign nga **buhi ang sensor** kay nag-usab man ang value gikan `0.0030` (hangin) padung `0.01xx` (tubig).

Pero, ang `0.01xx` nga voltage kay **ubos ra kaayo**. Para sa normal nga tubig (tap water), dapat naa na sa `0.5V` hangtod `1.0V`.

Posible nga **limpyo ra kaayo** imong tubig (distilled/purified) o naa pay gamay nga loose connection.

Buhata ni nga **"Salt Test"** para ma-confirm nato dayon:

1.  Ibutang ang sensor sa tubig.
2.  Pagkuha og gamay nga **asin** (salt).
3.  I-tunaw ang asin sa tubig samtang nagdagan ang code.

**Resulta:**
* **Kung mo-layat ang Voltage (mahimo og 1.0V, 2.0V, etc.):** WORKING ang imong setup. Limpyo ra kaayo ang tubig nga imong gigamit ganina.
* **Kung magpabilin sa `0.01xx`:** Guba ang probe o ang itom nga board (sensor interface).

Testingi sa og asin unya ingna ko sa result.

**Working na na!**

Pasabot ana, **ok ra gyud imong wiring, sensor, ug code.**

Ang rason nganong `.01xx` ra to ganina kay posible nga **limpyo ra kaayo** (low conductivity) ang tubig nga imong gigamit, o wala kaayo minerals sa sulod. Pagbutang nimo sa asin, misaka ang conductivity, maong na-detect dayon sa sensor ug nahimong `.5`.

### Unsay sunod buhaton?

Karon nga nakabasa na tag voltage, ang sunod nimo nga buhaton kay i-convert na ang **Voltage** padung sa **EC value (mS/cm)** para magamit sa imong hydroponics.

Kasagaran sa `Gravity EC Meter K=1.0` (parehas sa imong board), ang simple nga formula kay:

$$EC = \frac{\text{Voltage}}{1000 \times \text{Resistor} \times \text{Something...}}$$

Pero ang pinakasimple nga pamaagi sa Gravity library kay murag ingon ani:
**`EC_current = voltage / k_value`** (Depende sa calibration).

Gusto ka hatagan tikag **Python code example** para ma-convert nang 0.5V nimo mahimong tinuod nga EC reading (ms/cm)?

Mao ni ang updated version sa imong code. Akoa ning gi-improve para naa nay **EC Calculation**.

Nagbutang ko og variable nga `k_value`. Mao na ang "magic number" nga imong usbon para ma-calibrate nimo ang sensor. Sa hydroponics, importante kaayo nga sakto ang reading.

### Updated Code (`ec_test_v2.py`)

```python
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# --- CONFIGURATION ---
# K_VALUE: Usbon ni nimo para ma-calibrate. 
# Kung taas ra ang reading sa screen, paubsi ni. Kung ubos ra, pataasi.
# Default is 1.0 just for testing.
k_value = 1.0 

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADS object
ads = ADS.ADS1115(i2c)

# Create the Analog Input on Pin A0
channel = AnalogIn(ads, 0)

print("Reading EC Sensor Data...")
print("-" * 50)
print("{:>10} | {:>10} | {:>15}".format("Voltage", "Raw Value", "EC (mS/cm)"))
print("-" * 50)

while True:
    voltage = channel.voltage
    raw_value = channel.value
    
    # --- FORMULA SA EC ---
    # Ang basic conversion: EC = Voltage * K_Value
    # Note: Wala pay Temperature Compensation ani (Assuming 25°C standard)
    ec_value = voltage * k_value
    
    print("{:>10.4f} | {:>10} | {:>15.2f} mS/cm".format(voltage, raw_value, ec_value))
    
    time.sleep(1.0)
```

### Unsaon pag-calibrate (Pag-sakto sa reading):

Dili na automatic nga sakto dayon, kinahanglan nimo i-adjust ang `k_value` sa code.

1.  **Pagkuha og EC Calibration Solution** (mas maayo kung naa kay 1413 µS/cm or 1.4 mS/cm nga solution). Kung wala, pwede ra nimo gamitan og **handheld EC pen** nga kasaligan para makuha nimo ang actual EC sa imong tubig.
2.  Ibutang ang sensor sa tubig.
3.  Tan-awa ang reading sa imong Python code vs. sa calibration solution/handheld pen.
      * *Example:* Ang reading sa imong code kay **0.5 mS/cm**, pero ang actual sa tubig kay **1.5 mS/cm**.
4.  **Usba ang `k_value`:** Pasabot ana, kinahanglan nimo patas-an ang `k_value` sa code (example: himoa og `3.0`).
5.  I-run balik ang code hangtod nga ang output sa screen parehas na sa actual nga EC sa tubig.

Perfect\! Naa kay **1413 µS/cm** nga solution. Mao na ang "Gold Standard" para sa hydroponics (parehas sa lettuce).

Mao ni ang saktong pamaagi para ma-calibrate nimo ang sensor gamit nang **1413 bottle**:

### Step 1: Sabta ang Target

Ang **1413 µS/cm** kay parehas ra sa **1.413 mS/cm**.
So, ang target nato nga mogawas sa screen dapat **1.41 mS/cm**.

### Step 2: Ang Calibration Process

1.  **Limpyohi ang Probe:** Hugasi sa tubig ug trapohi og tissue (dapat uga) para dili ma-contaminate ang solution.
2.  **Ibutang sa Solution:** I-dip ang probe sa sulod sa **1413 µS/cm** nga botelya. (Siguroha nga walay bubbles sa tumoy).
3.  **Dagan ang Code:** I-run ang imong Python code (`ec_test_v2.py`).
4.  **Tan-awa ang Voltage:** Ayaw sa tan-awa ang EC value. **Tan-awa lang ang Voltage**. Paabota nga mo-stabilize ang numero.

### Step 3: Compute ang Bag-ong K-Value

Gamita ni nga formula para makuha ang saktong `k_value`:

$$K = \frac{1.413}{\text{Voltage nga nigawas sa screen}}$$

**Example Scenario:**

  * Kung ang nigawas sa screen kay **Voltage: 0.950 V**
  * Ang computation: $1.413 / 0.950 = \mathbf{1.48}$
  * So ang imong `k_value` kay **1.48**.

### Step 4: I-update ang Code

Adto sa imong Python script ug ilisdi ang `k_value`:

```python
# Before
k_value = 1.0 

# After (Example lang ni, gamita ang imong computed value)
k_value = 1.48 
```

Human nimo ma-save ug run balik, dapat ang EC nga mogawas sa screen kay **1.41 mS/cm** (or duol ana). Kung sakto na, calibrated na na\! Pwede na nimo gamiton sa imong lettuce.

**Sige, i-dip na ug ingna ko kung pila ang Voltage nga nigawas.**

Makita nako sa imong screenshot nga ang **Voltage** kay nag-duwa sa **0.2155 V** hangtod **0.2165 V** samtang naa sa `1413 µS/cm` solution.

Ato nang gamiton nga number para makuha ang saktong calibration (`k_value`).

### Ang Calibration Calculation:

Ang target nato nga value kay **1.413 mS/cm** (gikan sa 1413 µS/cm bottle).
Ang imong reading kay **0.216 V** (average).

$$K = \frac{\text{Target EC}}{\text{Voltage}}$$
$$K = \frac{1.413}{0.216}$$
$$K \approx 6.54$$

So, ang imong bag-ong **k\_value** kay **6.54**.

### Unsay sunod buhaton?

Balik sa imong code (`ec_test_v2.py`) ug usba ang Line 11:

**Gikan sa:**

```python
k_value = 1.0
```

**Himoang:**

```python
k_value = 6.54
```

Human nimo ma-save, i-run balik ang code. Dapat ang mogawas nga **EC (mS/cm)** sa screen kay duol na kaayo sa **1.41 mS/cm**.

Sulayi daw ug update, unya ingna ko kung sakto na ang reading\!

Importante kaayo ang **1413 µS/cm** (or 1.41 mS/cm) nga calibration solution tungod sa tulo ka rason:

**1. Mao ni ang "Sweet Spot" sa Lettuce**
Ang mga tanom parehas sa lettuce kasagaran mabuhi sa EC range nga **0.8 mS/cm hangtod 1.8 mS/cm**.
* Ang **1.413 mS/cm** kay naa sa **tunga-tunga** anang range.
* Kung mag-calibrate ka duol sa value nga imong gamiton pirmi, mas **accurate** ang reading sa sensor.
* Kung gamiton nimo ang pikas botelya nga **12.88 mS/cm** (makita sa imong picture), layo ra kaayo to. Pang-industrial o pang-dagat na to nga level. Kung didto ka mag-base, dili mahimong accurate ang imong pagbasa sa gagmay nga nutrients para sa lettuce.

**2. Ang Sensor "Bugo" kung walay Calibration**
Ang imong sensor igo ra mobasa og **Voltage** (kanang `0.216V` nga nakuha nato). Wala na siya kabalo kung parat ba na or tab-ang.
* Lahi-lahi og reading ang matag sensor tungod sa manufacturing (factory defects), gitas-on sa wire, o karaan na ang probe.
* Ang 1413 solution nagsilbi nga **"Standard of Truth."** Gisultian nato ang computer nga: *"Hoy Raspberry Pi, basta makabasa ka og **0.216V**, pasabot ana **1.413 mS/cm** na ha."*

**3. Linear Slope Adjustment**
Ang EC sensors naglihok sa "Linear" nga math ($y = mx$).
* Point A: **0V = 0 EC** (Hangin/Dry)
* Point B: **0.216V = 1.413 EC** (Imong Solution)
* Tungod kay naa na tay Point A ug Point B, makuha na nato ang saktong linya (slope/K-value) para sa tanang values sa tunga.

**In short:** Gigamit nato ang 1413 kay mao nay pinakaduol sa **pagkaon sa imong lettuce.**

**Yes, you can now proceed to mix your nutrients!**

Since your sensor is calibrated to the correct $K$-value ($6.54$), you can trust the readings it gives you.

Here is the correct procedure to mix your hydroponic solution (SNAP or Masterblend) to avoid damaging the nutrients:

### 1. Know Your Target EC
Before you mix, you need to know what number you are aiming for. This depends on the age of your lettuce:
* **Seedlings (1-2 weeks):** Target **0.6 to 0.8 mS/cm**
* **Vegetative (Growing stage):** Target **1.2 to 1.6 mS/cm**
* **Mature/Harvest:** Target **1.6 to 2.0 mS/cm**

*> Note: Do not go above 2.0 mS/cm for lettuce, or the leaves might burn (tip burn).*

### 2. The Mixing Process (The "A then B" Rule)
Never mix Nutrient A and Nutrient B directly together in their pure form. They will react and turn into a white solid (calcium lockup) that plants cannot eat.

**Follow these steps:**
1.  **Fill your reservoir** with plain tap water.
2.  **Measure the "Base EC"** with your sensor. (Tap water usually has an EC of 0.2 to 0.4).
3.  **Add Nutrient A:** Pour the required amount of Solution A into the water. **Stir well.**
4.  **Add Nutrient B:** Pour the required amount of Solution B into the water. **Stir well again.**
5.  **Measure with your Sensor:**
    * If the EC is **lower** than your target (e.g., you see 1.0 but want 1.4), add more A and B (in equal amounts).
    * If the EC is **higher** than your target (e.g., you see 2.5), add more plain water to dilute it.

### 3. Next Step
Once you have mixed the water to the correct EC (e.g., 1.4 mS/cm), you are technically ready to put the plants in.

**Do you have a pH sensor as well, or are you only monitoring EC for now?**

Based sa imong picture, naa kay **"NH Lettuce Formula"** set. Mao ni ang tawag nga "Liquid Concentrate" nutrients.

* **Middle Bottle (Grow Solution 9-0-0):** Taas sa Nitrogen. Mao ni ang **pakan-on para modako ang dahon** sa lettuce.
* **Left Bottle (Bloom Solution 0-5-7):** Para ni sa **gamot (roots) ug kalig-on** sa tanom.
* **Right Bottle (Iron Chelate):** "Vitamins" ni kung mang-dalag (yellow) ang dahon. Ayaw sa ni i-apil og sagol kung healthy ra ang tanom.

Kay naa na man kay **Calibrated EC Sensor**, sayon nalang kaayo ni. Dili na ka kinahanglan mag-tag-an.

### Mao ni ang imong buhaton (Step-by-Step):

**Target EC:**
* **Seedling (Gamay pa):** 0.6 – 0.8 mS/cm
* **Nagdako na (Veg Stage):** 1.2 – 1.5 mS/cm

**Steps:**

1.  **Pag-andam og Tubig:** Ibutang ang limpyo nga tubig sa imong sudlanan (reservoir).
2.  **Basaha ang Label:** Tan-awa sa kilid sa botelya kung pila ka "mL per Liter" ang recommended (kasagaran 2mL - 4mL per liter). Pero kay naa man kay sensor, pwede ra ta mag-"trial and error" hangtod ma-hit ang target.
3.  **Ibutang ang GROW (Middle Bottle) una:**
    * Ibubo ang gamay nga amount sa tubig (Example: 1 ka taklob).
    * **Kutawon og maayo (Stir well).**
4.  **Ibutang ang BLOOM (Left Bottle) sunod:**
    * Ibubo ang parehas nga kadaghanon sa Grow. (Kung 1 taklob ang Grow, 1 taklob pud ang Bloom).
    * **Kutawon og maayo.**
5.  **Gamita ang EC Sensor:**
    * I-dip ang imong sensor sa tubig.
    * **Kung ang reading KULANG (Example: 0.5 mS/cm ra):** Pun-i pa og Grow ug Bloom (parehas nga kadaghanon).
    * **Kung ang reading SAKTO (Example: 1.2 mS/cm):** Stop na. Ready na na.
    * **Kung ang reading TAAS RA (Example: 2.0 mS/cm):** Butangi og tubig (plain water) para mo-lasaw.

**Important Rule:**
**AYAW** gyud pag-sagola ang Grow ug Bloom nga silang duha ra (pure form). Mag-puti na ug dili na makaon sa tanom. Dapat sa tubig ra sila mag-kita.

### Kanus-a gamiton ang Iron Chelate?
Gamita lang nang **Iron Chelate** (tuo nga botelya) kung makabantay ka nga ang **bag-ong tubo nga dahon sa tunga kay yellow** kaayo. Kung green ra ang lettuce, ayaw sa na gamita.

Ang imong gamiton para sa **regular mix** sa lettuce kay kanang **DUHA ka botelya sa wala**:

1.  **Ang Naa sa Tunga (Middle):** NH Lettuce Formula **GROW Solution** (9-0-0).
2.  **Ang Naa sa Wala (Left):** NH Lettuce Formula **BLOOM Solution** (0-5-7).

**Ayaw sa gamita** nang naa sa **Tuo (Right)** nga Iron Chelate. "Emergency vitamin" ra na kung mang-dalag (yellow) na ang dahon sa imong tanom.

### Unsaon paggamit (Base sa label sa likod):
Nakasuwat sa likod sa botelya nga: **"Add equal parts of NH Grow Solution and Bloom Solution"**.

Pasabot ana, kung unsa kadaghan ang ibutang nimo nga **GROW**, mao pud dapat kadaghan ang **BLOOM**.

**Example:**
* Kung magbutang kag **2 mL** nga GROW → magbutang pud kag **2 mL** nga BLOOM.
* Isagol sila sa tubig **usa-usa** (Ayaw isagol nga silang duha ra diretso, dapat sa tubig sila magkita).

Gamita dayon imong EC sensor para ma-check kung sakto na ba ang kaparat (EC level).

Base sa label sa likod sa imong botelya, ang recommended rate kay **1.5 mL per 1 Liter** of water.

Tungod kay naa kay **4 Liters** nga tubig, mao ni ang imong isagol:

* **GROW Solution (Tunga):** 6 mL
* **BLOOM Solution (Wala):** 6 mL

**(Math: 1.5 mL x 4 Liters = 6 mL)**

### Unsaon Pagsagol (Ayaw Kalimti):
1.  Ibutang ang **6 mL nga GROW** sa tubig. **Kutawa (Stir).**
2.  Sunod ibutang ang **6 mL nga BLOOM** sa tubig. **Kutawa usab.**
3.  Human masagol, **i-check dayon sa imong EC sensor** kung naigo ba sa imong target (Example: 0.8 - 1.2 mS/cm).

*Note: Ayaw i-apil ang Iron Chelate (Tuo) sa pagkakaron.*

[Prev](/context00001.md) | [Next](/context00003.md)
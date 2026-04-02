# Summary of Interaction: EC Sensor & ADS1115 Setup

This interaction focused on the hardware assembly and wiring of a DFRobot EC Sensor to a Raspberry Pi 4 using an ADS1115 ADC module.

## ✅ What is Working (Final Configuration)

### 1. Hardware Preparation
*   **ADS1115 Soldering:** Completed. Header pins are soldered with the short side through the top (chip side) and long pins pointing down for breadboard insertion.
*   **Breadboard Placement:** The ADS1115 module correctly straddles the center gap of the breadboard to isolate the two rows of pins.

### 2. Critical Wiring (3.3V Logic)
*   **Power (VDD):** Must connect to **Raspberry Pi Pin 1 (3.3V)**.
*   **Pin Identification:** Pin 1 is on the **INNER ROW** (closer to the Raspberry Pi logo and silver chips).
*   **I2C Data:** SDA connects to Pin 3; SCL connects to Pin 5.
*   **Ground:** G (GND) and ADDR both connect to Pi Pin 6 (GND). Connecting ADDR to GND sets the I2C address to `0x48`.
*   **Sensor Input:** The EC sensor signal wire connects to **A0** on the ADS1115.

### 3. Software Prerequisite
*   I2C must be enabled via `sudo raspi-config` -> Interface Options -> I2C -> Yes, followed by a reboot.

---

## ❌ What was Rejected (Errors to Avoid)

*   **No Loose Connections:** Attempting to use the ADS1115 without soldering the header pins was rejected; loose pins provide unreliable data.
*   **Avoid 5V (Pin 2):** The user repeatedly attempted to connect power to the **OUTER ROW (Pin 2)**. This was strongly rejected as Pin 2 provides **5V**, which would send 5V signals back to the Pi's 3.3V GPIO pins and potentially destroy the processor.
*   **Diagram Confusion:** Relying on rotated software diagrams instead of the physical board layout led to incorrect pin identification. The "Inner vs. Outer" rule for the physical board is the source of truth.

---

## 📍 Final Wiring Table

| ADS1115 Pin | Raspberry Pi Pin | Function |
| :--- | :--- | :--- |
| **V (VDD)** | **Pin 1 (3.3V - INNER)** | Power |
| **G (GND)** | **Pin 6 (GND - OUTER)** | Ground |
| **SCL** | **Pin 5 (SCL - INNER)** | I2C Clock |
| **SDA** | **Pin 3 (SDA - INNER)** | I2C Data |
| **ADDR** | **Pin 6 (GND)** | Sets Address 0x48 |
| **A0** | **Sensor Signal** | Analog Input |

[Prev](/context00003.md) | [Next](/context00005.md)

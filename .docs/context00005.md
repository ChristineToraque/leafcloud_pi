[Prev](/context00004.md) | [Next](/context00006.md)

# Explanation of `leaf_node.py` Output

The output shows that the script is successfully communicating with the ADS1115 and the internal logic (like the pH averaging buffer) is working. However, the data itself indicates several hardware or calibration issues.

### 1. Temp (°C): `N/A`
*   **Status:** **FAILED**
*   **Why:** The script cannot find the 1-Wire device file (usually in `/sys/bus/w1/devices/28-*`).
*   **Action:** 
    *   Ensure the **DS18B20** temperature sensor is wired correctly (Data pin to GPIO 4 with a 4.7k resistor).
    *   Confirm 1-Wire is enabled: `sudo raspi-config` -> Interface Options -> 1-Wire -> Yes.

### 2. EC (mS/cm): `0.02` - `0.03`
*   **Status:** **IDLE/AIR READING**
*   **Why:** This value is extremely low, which is normal if the probe is dry or in distilled water.
*   **Action:** If the probe is in nutrient solution, you must calibrate the `EC_K_VALUE` in the script to match a known EC standard.

### 3. pH Level: `15.95`
*   **Status:** **INVALID / OUT OF BOUNDS**
*   **Why:** The pH scale is typically 0–14. A reading of ~16 suggests the voltage at **Pin A1** is very low (around 0.8V–0.9V).
*   **Action:** 
    *   Ensure the pH driver board is powered by **3.3V** and the signal wire is firmly connected to **A1**.
    *   Check if the BNC connector on the probe is tight.
    *   Calibration is required: The `PH_NEUTRAL_VOLTAGE` (currently 2.5V) and `PH_STEP_VOLTAGE` (0.18V) need to be adjusted based on readings from pH 4.0 and pH 7.0 buffer solutions.

### 4. Status: `Stabilizing` vs `Running`
*   **Status:** **WORKING**
*   **Why:** To prevent "jittery" data, the script collects a buffer of 20 readings for the pH sensor.
    *   **Stabilizing:** The script is filling the first 20 slots of the buffer.
    *   **Running:** The buffer is full, and the displayed pH is now a stable moving average.

---

### Summary Table of Current State
| Sensor | Data Result | Conclusion |
| :--- | :--- | :--- |
| **Temperature** | `N/A` | Hardware connection or 1-Wire setting error. |
| **EC Sensor** | `0.03 mS/cm` | Working, but likely reading air or needs calibration. |
| **pH Sensor** | `15.95` | Signal is too low; check A1 wiring or calibrate offset. |

# EC Calibration Formula

To calibrate the EC sensor, we use the ratio of the target solution value to the current reading to adjust the multiplier (`EC_K_VALUE`).

## Formula
The new K-value is calculated as:

$$K_{new} = K_{old} \times \left( \frac{EC_{target}}{EC_{reading}} \right)$$

## Recent Calibration (Example)
In the most recent adjustment, the sensor read **1.50 mS/cm** in a **1.413 mS/cm** (1413 µS/cm) solution using a K-value of **6.43**.

**Calculation:**
$$6.43 \times \left( \frac{1.413}{1.50} \right) \approx 6.06$$

The `EC_K_VALUE` in `leaf_node.py` was updated to **6.06** to match the solution concentration.

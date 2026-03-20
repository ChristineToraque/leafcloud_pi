import sys
import select
import termios
import tty
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# --- CONFIGURATION ---
# K_VALUE: Usbon ni nimo para ma-calibrate.
# Kung taas ra ang reading sa screen, paubsi ni. Kung ubos ra, pataasi.
# Default is 1.0 just for testing.
k_value = 8.65

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADS object
ads = ADS.ADS1115(i2c)

# Create the Analog Input on Pin A0
channel = AnalogIn(ads, 0)

print("Reading EC Sensor Data...")
print("Press 'q' to quit.")
print("-" * 50)
print("{:>10} | {:>10} | {:>15}".format("Voltage", "Raw Value", "EC (mS/cm)"))
print("-" * 50)

def is_q_pressed():
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.read(1).lower() == 'q'
    return False

# Save old terminal settings
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
    # Set to cbreak mode to read single keypress without Enter
    tty.setcbreak(fd)

    while True:
        voltage = channel.voltage
        raw_value = channel.value

        # --- FORMULA SA EC ---
        # Ang basic conversion: EC = Voltage * K_Value
        # Note: Wala pay Temperature Compensation ani (Assuming 25°C standard)
        ec_value = voltage * k_value

        print("{:>10.4f} | {:>10} | {:>15.2f} mS/cm".format(voltage, raw_value, ec_value))

        # Non-blocking wait for 1.0 second, checking for 'q'
        start_time = time.time()
        while time.time() - start_time < 1.0:
            if is_q_pressed():
                print("\nExiting...")
                sys.exit(0)
            time.sleep(0.1)

finally:
    # Restore terminal settings
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
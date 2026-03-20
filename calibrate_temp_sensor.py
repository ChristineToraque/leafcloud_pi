import os
import glob
import time
import sys
import select
import tty
import termios

# Find the sensor file path automatically
base_dir = '/sys/bus/w1/devices/'
print("Looking for temperature sensor in:", base_dir)
try:
    device_folder = glob.glob(base_dir + '28*')[0]
    print("Found temperature sensor in:", device_folder)
    device_file = device_folder + '/w1_slave'
    print("Temperature sensor file path:", device_file)
except IndexError:
    print("No temperature sensor found. Is the device connected?")
    device_file = None

def read_temp_raw():
    if device_file is None:
        return []
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()

    if not lines:
        return 0.0

    # Wait if the sensor is not ready (YES indicates ready)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()

    # Find the temperature position
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
    return 0.0

# Main loop
if device_file:
    print("Press 'q' to exit...")
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())
        while True:
            temperature = read_temp()
            print(f"Current Water Temp: {temperature:.2f} °C")

            # Wait for 1 second or input
            if select.select([sys.stdin], [], [], 1)[0]:
                c = sys.stdin.read(1)
                if c == 'q':
                    break
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
else:
    print("Exiting due to missing sensor.")

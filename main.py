import RPi.GPIO as GPIO
from pad4pi import rpi_gpio

# Define keypad layout (matrix 4x4)
KEYPAD = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

# GPIO pin setup (BCM mode)
ROW_PINS = [4, 17, 27, 22]     # Connect to R1, R2, R3, R4
COL_PINS = [5, 6, 13, 19]      # Connect to C1, C2, C3, C4

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def handle_key_press(key):
    print(f"Key Pressed: {key}")
    # You can trigger actions based on key here

keypad.registerKeyPressHandler(handle_key_press)

print("Ready. Press keys on the keypad. Ctrl+C to quit.")
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    GPIO.cleanup()


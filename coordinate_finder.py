import pyautogui
import time
import sys

print("Move your mouse cursor to the desired location.")
print("The current coordinates will be displayed below.")
print("Press Ctrl+C in the terminal to quit.")

try:
    while True:
        # Get current mouse coordinates
        x, y = pyautogui.position()

        # Format the coordinate string
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        # Print the coordinates, overwriting the previous line
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

        # Short pause to prevent high CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print('\nCoordinate finder stopped.')
except Exception as e:
    # Handle potential errors, like pyautogui not being installed
    print(f"\nAn error occurred: {e}")
    print("\nPlease ensure you have the 'pyautogui' library installed.")
    print("You can install it by running this command in your terminal:")
    print("pip install pyautogui")
    sys.exit(1)

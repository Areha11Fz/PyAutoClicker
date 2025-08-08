import time
import pyautogui
import datetime

# =========================
# Debug mode setting
DEBUG = True  # Set to True for debug mode (run after X seconds), False for actual date/time
# =========================

# User-configurable settings
# =========================
# Set the target date and time for when the click should happen
YEAR = 2025
MONTH = 8      # 1-12 (January = 1, December = 12)
DAY = 8        # 1-31 (day of the month)
HOUR = 15      # 0-23 (24-hour format, 2:00 PM = 14)
MINUTE = 38    # 0-59
SECOND = 20    # 0-59
MILLISECOND = 0  # 0-999 (1/1000th of a second precision)

# Set the screen coordinates for the INITIAL click
# INITIAL_CLICK_X = 1422 # Select Product Reg Version
# INITIAL_CLICK_Y = 345

INITIAL_CLICK_X = 1393 # Select Product Lite Version
INITIAL_CLICK_Y = 307

# Set the screen coordinates for the subsequent SPAM click
SPAM_CLICK_X = 2117
SPAM_CLICK_Y = 1986
# =========================

def main():
    if DEBUG:
        debug_seconds = 2
        target_date = datetime.datetime.now() + datetime.timedelta(seconds=debug_seconds)
        print(f"[DEBUG MODE] Target time set to {debug_seconds} seconds from now.")
    else:
        microseconds = MILLISECOND * 1000
        target_date = datetime.datetime(YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, microseconds)

    target_timestamp = target_date.timestamp()
    current_time = time.time()
    delay = target_timestamp - current_time

    print(f"Current time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
    print(f"Target time: {target_date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")

    if delay > 0:
        print(f"Waiting for {delay:.2f} seconds (about {delay/60:.2f} minutes)...")
        time.sleep(delay)
        
        # Perform initial single click
        print(f"Performing initial click at ({INITIAL_CLICK_X}, {INITIAL_CLICK_Y})...")
        pyautogui.moveTo(INITIAL_CLICK_X, INITIAL_CLICK_Y, duration=0)
        pyautogui.click(x=INITIAL_CLICK_X, y=INITIAL_CLICK_Y)
        print("Initial click done.")
        
        # Perform spam click for 5 seconds at the second location
        print(f"Performing spam click at ({SPAM_CLICK_X}, {SPAM_CLICK_Y}) for 5 seconds...")
        start_time = time.time()
        duration = 5  # seconds
        clicks = 0

        # Start
        pyautogui.moveTo(SPAM_CLICK_X, SPAM_CLICK_Y, duration=0)
        while time.time() < start_time + duration:
            pyautogui.click(x=SPAM_CLICK_X, y=SPAM_CLICK_Y)
            clicks += 1
            # Optional: Add a very small delay if needed to avoid overwhelming the system,
            # but for spam clicking, usually no delay is desired.
            # time.sleep(0.01)
            
        print(f"Spam clicking finished after {duration} seconds.")
        print(f"Performed approximately {clicks} clicks at coordinates ({SPAM_CLICK_X}, {SPAM_CLICK_Y})")
    else:
        print("The target time is in the past. Please set a future time.")

if __name__ == "__main__":
    main()

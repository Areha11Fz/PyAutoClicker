import time
import pyautogui
import datetime

# User-configurable settings
# =========================
# Set the target date and time for when the click should happen
YEAR = 2025
MONTH = 5      # 1-12 (January = 1, December = 12)
DAY = 4        # 1-31 (day of the month)
HOUR = 14      # 0-23 (24-hour format, 2:00 PM = 14)
MINUTE = 30    # 0-59
SECOND = 0     # 0-59
MILLISECOND = 0  # 0-999 (1/1000th of a second precision)

# Set the screen coordinates for the click
CLICK_X = 500  # X-coordinate on screen
CLICK_Y = 300  # Y-coordinate on screen
# =========================

def main():
    # Create a datetime object from the user settings
    # Note: datetime uses microseconds (1/1,000,000 sec), so we convert milliseconds (1/1,000 sec) to microseconds
    microseconds = MILLISECOND * 1000  # Convert milliseconds to microseconds
    target_date = datetime.datetime(YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, microseconds)
    
    # Convert to timestamp
    target_timestamp = target_date.timestamp()
    
    # Calculate delay (in seconds)
    current_time = time.time()
    delay = target_timestamp - current_time
    
    # Display information
    print(f"Current time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
    print(f"Target time: {target_date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
    
    if delay > 0:
        print(f"Waiting for {delay:.2f} seconds (about {delay/60:.2f} minutes)...")
        time.sleep(delay)
        print("Performing click now!")
        pyautogui.click(x=CLICK_X, y=CLICK_Y)
        print(f"Click performed at coordinates ({CLICK_X}, {CLICK_Y})")
    else:
        print("The target time is in the past. Please set a future time.")

if __name__ == "__main__":
    main()

import time
import pyautogui
import datetime

# User-configurable settings
# =========================
# Set the target date and time for when the click should happen
YEAR = 2025
MONTH = 8      # 1-12 (January = 1, December = 12)
DAY = 8        # 1-31 (day of the month)
HOUR = 0      # 0-23 (24-hour format, 2:00 PM = 14)
MINUTE = 49    # 0-59
SECOND = 59     # 0-59
MILLISECOND = 800  # 0-999 (1/1000th of a second precision)

# Set the screen coordinates for the INITIAL click
INITIAL_CLICK_X = 1422
INITIAL_CLICK_Y = 345

# INITIAL_CLICK_X = 960
# INITIAL_CLICK_Y = 342

# Set the screen coordinates for the subsequent SPAM click
SPAM_CLICK_X = 2117
SPAM_CLICK_Y = 1986
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
        
        # # Perform initial single click
        # print(f"Performing initial click at ({INITIAL_CLICK_X}, {INITIAL_CLICK_Y})...")
        # pyautogui.click(x=INITIAL_CLICK_X, y=INITIAL_CLICK_Y)
        # print("Initial click done.")
        
        # Perform spam click for 5 seconds at the second location
        print(f"Performing spam click at ({SPAM_CLICK_X}, {SPAM_CLICK_Y}) for 5 seconds...")
        start_time = time.time()
        duration = 5  # seconds
        clicks = 0
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

import time, pyautogui
target_timestamp =  time.mktime((2025,5,4,14,30,0,0,0,0))
delay = target_timestamp - time.time()
if delay > 0:
    time.sleep(delay)
    pyautogui.click(x=500, y=300)

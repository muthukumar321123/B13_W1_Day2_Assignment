import pyautogui
import time

pyautogui.moveTo(100, 100, duration=1)  # Move the mouse to (100, 100) over 1 second
#pyautogui.doubleClick(100, 100)  # Double-click at (100, 100)
pyautogui.rightClick(100, 100)  # Right-click at (100, 100)
pyautogui.click(100, 100)  # Click at (100, 100)
time.sleep(5)  # Wait for 1 second
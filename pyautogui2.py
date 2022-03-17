import pyautogui
import time
print(pyautogui.size()) # resolution of screen
time.sleep(3) # take a break
pyautogui.moveTo(x, y, time) # move slowly during time
pyautogui.moveRel(x, y, time) # move relative to
pyautogui.click(x, y, n, time, button="left")
pyautogui.tripleClick() # doubleClick, leftClick, rightClick
pyautogui.scroll(500) # scroll wheel
# .mouseUp, mouse.Down, hold button draw
# .dragRel, drag relative


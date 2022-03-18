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

# keyboard functions
pyautogui.write("hello")
pyautogui.press("enter") # press keyboard

# screenshot
pyautogui.screenshot("name.png") # save picture

# look for button location
button7location = pyautogui.locateOnScreen('calc7key.png')
# button7location:
# Box(left=1416, top=562, width=50, height=41)
button7point = pyautogui.center(button7location)
button7x, button7y = button7point
pyautogui.click(button7x, button7y)  # clicks the center of where the 7 button was found
pyautogui.click('calc7key.png') # a shortcut version to click on the center of where the 7 button was found

# find pixel location, mouse click, type words, press enter
import pyautogui
print(pyautogui.position()) # place mouse, get pixel
pyautogui.click(x, y)
pyautogui.typewrite("abc")
pyautogui.typewrite(["Enter"]) # search in address bar
#hot key
pyautogui.hotkey("control", "c") # copy url


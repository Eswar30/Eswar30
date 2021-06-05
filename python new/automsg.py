import pyautogui
import time
message = int(input("Enter no of times\n"))
while message > 0:
#    time.sleep(1)
    pyautogui.typewrite('Hello karthi')
#    time.sleep(1)
    pyautogui.press('enter')
    message  = message - 1


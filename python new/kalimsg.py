import pyautogui
import time
time.sleep(5)
# message = int(input("Enter no of times\n"))
message=1
while message > 0:
#    time.sleep(1)
    pyautogui.typewrite('curl -X POST https://textbelt.com/text \\')
    pyautogui.press('enter')
    pyautogui.typewrite('--data-urlencode phone=\'+91 8074611376\'\\')
    pyautogui.press('enter')
    pyautogui.typewrite('--data-urlencode message=\'Hello\'\\')
    pyautogui.press('enter')
    pyautogui.typewrite('-d key=textbelt')
    pyautogui.press('enter')
#    time.sleep(1)
    pyautogui.press('enter')
    message  = message - 1

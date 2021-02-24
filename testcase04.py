# coding=utf-8

#投注 B100, b100 , T100, t100, BP100, bp100
import pyautogui
import pyperclip
import time

def tc04():
    print("TestCase04 Start")
    #size = pyautogui.size()
    #pyautogui.click(1217, 12, duration=2)
    #pyautogui.typewrite("LINE")
    #pyautogui.typewrite(["enter"])

    for i in range(0, 30):
        # LineBot confirm
        pyautogui.click(139, 86, duration=2)  # LineSearch
        pyautogui.typewrite("Yabo Thai")  # GroupName
        pyautogui.click(238, 146, duration=2)
        pyperclip.copy("余额")
        pyautogui.hotkey('command', 'v')
        pyautogui.typewrite(["enter"])
        time.sleep(3)
        balance = pyautogui.screenshot()
        balance.save('GameStart_balance.png')
        time.sleep(3)
        pyautogui.click(338, 85, duration=1)  # ClickClear

        # into Group1 test
        pyautogui.click(139, 86, duration=2)  # LineSearch
        pyautogui.typewrite("SexyLineStgG1")  # GroupName
        pyautogui.click(238, 146, duration=1)

        # Bet game
        pyautogui.typewrite("B100")
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyautogui.typewrite("b100")
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyautogui.typewrite("T100")
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyautogui.typewrite("t100")
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyautogui.typewrite("BP100")
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyautogui.typewrite("bp100")
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyautogui.typewrite("donate150")
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyautogui.click(338, 85, duration=1)  # ClickClear

        # LineBot Confirm
        pyautogui.click(139, 86, duration=2)  # LineSearch
        pyautogui.typewrite("Yabo Thai")  # GroupName
        pyautogui.click(238, 146, duration=2)
        pyperclip.copy("余额")
        pyautogui.hotkey('command', 'v')
        pyautogui.typewrite(["enter"])
        time.sleep(3)
        balance = pyautogui.screenshot()
        balance.save('balance.png')
        time.sleep(3)
        pyautogui.click(338, 85, duration=1)  # ClickClear
        print("Round", i + 1, "-- Done")
    print("TestCase04 Run Done")
    #pyautogui.click(14, 14, duration=2)  # closebtn





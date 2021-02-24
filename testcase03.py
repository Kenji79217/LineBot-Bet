# coding=utf-8

#投注 P100/t100/PP100/pp100/ไพ่คู่เพลเยอร์ 100

import pyautogui
import pyperclip
import time

def tc03():
    print("TestCase03 Start")
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
        pyautogui.typewrite("P100")
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyautogui.typewrite("t100")
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyautogui.typewrite("PP100")
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyautogui.typewrite("pp100")
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyperclip.copy("ไพ่คู่เพลเยอร์ 100")
        pyautogui.hotkey('command', 'v')
        pyautogui.typewrite(["enter"])
        time.sleep(2)
        pyperclip.copy("ให้ทิป 150")
        pyautogui.hotkey('command', 'v')
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
    print("TestCase03 Run Done")
    #pyautogui.click(14, 14, duration=2)  # closebtn





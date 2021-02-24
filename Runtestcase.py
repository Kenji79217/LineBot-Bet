import testcase01 as one
import testcase02 as two
import testcase03 as three
import testcase04 as four
import testcase05 as five
import testcase06 as six
import testcase07 as seven
import testcase08 as eight
import pyautogui




size = pyautogui.size()
pyautogui.click(1217, 12, duration=2)
pyautogui.typewrite("LINE")
pyautogui.typewrite(["enter"])

one.tc01()
two.tc02()
three.tc03()
four.tc04()
five.tc05()
six.tc06()
seven.tc07()
eight.tc08()

pyautogui.click(14, 14, duration=2)  # closebtn
print('Finished')



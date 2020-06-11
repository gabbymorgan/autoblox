import time
import pyautogui
from sys import platform

if platform == 'win32':
    import winsound
else:
    import os

pyautogui.FAILSAFE = True
sPath = input('Path of source: ')
source = open(sPath, 'r')
separator = input('Separator: ')
blocks = source.read().split(separator)
ready = input(
    "Position your mouse over the window you wish to type into, then press ENTER.")

# Count down and then click
time.sleep(1)
print(5)
time.sleep(1)
print(4)
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
pyautogui.click()

# Type!
for i in range(len(blocks)):
    for x in range(len(blocks[i])):
        pyautogui.press(blocks[i][x])

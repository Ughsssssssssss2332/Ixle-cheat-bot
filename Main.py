#!/usr/bin/python3

# Importing modules
print("Importing modules...")

import sys
import os

try:
    import pyautogui as pygui
except:
    print("You need to install the pyautogui module (pip install pyautogui).")
    sys.exit()
# ------------------------This will be removed later----------------------------
try:
    import cv2
except:
    print("You need to install the cv2 module (pip install opencv-python).")
    sys.exit()

try:
    import pytesseract
except:
    print("You need to install the pytesseract module (pip install pytesseract).")
    sys.exit()

# ------------------------------------------------------------------------------

cd = os.getcwd()
sys.path.insert(1, cd+'/Data/ExternalModules')

from ScreenshotVerify import screenshot_verify

from ScreenshotModules import take_screenshot

from MainMenu import main_menu

sys.path.insert(1, cd)

print("Done!")

print()
print()
print()

def take_screenshot_func():
    dir = cd+"/Data/Screenshot"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    take_screenshot()
    return "Done!"

# Prints keyboard and screenshot warning if it's the first time running.
screenshot_verify()

# This is where the actual script starts
pygui.alert("Welcome.")

# Displays the main menu
main_menu()

# This is the main loop. It will later be removed.
while True:
    main_input = pygui.confirm("...", buttons=["Scan", "Quit"])

    if main_input == "Quit":
        sys.exit()
    elif main_input == "Scan":
        take_screenshot_func()
    else:
        pygui.alert("Please enter a valid action.")

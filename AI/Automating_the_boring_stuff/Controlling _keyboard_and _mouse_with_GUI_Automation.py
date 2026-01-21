#January 21, 2026
'''Way to solve out of control GUI automation:
1.Log out by pressing CTRL + ALT + DEL
2. Asking you progrma to puse for an amount of time. For example, setting pyautogui.PAUSE = 1.5,
every PYAUTOGUI function will wait 1.5s after running.
NB: Non-PYAUTOGUI codes will not have this pause.
3. Uisng the fail-safe feature:This feature stops the PYAUTOGUI scripts when the mouse cursor is moved  as far up and left as possible
NB: You can disable this feature by  setting pyautogui.FAILSAFE = False'''

#Controlling mouse movement.
#The mouse position is determined by coordiabnte frame where the upper left corner of the screen is  (0,0) and the downward right coner is the maximum coordiante.
import pyautogui
print(pyautogui.size()) #Output: Returns two-integer tuple of the screen's width and height in pixels

#Moving the mouse: we use the .moveTo() method to move the mouse to a specified location
import pyautogui
for i in range(2):
    pyautogui.moveTo(100,100, .25)
    pyautogui.moveTo(200,100, .25)
    pyautogui.moveTo(200,200, .25)
    pyautogui.moveTo(100,200, .25)

#The third input is for duration and it's optional

#The .moveRel() funtion moves the mosue relative to it's initial position
import pyautogui
for i in range(2):
    pyautogui.moveRel(100, 0, .25)
    pyautogui.moveRel(0, 100, .25)
    pyautogui.moveRel(-100, 0, .25)
    pyautogui.moveRel(0, -100, .25)

#Getting the mouse position
print(pyautogui.position())
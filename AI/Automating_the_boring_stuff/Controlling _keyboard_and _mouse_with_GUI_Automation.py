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


# March 9, 2026
#Clicking the Mouse
'''
The default mouse button is the left mouse button
The pyautogui.mouseDown() pushes the mouse button down and pyautogui.mouseUp() releases the mouse button.
The combination of the two activity is the pyautogui.click().

Other clicking activities are:
-pyautogui.doubleClick(): Performs two clicks with the left mouse button
-pyautogui.rightClick(): performs a click with the right mouse button
-pyautogui.middleClick():performs a click with middle mouse button
Example:
'''
import pyautogui
pyautogui.click(10,5) #Moves the cursor to 10,5 and left click
                
#Dragging the Mouse
'''
PyAutoGUI provides the pyautogui.dragTo() and pyautogui.dragRel()
functions to drag the mouse cursor to a new location or a location relative to its current one. The arguments for dragTo() and dragRel() are the 
same as moveTo() and moveRel(): the x-coordinate/horizontal movement, the 
y-coordinate/vertical movement, and an optional duration of time. (OS X 
does not drag correctly when the mouse moves too quickly, so passing a 
duration keyword argument is recommended.)


 sample code
'''
import pyautogui, time
time.sleep(5)
pyautogui.click() # click to put drawing program in focus
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2) # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2) # move down
    pyautogui.dragRel(-distance, 0, duration=0.2) # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2) # move up


#Scrolling the Mouse
import pyautogui
pyautogui.scroll(200) #Scrolls up by 200px


#March 10, 2026
# Controlling the Keyboard

'''Sending a string from the keyboard
sample code:
'''
pyautogui.click(100,100)
pyautogui.typewrite('Hello World!')

#A  second argument of float integers in the typewrite function would pause the typing for the stipulated number of seconds before typing the next letter

'''Key Names:
Some keys  are represented with a string . examples are the 
'shift' for the Shift key, 'esc' for the esc key, etc.
'''
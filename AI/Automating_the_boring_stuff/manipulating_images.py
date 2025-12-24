#December 23, 2025
'''Colors and RGBA Values:
Computer programs often represent a color in an image as an RGBA value. 
An RGBA value is a group of numbers that specify the amount of red, green, 
blue, and alpha (or transparency) in a color.

Each of these component values is an integer from 0 (none at all) to 255 (the maximum). These RGBA values 
are assigned to individual pixels; 
a pixel is the smallest dot of a single color the computer screen can show (there are millions of 
pixels on a screen). 

A pixel’s RGB setting tells it precisely what shade of color it should display. Images also have an alpha value to create RGBA 
values. If an image is displayed on the screen over a background image 
or desktop wallpaper, the alpha value determines how much of the background you can “see through” the image’s pixel.

In Pillow, RGBA values are represented by a tuple of four integer values. 
For example, the color red is represented by (255, 0, 0, 255). This color has 
the maximum amount of red, no green or blue, and the maximum alpha 
value, meaning it is fully opaque. 

Green is represented by (0, 255, 0, 255), 
and blue is (0, 0, 255, 255). 

White, the combination of all colors, is (255, 
255, 255, 255), while black, which has no color at all, is (0, 0, 0, 255).

If a color has an alpha value of 0, it is invisible, and it doesn’t really matter what the RGB values are. 
After all, invisible red looks the same as invisible black.

Standard Color Names and Their RGBA Values:

Name             RGBA value             Name    RGBA value
White           (255, 255, 255, 255)    Red     (255, 0, 0, 255)
Green           (0, 128, 0, 255)        Blue    (0, 0, 255, 255)
Gray            (128, 128, 128, 255)    Yellow  (255, 255, 0, 255)
Black           (0, 0, 0, 255)          Purple  (128, 0, 128, 255)


Note:
Pillow offers the ImageColor.getcolor() function so you don’t have to 
memorize RGBA values for the colors you want to use. This function takes 
a color name string as its first argument, and the string 'RGBA' as its second 
argument, and it returns an RGBA tuple.

Example:
'''
from PIL import ImageColor
print(ImageColor.getcolor('red', 'RGBA')) # Output: (255, 0, 0, 255)
print(ImageColor.getcolor('chartreuse', 'RGBA')) # Output: (127, 255, 0, 255)
print(ImageColor.getcolor('hotpink', 'RGBA')) # Output: (255, 105, 180, 255)
print(ImageColor.getcolor('aliceblue', 'RGBA')) # Output: (240, 248, 255, 255)  
print(ImageColor.getcolor('lavenderblush', 'RGBA')) # Output: (255, 240, 245, 255)  

'''Coordinate and Box Tuples:
Many of Pillow’s functions and methods take a box tuple argument. 
This means Pillow is expecting a tuple of four integer coordinates that represent a rectangular region in an image. 

The four integers are, in order, as follows:
•	 Left: The x-coordinate of the leftmost edge of the box.

•	 Top: The y-coordinate of the top edge of the box.

•	 Right: The x-coordinate of one pixel to the right of the rightmost edge of the box. This integer must be greater 
than the left integer.

•	 Bottom: The y-coordinate of one pixel lower than the bottom edge of the box. 
This integer must be greater than the top integer.
For example, the box tuple (100, 200, 300, 400) represents the rectangular region that starts at pixel (100, 200) in the upper-left corner and ends at pixel (299, 399) in the lower-right corner. 
The width of this box is 200 pixels (300 − 100), and the height is also 200 pixels (400 − 200).'''


'''Manipulating Images with the Pillow Module
The Pillow module (PIL) is a powerful library for opening, manipulating, and saving many different image file formats in Python.
To use Pillow, you must first install it using pip. You can do this by running the following command in your terminal or command prompt:
pip install Pillow  '''

#Loading Images
from PIL import Image
img = Image.open('AI\\Automating_the_boring_stuff\\example.png') #The image's file path
img.show()

#Getting Image Information
print(img.filename) #Output: AI\Automating_the_boring_stuff\example.png
print(img.format)   #Output: PNG
print(img.size)     #Output: (640, 480)
print(img.mode)     #Output: RGBA


'''Cropping Images:
You can crop an image to a rectangular region using the crop() method.
Cropping an image means selecting a rectangular region inside an image 
and removing everything outside the rectangle.
The cropping does not happen in place—that is, the original Image object is left untouched, 
and the crop() method returns a new Image object. 
The crop() method takes a box tuple as its only argument.

Example:
'''
box = (100, 100, 400, 400)
croppedImg = img.crop(box)
croppedImg.show()

'''Saving Images:
You can save an image to a file using the save() method.
The save() method takes a string filename as its first argument.
Example:
'''
croppedImg.save('AI\\Automating_the_boring_stuff\\cropped_example.png')


#Copying and Pasting Images:
'''You can copy and paste rectangular regions of an image using the copy() and paste() methods, respectively.

Example Usage:
'''
copyImg = img.copy() #Create a copy of the original image
box = (50, 50, 200, 200) #Define the box tuple for the region to copy
region = copyImg.crop(box) #Crop the region from the copied image
copyImg.paste(region, (300, 300))#Paste the cropped region into a new location
copyImg.show() #Display the modified image
copyImg.save('AI\\Automating_the_boring_stuff\\pasted_example.png') #Save the modified image


#December 24, 2025
'''Resizing Images:
You can resize an image using the resize() method.
The resize() method is called on an Image object and returns a new Image object of the specified size.
The resize() method takes a tuple of two integers as its only argument, representing the new width and height of the image in pixels.
Example Usage:
'''
resizedImg = img.resize((100, 100)) #Resize the image to 100x100 pixels
resizedImg.show() #Display the resized image
resizedImg.save('AI\\Automating_the_boring_stuff\\resized_example.png') #Save the resized image

'''Rotating and Flipping Images:
You can rotate and flip images using the rotate() and transpose() methods, respectively.
The rotate() method takes a single argument, the angle in degrees to rotate the image counterclockwise.
The transpose() method takes a single argument that specifies the type of flip to perform.

Example Usage:  
'''
rotatedImg = img.rotate(90) #Rotate the image 90 degrees counterclockwise
rotatedImg.show() #Display the rotated image    
rotatedImg.save('AI\\Automating_the_boring_stuff\\rotated_example.png') #Save the rotated image
flippedImg = img.transpose(Image.FLIP_LEFT_RIGHT) #Flip the image horizontally
flippedImag2 = img.transpose(Image.FLIP_TOP_BOTTOM) #Flip the image vertically   
flippedImg.show() #Display the flipped image
flippedImag2.show() #Display the vertically flipped image  
flippedImag2.save('AI\\Automating_the_boring_stuff\\flipped_vertical_example.png') #Save the vertically flipped image   
flippedImg.save('AI\\Automating_the_boring_stuff\\flipped_example.png') #Save the flipped image

#The rotate() method has an optional second argument called expand.
#If this argument is set to True, the image size is adjusted to fit the entire rotated image.
rotatedImg2 = img.rotate(45, expand=True) #Rotate the image 45 degrees counterclockwise and expand the size
rotatedImg2.show() #Display the rotated and expanded image  
rotatedImg2.save('AI\\Automating_the_boring_stuff\\rotated_expanded_example.png') #Save the rotated and expanded image  

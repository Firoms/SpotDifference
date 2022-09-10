# Importing Image and ImageGrab module from PIL package 
from PIL import Image, ImageGrab
    
# creating an image object
im1 = Image.open(r"./testimg.png")
    
# using the grab method
im2 = ImageGrab.grab(bbox =(10, 10, 11, 11))
    
print(im2.getpixel((0,0)))

from .senseHat import PiSenseHat

"""
Class Emoji is used to create emoji from LED matrix and display them to senseHat
"""
class Emoji:
    def __init__(self, images):
        self.__images = images 
    
    def display(self):
        count = 0
        #Loop through all pixel emoji
        while count < 10:
            PiSenseHat.display_image_duration(self.__images[count % 4], 0.3)
            count += 1
from .senseHat import PiSenseHat

class Emoji:
    def __init__(self, images):
        self.__images = images 
    
    def display(self):
        count = 0
        while count < 10:
            PiSenseHat.display_image_duration(self.__images[count % 4], 0.3)
            count += 1
from .senseHat import SenseHat

class Emoji:
    def __init__(self, images):
        self.images = images 
    
    def display(self):
        count = 0
        while count < 10:
            SenseHat.display_image_duration(self.images[count % 4], 0.3)
            count += 1
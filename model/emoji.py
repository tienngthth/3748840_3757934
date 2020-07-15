from senseHAT import SenseHAT

class Emoji:
    def __init__(self, images):
        self.images = images
    
    def display(self):
        count = 0
        while count < 10:
            SenseHAT.display_image_duration(self.images[count % 4], 0.3)
            count += 1
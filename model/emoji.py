from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

class Emoji:
    def __init__(self, images):
        self.images = images
    
    def display(self):
        count = 0
        while count < 10:
            sense.set_pixels(self.images[count % 4])
            sleep(0.3)
            count += 1
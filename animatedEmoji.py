from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Define some colours
g = (0, 255, 0) # Green
r = (255, 0, 0) # Red
b = (0, 0, 255) # Blue
b = (0, 0, 0) # Black

class Emoji:
  def __init__(self, order):
    if order == 1:
        self.image = [
            g, g, g, g, g, g, g, g,
            g, g, g, g, g, g, g, g,
            g, b, b, g, g, b, b, g,
            g, b, b, g, g, b, b, g,
            g, g, g, b, b, g, g, g,
            g, g, b, b, b, b, g, g,
            g, g, b, b, b, b, g, g,
            g, g, b, g, g, b, g, g
        ]
    elif order == 2:
        self.image = [
            r, r, r, r, r, r, r, r,
            g, g, g, g, g, g, g, g,
            g, b, b, g, g, b, b, g,
            g, b, b, g, g, b, b, g,
            g, g, g, b, b, g, g, g,
            g, g, b, b, b, b, g, g,
            g, g, b, b, b, b, g, g,
            g, g, b, g, g, b, g, g
        ]
    else:
        self.image = [
            b, b, b, b, b, b, b, b,
            g, g, g, g, g, g, g, g,
            g, b, b, g, g, b, b, g,
            g, b, b, g, g, b, b, g,
            g, g, g, b, b, g, g, g,
            g, g, b, b, b, b, g, g,
            g, g, b, b, b, b, g, g,
            g, g, b, g, g, b, g, g
        ]

  def displayEmoji(self):
    sense.set_pixels(self.image)

emojis = [Emoji(1), Emoji(2), Emoji(3)]

while True:
    for emoji in emojis:
        emoji.displayEmoji()
        sleep(3)

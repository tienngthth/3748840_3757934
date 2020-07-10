from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Define some colours
lo = (255, 165, 0) # Light Orange
br = (165, 42, 42) # Brown
db = (0, 0, 255) # Dark Blue
lb = (0, 102, 255) # Light Blue
bl = (0, 0, 0) # Black
cr = (255, 255, 179) # Cream

class Emoji:
  def __init__(self, order):
    if order == 1:
        self.image = [
            bl, lo, bl, bl, bl, bl, br, bl,
            bl, lo, br, bl, bl, br, cr, bl,
            bl, lo, lo, br, lb, cr, cr, bl,
            lb, lb, lo, lb, lo, lb, lo, bl,
            lo, bl, lo, lo, bl, lo, lo, bl,
            lo, bl, lo, lo, bl, lo, lo, lo,
            br, lo, cr, lo, lo, lo, lo, bl,
            bl, br, bl, lo, lo, br, bl, bl
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
            bl, bl, bl, bl, bl, bl, bl, bl,
            g, g, g, g, g, g, g, g,
            g, b, b, g, g, b, b, g,
            g, b, b, g, g, b, b, g,
            g, g, g, b, b, g, g, g,
            g, g, b, b, b, b, g, g,
            g, g, b, b, b, b, g, g,
            g, g, b, g, g, b, g, g
        ]

  def display(self):
    sense.set_pixels(self.image)

# emojis = [Emoji(1), Emoji(2), Emoji(3)]
emoji = Emoji(1)
emoji.display()

# while True:
#     for emoji in emojis:
#         emoji.display()
#         sleep(3)

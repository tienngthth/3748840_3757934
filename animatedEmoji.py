from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Define some colors
whi = (255, 255, 255)
bla = (0, 0, 0)
red = (255, 0, 0)
ora = (255, 165, 0)
yel = (255, 255, 0)
gre = (0, 255, 0)
blu = (0, 0, 255)
vio = (238, 130, 238)
pur = (255, 51, 255)
bro = (165, 42, 42)
dpu = (102, 0, 102)
cre = (255, 255, 153)

rainbow_mouth_pixels_1 = [
    bla, yel, yel, yel, yel, yel, yel, bla,
    yel, whi, bla, yel, yel, whi, bla, yel,
    yel, bla, bla, yel, yel, bla, bla, yel,
    yel, yel, yel, yel, yel, yel, yel, yel,
    bla, bla, bla, bla, bla, bla, bla, bla,
    red, ora, yel, gre, blu, vio, pur, dpu,
    bla, ora, yel, gre, blu, vio, pur, bla,
    bla, bla, yel, gre, blu, vio, bla, bla,
]

rainbow_mouth_pixels_2 = [
    bla, yel, yel, yel, yel, yel, yel, bla,
    yel, whi, bla, yel, yel, whi, bla, yel,
    yel, bla, bla, yel, yel, bla, bla, yel,
    yel, yel, yel, yel, yel, yel, yel, yel,
    bla, bla, bla, bla, bla, bla, bla, bla,
    dpu, red, ora, yel, gre, blu, vio, pur,
    bla, red, ora, yel, gre, blu, vio, bla,
    bla, bla, ora, yel, gre, blu, bla, bla,  
]

rainbow_mouth_pixels_3 = [
    bla, yel, yel, yel, yel, yel, yel, bla,
    yel, whi, bla, yel, yel, whi, bla, yel,
    yel, bla, bla, yel, yel, bla, bla, yel,
    yel, yel, yel, yel, yel, yel, yel, yel,
    bla, bla, bla, bla, bla, bla, bla, bla,
    pur, dpu, red, ora, yel, gre, blu, vio,
    bla, dpu, red, ora, yel, gre, blu, bla,
    bla, bla, red, ora, yel, gre, bla, bla,  
]

rainbow_mouth_pixels_4 = [
    bla, yel, yel, yel, yel, yel, yel, bla,
    yel, whi, bla, yel, yel, whi, bla, yel,
    yel, bla, bla, yel, yel, bla, bla, yel,
    yel, yel, yel, yel, yel, yel, yel, yel,
    bla, bla, bla, bla, bla, bla, bla, bla,
    vio, pur, dpu, red, ora, yel, gre, blu,
    bla, pur, dpu, red, ora, yel, gre, bla,
    bla, bla, dpu, red, ora, yel, bla, bla,
]

rainbow_mouth_pixels = (
  rainbow_mouth_pixels_1, rainbow_mouth_pixels_2, 
  rainbow_mouth_pixels_3, rainbow_mouth_pixels_4
)

eyes_mouth_pixels_1 = [
    bla, bla, blu, blu, blu, blu, bla, bla,
    bla, blu, blu, blu, blu, blu, blu, bla,
    red, whi, whi, whi, whi, whi, whi, red,
    red, whi, pur, whi, whi, pur, whi, red,
    red, whi, whi, whi, whi, whi, whi, red,
    bla, blu, blu, blu, blu, blu, blu, bla,
    bla, bla, blu, blu, blu, blu, bla, bla,
    bla, bla, blu, blu, blu, blu, bla, bla,
]

eyes_mouth_pixels_2 = [
    bla, bla, blu, blu, blu, blu, bla, bla,
    bla, blu, blu, blu, blu, blu, blu, bla,
    red, whi, whi, whi, whi, whi, whi, red,
    red, pur, whi, whi, pur, whi, whi, red,
    red, whi, whi, whi, whi, whi, whi, red,
    bla, blu, blu, blu, blu, blu, blu, bla,
    bla, bla, blu, whi, whi, blu, bla, bla,
    bla, bla, blu, blu, blu, blu, bla, bla,
]

eyes_mouth_pixels_3 = [
    bla, bla, blu, blu, blu, blu, bla, bla,
    bla, blu, blu, blu, blu, blu, blu, bla,
    red, whi, whi, whi, whi, whi, whi, red,
    red, whi, pur, whi, whi, pur, whi, red,
    red, whi, whi, whi, whi, whi, whi, red,
    bla, blu, blu, blu, blu, blu, blu, bla,
    bla, bla, blu, whi, whi, blu, bla, bla,
    bla, bla, blu, blu, blu, blu, bla, bla,
]

eyes_mouth_pixels_4 = [
    bla, bla, blu, blu, blu, blu, bla, bla,
    bla, blu, blu, blu, blu, blu, blu, bla,
    red, whi, whi, whi, whi, whi, whi, red,
    red, whi, whi, pur, whi, whi, pur, red,
    red, whi, whi, whi, whi, whi, whi, red,
    bla, blu, blu, blu, blu, blu, blu, bla,
    bla, bla, blu, whi, whi, blu, bla, bla,
    bla, bla, blu, blu, blu, blu, bla, bla,
]

eyes_mouth_pixels = (
  eyes_mouth_pixels_1, eyes_mouth_pixels_2, 
  eyes_mouth_pixels_3, eyes_mouth_pixels_4
)

cat_pixels_1 = [
    cre, bla, bla, bla, cre, bla, bla, bla,
    ora, ora, ora, ora, ora, bla, bla, bla,
    ora, bla, ora, bla, ora, bla, ora, ora,
    ora, ora, cre, ora, ora, bla, bla, yel,
    bla, ora, ora, ora, bla, bla, ora, bla,
    bla, yel, yel, yel, bla, bla, bla, yel,
    bla, ora, ora, ora, ora, ora, ora, bla,
    bla, ora, ora, bla, bla, ora, ora, bla,
]

cat_pixels_2 = [
    cre, bla, bla, bla, cre, bla, bla, bla,
    ora, ora, ora, ora, ora, bla, bla, ora,
    ora, bla, ora, bla, ora, bla, ora, ora,
    ora, ora, cre, ora, ora, bla, yel, bla,
    bla, ora, ora, ora, bla, bla, bla, ora,
    bla, yel, yel, yel, bla, bla, yel, bla,
    bla, ora, ora, ora, ora, ora, ora, bla,
    bla, ora, ora, bla, bla, ora, ora, bla,
]

cat_pixels_3 = [
    cre, bla, bla, bla, cre, bla, bla, bla,
    ora, ora, ora, ora, ora, bla, bla, bla,
    ora, bla, ora, bla, ora, bla, ora, ora,
    ora, ora, cre, ora, ora, bla, yel, bla,
    bla, ora, ora, ora, bla, bla, bla, ora,
    bla, yel, yel, yel, bla, bla, yel, bla,
    bla, ora, ora, ora, ora, ora, ora, bla,
    bla, ora, ora, bla, bla, ora, ora, bla,
]

cat_pixels_4 = [
    cre, bla, bla, bla, cre, bla, bla, bla,
    ora, ora, ora, ora, ora, bla, ora, bla,
    ora, bla, ora, bla, ora, bla, ora, ora,
    ora, ora, cre, ora, ora, bla, bla, yel,
    bla, ora, ora, ora, bla, bla, ora, bla,
    bla, yel, yel, yel, bla, bla, bla, yel,
    bla, ora, ora, ora, ora, ora, ora, bla,
    bla, ora, ora, bla, bla, ora, ora, bla,
]

cat_pixels = (
    cat_pixels_1, cat_pixels_2, 
    cat_pixels_3, cat_pixels_4
)

class Emoji:
    def __init__(self, images):
        self.images = images
    
    def display(self):
        count = 0
        while count < 10:
            sense.set_pixels(self.images[count % 4])
            sleep(0.3)
            count += 1
    
emojis = [Emoji(rainbow_mouth_pixels), Emoji(eyes_mouth_pixels), Emoji(cat_pixels)]

while True:
    for emoji in emojis:
        emoji.display()

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Define some colors
whi = (255, 255, 255)
bla = (0, 0, 0)
red = (255, 0, 0)
ora = (255, 165, 0)
yel = (255, 255, 0)
gre = (0, 77, 0)
blu = (102, 153, 255)
vio = (238, 130, 238)
pur = (255, 51, 255)
bro = (102, 102, 51)
dpu = (102, 0, 102)
cre = (255, 255, 153)
gol = (255, 232, 102)
gra = (102, 51, 0)

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

sword_pixels_1 = [
    bla, gre, gre, gre, gre, bla, blu, bla,
    bla, gre, gre, gre, gre, bla, blu, bla,
    bla, gol, dpu, gol, dpu, bla, blu, bla,
    bla, gol, gol, gol, gol, bla, blu, bla,
    bro, bro, gra, gra, gra, blu, blu, blu,
    bro, bro, gra, gra, gra, gol, gol, bla,
    bro, bro, gra, gra, gra, bla, blu, bla,
    bla, dpu, bla, bla, dpu, bla, bla, bla,
]

sword_pixels_2 = [
    bla, gre, gre, gre, gre, bla, blu, bla,
    bla, gre, gre, gre, gre, bla, blu, bla,
    bla, gol, dpu, gol, dpu, bla, blu, bla,
    bla, gol, gol, gol, gol, blu, blu, blu,
    bro, bro, gra, gra, gra, bla, gol, bla,
    bro, bro, gra, gra, gra, gol, blu, bla,
    bro, bro, gra, gra, gra, bla, bla, bla,
    bla, dpu, bla, bla, dpu, bla, bla, bla,
]

sword_pixels_3 = [
    bla, gre, gre, gre, gre, bla, blu, bla,
    bla, gre, gre, gre, gre, bla, blu, bla,
    bla, gol, dpu, gol, dpu, bla, blu, bla,
    bla, gol, gol, gol, gol, bla, blu, bla,
    bro, bro, gra, gra, gra, blu, blu, blu,
    bro, bro, gra, gra, gra, gol, gol, bla,
    bro, bro, gra, gra, gra, bla, blu, bla,
    bla, dpu, bla, bla, dpu, bla, bla, bla,
]

sword_pixels_4 = [
    bla, gre, gre, gre, gre, bla, blu, bla,
    bla, gre, gre, gre, gre, bla, blu, bla,
    bla, gol, dpu, gol, dpu, bla, blu, bla,
    bla, gol, gol, gol, gol, blu, blu, blu,
    bro, bro, gra, gra, gra, bla, gol, bla,
    bro, bro, gra, gra, gra, gol, blu, bla,
    bro, bro, gra, gra, gra, bla, bla, bla,
    bla, dpu, bla, bla, dpu, bla, bla, bla,
]

sword_pixels = (
  sword_pixels_1, sword_pixels_2, 
  sword_pixels_3, sword_pixels_4
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

def main():
    global sense
    sense.low_light = True
    emojis = [Emoji(rainbow_mouth_pixels), Emoji(sword_pixels), Emoji(cat_pixels)]
    while True:
        for emoji in emojis:
            emoji.display()

main()

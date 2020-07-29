from random import randint
from .senseHat import bla, red, whi, PiSenseHat

class Dice:
    dice_value = None
    dice_one = [
        bla, bla, bla, bla, bla, bla, bla, bla,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, whi, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
    ]
    dice_two = [
        bla, bla, bla, bla, bla, bla, bla, bla,
        bla, red, red, red, red, red, red, red,
        bla, red, whi, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, whi, red,
        bla, red, red, red, red, red, red, red,
    ]
    dice_three = [
        bla, bla, bla, bla, bla, bla, bla, bla,
        bla, red, red, red, red, red, red, red,
        bla, red, whi, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, whi, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, whi, red,
        bla, red, red, red, red, red, red, red,
    ]
    dice_four = [
        bla, bla, bla, bla, bla, bla, bla, bla,
        bla, red, red, red, red, red, red, red,
        bla, red, whi, red, red, red, whi, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, whi, red, red, red, whi, red,
        bla, red, red, red, red, red, red, red,
    ]
    dice_five = [
        bla, bla, bla, bla, bla, bla, bla, bla,
        bla, red, red, red, red, red, red, red,
        bla, red, whi, red, red, red, whi, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, whi, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, whi, red, red, red, whi, red,
        bla, red, red, red, red, red, red, red,
    ]
    dice_six = [
        bla, bla, bla, bla, bla, bla, bla, bla,
        bla, red, red, red, red, red, red, red,
        bla, red, whi, red, whi, red, whi, red,
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, whi, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, whi, red, whi, red, whi, red,
        bla, red, red, red, red, red, red, red,
    ]
    dice_pixels = (dice_one, dice_two, dice_three, dice_four, dice_five, dice_six)

    @staticmethod
    def dice_turn():
        dice_value = Dice.roll_dice()
        Dice.display()
        return dice_value

    @staticmethod
    def roll_dice():
        #detect (key stick -> motion -> stop)
        return randint(1, 6)

    @staticmethod
    def display():
        PiSenseHat.display_image_duration(Dice.dice_pixels[Dice.dice_value - 1], 0.3)

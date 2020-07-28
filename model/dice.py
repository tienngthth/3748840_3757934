from random import randint
from senseHat import bla, red, whi, PiSenseHat
import time

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
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, whi, red, whi, red, whi, red,
        bla, red, red, red, red, red, red, red,
    ]
    dice_pixels = (dice_one, dice_two, dice_three, dice_four, dice_five, dice_six)
    threshold = 0.75
    speed_change = 0.25
    speed = 0.01
    myDict = None
    oldDict = None

    @staticmethod
    def compare_dicts(firstDict,secondDict):
        diceDiff = 0.0
        for key, value in firstDict.items():
            diceDiff += abs(firstDict.get(key) - secondDict.get(key))
        return diceDiff

    @staticmethod
    def cal_speed_change():
        Dice.speed = Dice.speed_change/Dice.compare_dicts(Dice.myDict, Dice.oldDict)

    @staticmethod
    def role_dice():
        Dice.myDict = PiSenseHat.get_accelerometer()
        Dice.oldDict = PiSenseHat.get_accelerometer()
        while(Dice.compare_dicts(Dice.myDict, Dice.oldDict) < Dice.threshold):
            print("not shaking")
            Dice.oldDict = Dice.myDict
            time.sleep(1)
            Dice.myDict = PiSenseHat.get_accelerometer()

        while(Dice.compare_dicts(Dice.myDict, Dice.oldDict) > Dice.threshold):
            print("shaking")
            Dice.oldDict = Dice.myDict
            time.sleep(Dice.speed)
            Dice.myDict = PiSenseHat.get_accelerometer()
            Dice.dice_turn(Dice.cal_speed_change())
        
        print("done")
        print(Dice.dice_value)
        return Dice.dice_value

    @staticmethod
    def dice_turn(time_change):
        Dice.dice_value = Dice.roll_dice()
        Dice.display(time_change)
        print(time_change)
        return Dice.dice_value

    @staticmethod
    def roll_dice():
        #detect (key stick -> motion -> stop)
        return randint(1, 6)

    @staticmethod
    def display(time_change):
        PiSenseHat.display_image_duration(Dice.dice_pixels[Dice.dice_value - 1],time_change)

Dice.role_dice()

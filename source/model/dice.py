import time
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
        bla, red, red, red, red, red, red, red,
        bla, red, red, red, red, red, red, red,
        bla, red, whi, red, whi, red, whi, red,
        bla, red, red, red, red, red, red, red,
    ]
    dice_pixels = (dice_one, dice_two, dice_three, dice_four, dice_five, dice_six)
    shaking_threshold = 0.2
    speed_change = 0.25
    speed = None
    current_reading = None
    old_reading = None

    @staticmethod
    def roll_dice():
        Dice.current_reading = PiSenseHat.get_accelerometer()
        Dice.old_reading = Dice.current_reading
        Dice.speed = 0.01
        Dice.wait_for_shake()
        Dice.detect_shake()
        return Dice.dice_value

    @staticmethod
    def wait_for_shake():
        while(Dice.compare_reading(Dice.current_reading, Dice.old_reading) < Dice.shaking_threshold):
            print("not shaking")
            Dice.old_reading = Dice.current_reading
            time.sleep(0.5)
            Dice.current_reading = PiSenseHat.get_accelerometer()

    @staticmethod
    def detect_shake():
        while(Dice.compare_reading(Dice.current_reading, Dice.old_reading) > Dice.shaking_threshold):
            print("shaking")
            Dice.old_reading = Dice.current_reading
            time.sleep(Dice.speed)
            Dice.current_reading = PiSenseHat.get_accelerometer()
            Dice.display_dice()
        print("done")
        print(Dice.dice_value)

    @staticmethod
    def compare_reading(first_reading, second_reading):
        dice_diff = 0.0
        for key, value in first_reading.items():
            dice_diff += abs(first_reading.get(key) - second_reading.get(key))
        return dice_diff

    @staticmethod
    def display_dice():
        Dice.dice_value = randint(1, 6)
        Dice.display()

    @staticmethod
    def display():
        Dice.cal_speed_change()
        PiSenseHat.display_image_duration(Dice.dice_pixels[Dice.dice_value - 1])
    
    @staticmethod
    def cal_speed_change():
        Dice.speed = Dice.speed_change/Dice.compare_reading(Dice.current_reading, Dice.old_reading)


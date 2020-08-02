#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from model.senseHat import PiSenseHat
from model.dice import Dice

def roll_dice():
    Dice.roll_dice()

if __name__ == "__main__":
    roll_dice()

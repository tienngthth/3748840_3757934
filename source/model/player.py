from time import sleep
from .score import Score
from .dice import Dice
from .senseHat import PiSenseHat, vio
from .dice import Dice

"""
Class Player is to create new player for game.py. 
Class Player is used to control score and simulate a player turn.
"""
class Player:
    def __init__(self, player_name, target_score = 30):
        self.__score = Score(target_score)
        self.__dice_value = None
        self.__name = player_name
        self.__winner = False

    #Simulate a player turn
    def play(self):
        self.roll_dice()
        self.__update_score()
        return self.__winner

    #Simulate Player roll a dice
    def roll_dice(self):
        PiSenseHat.show_message("Player", vio, 0.05)
        PiSenseHat.show_letter(self.__name, vio)
        PiSenseHat.detect_stick()
        while not PiSenseHat.detect_stick():
            pass
        self.__dice_value = Dice.roll_dice()
        sleep(2)
        return self.__dice_value

    #Update player score
    def __update_score(self):
        if self.__score.update_score(self.__dice_value):
            self.__winner = True
    
    #Getter and setter
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score.get_score()

    def get_dice_value(self):
        return self.__dice_value    


    
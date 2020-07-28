from time import sleep
from .score import Score
from .dice import Dice
from .senseHat import PiSenseHat, blu
from .dice import Dice

class Player:
    def __init__(self, player_name, target_score = 30):
        self.__score = Score(target_score)
        self.__dice_value = None
        self.__name = player_name
        self.__winner = False

    def play(self):
        self.roll_dice()
        self.__update_score()
        return self.__winner

    def roll_dice(self):
        PiSenseHat.show_letter(self.__name)
        PiSenseHat.detect_stick()
        while not PiSenseHat.detect_stick():
            pass
        self.__dice_value = Dice.roll_dice()
        sleep(2)
        return self.__dice_value

    def __update_score(self):
        if self.__score.update_score(self.__dice_value):
            self.__winner = True
            PiSenseHat.show_message("Congratz P" + self.__name)
        else:
            PiSenseHat.show_message("P" + self.__name + ": " + str(self.__score.get_score()), blu, 0.045)

    def get_name(self):
        return self.__name

    def get_dice_value(self):
        return self.__dice_value    


    
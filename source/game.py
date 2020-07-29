from model.player import Player
from model.dice import Dice
from model.senseHat import PiSenseHat

def find_first_player(player_1, player_2):
    PiSenseHat.show_message("Welcome to the game ~ First roll to find first player")
    while player_1.roll_dice() == player_2.roll_dice():
        PiSenseHat.show_message("A tie! ~ One more time")
    if player_2.get_dice_value < player_2.get_dice_value:
        return (player_2, player_1)
    
def play_game(players_order):
    while True:
        for player in players_order:
            if player.play():
                end_record()
                return player.get_name()

def end_game():
                
def main():
    player_1 = Player("1")
    player_2 = Player("2")
    players_order = find_first_player(player_1, player_2)
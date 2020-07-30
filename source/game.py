import datetime
from model.player import Player
from model.dice import Dice
from model.senseHat import PiSenseHat, ora
from model.util import Util
from electronicDice import roll_dice

def find_first_player(player_1, player_2):
    PiSenseHat.show_message("Welcome ~ First roll to find first player")
    while player_1.roll_dice() == player_2.roll_dice():
        PiSenseHat.show_message("A tie! ~ One more time")
    if player_2.get_dice_value() > player_1.get_dice_value():
        players_order = (player_2, player_1)
        PiSenseHat.show_message("P2 first!")
    else:
        players_order = (player_1, player_2)
        PiSenseHat.show_message("P1 first!")
    return players_order
    
def play_game(players_order):
    while True:
        for player in players_order:
            if player.play():
                return "Player " + player.get_name() + "wins the game with " +  str(player.get_score()) + " scores"
            else:
                PiSenseHat.show_message("P" + player.get_name() + ": " + str(player.get_score()), blu, 0.06)

def end_game(winning_info):
    PiSenseHat.show_message("Congratz!!!" + winning_info, ora, 0.06)
    record = datetime.datetime.now().replace(microsecond = 0) + ": " + winning_info
    File.write_csv(Util.get_file_name("winner"), record)

def main():
    global players_order
    player_1 = Player("1")
    player_2 = Player("2")
    end_game(play_game(find_first_player(player_1, player_2)))

if __name__ == "__main__":
    main()

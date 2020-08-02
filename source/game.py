#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
from model.player import Player
from model.senseHat import PiSenseHat, ora, blu
from model.util import Util
from model.fileHandle import File
from electronicDice import roll_dice

# Find first player to start the game 
def find_first_player(player_1, player_2):
    PiSenseHat.show_message("Welcome to THE DICE ~")
    PiSenseHat.show_message("Please press joy stick to start every shaking ~")
    PiSenseHat.show_message("First roll to find first player ~")
    # Retry until a player has the first higher roll
    while player_1.roll_dice() == player_2.roll_dice():
        PiSenseHat.show_message("A tie! ~ One more time ~")
    # Check to see which player has first higher roll to play first
    if player_2.get_dice_value() > player_1.get_dice_value():
        players_order = (player_2, player_1)
        PiSenseHat.show_message("P2 first!")
    else:
        players_order = (player_1, player_2)
        PiSenseHat.show_message("P1 first!")
    return players_order
    
# Play game until winner is found
def play_game(players_order):
    while True:
        # Players roll dice one by one to get points
        for player in players_order:
            if player.play():
                # Game ends when finding a winner with 30 points 
                return "Player " + player.get_name() + " wins with " +  str(player.get_score()) + " points"
            else:
                # Display updated points message to Sense HAT
                PiSenseHat.show_message("P" + player.get_name() + " has " + str(player.get_score()) + " points", blu, 0.06)

# Announce winner in Sense HAT and save the game record
def end_game(winning_info):
    # Display winner annoucement to Sense HAT
    PiSenseHat.show_message("Congratz!! " + winning_info, ora, 0.06)
    # Ask for user input winner file name and record the winner points with time to the appropriate file
    record = str(datetime.datetime.now().replace(microsecond = 0)) + ": " + winning_info + "\n"
    message = "Input game winners report file name. Default name is winner.csv"
    File.write_csv(Util.get_file_name("winner", ".csv", message), record)

def start_game():
    player_1 = Player("1")
    player_2 = Player("2")
    end_game(play_game(find_first_player(player_1, player_2)))

if __name__ == "__main__":
    start_game()

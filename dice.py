import random
from players import Players
from board import Board
from turn import Turn

class Dice:

    def player_roll(self):
        players = Players()
        board = Board()
        turn = Turn()
        
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total = dice1 + dice2 
        self.roll_history.append(total)

        print(f"Roll: {total}, Dice 1: {dice1}, Dice 2: {dice2}\n")
        print(f"{players[0]} moved {total} spaces and landed on {board.monopoly[str()]}\n")
    

    def bot_roll(self):
        players = Players()
        board = Board()
        bot_turn = Turn()

        bot_roll_history = [0]
        bot_total = 0
        bot_dice1 = random.randint(1,6)
        bot_dice2 = random.randint(1,6)

        bot_total = bot_dice1 + bot_dice2 
        bot_roll_history.append(bot_total)
        self.bot_current += bot_total

        print(f"Roll: {bot_total}, Dice 1: {bot_dice1}, Dice 2: {bot_dice2}\n")
        print(f"{players[0]} moved {bot_total} spaces and landed on {board.monopoly[str()]}\n")
    

    

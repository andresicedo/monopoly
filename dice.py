import random
from position import Position
from bot_position import Bot_Position
from players import Players
from board import Board
from bank import Bank
from purchase import Purchase

class Dice:
    def __init__(self, players):
        self.players = players.players

    def player_roll(self):
        position = Position()
        players = Players()
        board = Board()
        bank = Bank()
        purchase = Purchase()
        dice1 = 0
        dice2 = 0
        total = 0
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        total = dice1 + dice2 

        position.location += total
        position.position(location=position.location)
        print(f"Roll: {total}, Dice 1: {dice1}, Dice 2: {dice2}\n")
        print(f"{self.players[0]} moved {total} spaces and landed on {board.monopoly[str(position.location + total)]}\n")
        for property in bank.properties.keys():
            if board.monopoly[str(position.location)] == property:
                purchase.purchase()

    def bot_roll(self):
        bot_position = Bot_Position()
        players = Players()
        board = Board()
        bot_dice1 = 0
        bot_dice2 = 0
        bot_total = 0
        bot_dice1 = random.randint(1,6)
        bot_dice2 = random.randint(1,6)

        bot_total = bot_dice1 + bot_dice2 

        bot_position.bot_location += bot_total
        bot_position.bot_position(bot_location=bot_position.bot_location)
        print(f"Roll: {bot_total}, Dice 1: {bot_dice1}, Dice 2: {bot_dice2}\n")
        print(f"{self.players[1]} moved {bot_total} spaces and landed on {board.monopoly[str(bot_position.bot_location + bot_total)]}\n")


    

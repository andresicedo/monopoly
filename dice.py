from bot_position import Bot_position
import random
from players import Players
from board import Board
from turn import Turn
from position import Position

class Dice:
    def player_roll(self, players: Players):
        board = Board()
        turn = Turn()
        position = Position()
        
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total = dice1 + dice2 
        turn.roll_history.append(total)
        position.current(turn)
        print(f"Roll: {total}, Dice 1: {dice1}, Dice 2: {dice2}\n")
        print(f"{players.players[0]} moved {total} spaces and landed on {board.monopoly[str(position.current(turn))]}\n")
        

    def bot_roll(self, players: Players):
        board = Board()
        bot_turn = Turn()
        bot_position = Bot_position()

        bot_dice1 = random.randint(1,6)
        bot_dice2 = random.randint(1,6)
        bot_total = bot_dice1 + bot_dice2 
        
        bot_turn.bot_roll_history.append(bot_total)

        print(f"Roll: {bot_total}, Dice 1: {bot_dice1}, Dice 2: {bot_dice2}\n")
        print(f"{players.players[1]} moved {bot_total} spaces and landed on {board.monopoly[str(bot_position.bot_current(bot_turn))]}\n")
    

    

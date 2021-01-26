from bot_position import Bot_position
from bot_probability import Bot_probability
from position import Position
from players import Players
from board import Board
from bank import Bank
from assets import Assets
from turn import Turn
class Rent:
    def rent(self, players: Players, turn):
        position = Position()
        board = Board()
        bank = Bank()
        assets = Assets()

        if board.monopoly[str(position.current(turn))] in assets.bot_properties:
            assets.bot_account_balance[0] += 500
            assets.user_account_balance[0] -= 500
            print("You landed on a purchased property!\n")
            print(f"Rent paid to {players.players[1]}: $500\n")

    def bot_rent(self, players: Players, bot_turn):
        position = Position()
        board = Board()
        bank = Bank()
        assets = Assets()
        # bot_turn = Turn()
        bot_position = Bot_position()

        if board.monopoly[str(bot_position.bot_current(bot_turn))] in assets.user_properties:
            assets.bot_account_balance[0] -= 500
            assets.user_account_balance[0] += 500
            print(f"Rent paid to {players.players[0]}: $500\n")
            print(f"Updated Balance for {players.players[1]}: ${assets.bot_account_balance[0]}")
            print(f"Updated Balance for {players.players[0]}: ${assets.user_account_balance[0]}")
from bot_position import Bot_position
from bot_probability import Bot_probability
from position import Position
from players import Players
from board import Board
from bank import Bank
from assets import Assets
from turn import Turn

class Purchase:
    def purchase(self, players: Players, turn):
        position = Position()
        board = Board()
        bank = Bank()
        assets = Assets()
        # turn = Turn()

        if board.monopoly[str(position.current(turn))] in bank.properties:
            user_input = input(f"Would you like to purhcase {board.monopoly[str(position.current(turn))]} for ${bank.properties[board.monopoly[str(position.current(turn))]]}?\n1. Yes\n2. No")
            if user_input == "1":
                if assets.bot_account_balance > bank.properties[board.monopoly[str(position.current(turn))]]:
                    user_input = input(f"Are you sure you want to complete the purchase of {board.monopoly[str(position.current(turn))]}?\n1. Yes\n2. No\nENTER HERE: ")
                    if user_input == "1":
                        print("Accessing your BANK ACCOUNT...\n")
                        print(f"BALANCE: {players.players[0]}, your current account balance is ${assets.bot_account_balance}\n")
                        assets.bot_account_balance -= bank.properties[board.monopoly[str(position.current(turn))]]
                        assets.user_properties.append(board.monopoly[str(position.current(turn))])
                        del bank.properties[board.monopoly[str(position.current(turn))]]
                        print(f"Your updated balance is ${assets.bot_account_balance}")
                        print(f"Current Properties: {assets.user_properties}")
        elif board.monopoly[str(position.current(turn))] not in bank.properties:
            print("You landed on a purchased property!\n")
            print(f"Rent paid to {players.players[1]}: $500")
            assets.user_account_balance += 500
            assets.bot_account_balance

    def bot_purchase(self, players: Players):
        position = Position()
        board = Board()
        bank = Bank()
        assets = Assets()
        bot_turn = Turn()
        bot_probability = Bot_probability()
        bot_position = Bot_position()

        
        if board.monopoly[str(bot_position.bot_current(bot_turn))] in bank.properties:
            user_input = bot_probability.probability()
            if user_input == "1":
                if assets.bot_account_balance > bank.properties[board.monopoly[str(bot_position.bot_current(bot_turn))]]:
                    user_input = input(f"Are you sure you want to complete the purchase of {board.monopoly[str(position.current(turn))]}?\n1. Yes\n2. No\nENTER HERE: ")
                    if user_input == "1":
                        assets.bot_account_balance -= bank.properties[board.monopoly[str(bot_position.bot_current(bot_turn))]]
                        assets.user_properties.append(board.monopoly[str(bot_position.bot_current(bot_turn))])
                        del bank.properties[board.monopoly[str(bot_position.bot_current(bot_turn))]]
                        print(f"{players.players[1]} Properties: {assets.user_properties}")
        elif board.monopoly[str(bot_position.bot_current(bot_turn))] not in bank.properties:
            print("You landed on a purchased property!\n")
            print(f"Rent paid to {players.players[0]}: $500")
            

        

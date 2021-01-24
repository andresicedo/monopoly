from position import Position
from bot_position import Bot_Position
from players import Players
from board import Board
from bank import Bank
from assets import Assets
class Purchase:
    def purchase(self):
        position = Position()
        players = Players()
        board = Board()
        bank = Bank()
        assets = Assets()
        user_input = input(f"Would you like to purhcase {board.monopoly[str(position.location)]} for ${bank.properties[board.monopoly[str(position.location.lower())]]}?\n1. Yes\n2. No")
        if user_input == "1":
            print("Accessing your BANK ACCOUNT...\n")
            print(f"BALANCE: {self.players[0]}, your current account balance is ${assets.user_account_balance}\n")
            if assets.user_account_balance > bank.properties[board.monopoly[str(position.location.lower())]]:
                user_input = input(f"Are you sure you want to complete the purchase of {board.monopoly[str(position.location)]}?\n1. Yes\n2. No\nENTER HERE: ")
                if user_input == "1":
                    assets.user_account_balance -= bank.properties[board.monopoly[str(position.location.lower())]]
                    assets.user_properties.append(board.monopoly[str(position.location)])
                    del bank.properties[board.monopoly[str(position.location.lower())]]
                    print(f"Your updated balance is ${assets.user_account_balance}")
                    print(f"Current Properties: {assets.user_properties}")

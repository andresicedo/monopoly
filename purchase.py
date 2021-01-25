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
        if board.monopoly[str(self.current_position)] in bank.properties:
            user_input = input(f"Would you like to purhcase {board.monopoly[str(self.current_position)]} for ${bank.properties[board.monopoly[str(self.current_position)]]}?\n1. Yes\n2. No")
            if user_input == "1":
                if assets.user_account_balance > bank.properties[board.monopoly[str(self.current_position)]]:
                    user_input = input(f"Are you sure you want to complete the purchase of {board.monopoly[str(position.position())]}?\n1. Yes\n2. No\nENTER HERE: ")
                    if user_input == "1":
                        print("Accessing your BANK ACCOUNT...\n")
                        print(f"BALANCE: {self.players[0]}, your current account balance is ${assets.user_account_balance}\n")
                        assets.user_account_balance -= bank.properties[board.monopoly[str(self.current_position)]]
                        assets.user_properties.append(board.monopoly[str(self.current_position)])
                        del bank.properties[board.monopoly[str(self.current_position)]]
                        print(f"Your updated balance is ${assets.user_account_balance}")
                        print(f"Current Properties: {assets.user_properties}")
        elif board.monopoly[str(self.current_position)] not in bank.properties:
            print("No purchase is available for this location.\n")
        

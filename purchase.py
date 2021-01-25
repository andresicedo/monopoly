from position import Position
from players import Players
from board import Board
from bank import Bank
from assets import Assets
from turn import Turn

class Purchase:
    def purchase(self, players: Players):
        position = Position()
        board = Board()
        bank = Bank()
        assets = Assets()
        turn = Turn()

        if board.monopoly[str(position.current(turn))] in bank.properties:
            user_input = input(f"Would you like to purhcase {board.monopoly[str(position.current(turn))]} for ${bank.properties[board.monopoly[str(position.current(turn))]]}?\n1. Yes\n2. No")
            if user_input == "1":
                if assets.user_account_balance > bank.properties[board.monopoly[str(position.current(turn))]]:
                    user_input = input(f"Are you sure you want to complete the purchase of {board.monopoly[str(position.current(turn))]}?\n1. Yes\n2. No\nENTER HERE: ")
                    if user_input == "1":
                        print("Accessing your BANK ACCOUNT...\n")
                        print(f"BALANCE: {players.players[0]}, your current account balance is ${assets.user_account_balance}\n")
                        assets.user_account_balance -= bank.properties[board.monopoly[str(position.current(turn))]]
                        assets.user_properties.append(board.monopoly[str(position.current(turn))])
                        del bank.properties[board.monopoly[str(position.current(turn))]]
                        print(f"Your updated balance is ${assets.user_account_balance}")
                        print(f"Current Properties: {assets.user_properties}")
        elif board.monopoly[str(position.current(turn))] not in bank.properties:
            print("No purchase is available for this location.\n")
        

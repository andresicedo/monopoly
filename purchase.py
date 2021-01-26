from bot_position import Bot_position
from bot_probability import Bot_probability
from position import Position
from players import Players
from board import Board
from bank import Bank
from assets import Assets
from turn import Turn
from rent import Rent

class Purchase:
    def purchase(self, players: Players, turn):
        position = Position()
        board = Board()
        bank = Bank()
        assets = Assets()
        rent = Rent()
        # turn = Turn()
        rent.rent(players, turn)
        if board.monopoly[str(position.current(turn))] in bank.properties:
            user_input = input(f"Would you like to purhcase {board.monopoly[str(position.current(turn))]} for ${bank.properties[board.monopoly[str(position.current(turn))]]}?\n1. Yes\n2. No\nENTER HERE: ")
            if user_input == "1":
                if assets.bot_account_balance > bank.properties[board.monopoly[str(position.current(turn))]]:
                    user_input = input(f"Are you sure you want to complete the purchase of {board.monopoly[str(position.current(turn))]}?\n1. Yes\n2. No\nENTER HERE: ")
                    if user_input == "1":
                        print("Accessing your BANK ACCOUNT...\n")
                        print(f"BALANCE: {players.players[0]}, your current account balance is ${assets.user_account_balance}\n")
                        assets.bot_account_balance -= int(bank.properties[board.monopoly[str(position.current(turn))]])
                        assets.user_properties.append(board.monopoly[str(position.current(turn))])
                        del bank.properties[board.monopoly[str(position.current(turn))]]
                        print(f"Your updated balance is ${assets.user_account_balance}\n")
                        print(f"Current Properties: {assets.user_properties}\n")
                        print(f"{players.players[1]} will roll next\n")
                else:
                    print("You dont't have enough money to purchase this property.")
                    print(f"{players.players[1]} will roll next\n")
            if user_input == "2":
                print(f"{players.players[1]} will roll next\n")
        
        

    def bot_purchase(self, players: Players, bot_turn):
        position = Position()
        board = Board()
        bank = Bank()
        assets = Assets()
        # bot_turn = Turn()
        bot_probability = Bot_probability()
        bot_position = Bot_position()
        bot_rent = Rent()

        bot_rent.bot_rent(players, bot_turn)
        if board.monopoly[str(bot_position.bot_current(bot_turn))] in bank.properties:
            if assets.bot_account_balance > bank.properties[board.monopoly[str(bot_position.bot_current(bot_turn))]]:
                user_input = bot_probability.probability()
                if user_input == "1":
                    print(f"{players.players[1]} purchased {board.monopoly[str(bot_position.bot_current(bot_turn))]}")
                    assets.bot_account_balance -= bank.properties[board.monopoly[str(bot_position.bot_current(bot_turn))]]
                    assets.bot_properties.append(board.monopoly[str(bot_position.bot_current(bot_turn))])
                    del bank.properties[board.monopoly[str(bot_position.bot_current(bot_turn))]]
                    print(f"{players.players[1]} Properties: {assets.bot_properties}\n")
                    print(f"{players.players[1]} Balance: {assets.bot_account_balance}\n")
                    print(f"{players.players[0]} will roll next\n")
                if user_input == "2":
                    print(f"{players.players[0]} will roll next\n")     
        
            

        

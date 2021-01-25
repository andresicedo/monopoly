from life_locations import Life_locations
from players import Players
from board import Board
from position import Position
from bot_position import Bot_position
from luck_locations import Lucky_locations
from assets import Assets

class Turn:
    def __init__(self):
        self.roll_history = [0]
        self.bot_roll_history = [0]

    def current(self):
        current_position = self.roll_history[-1] + self.roll_history[-2]
        if current_position > 44:
            current_position -= 44
        return current_position

    

    def player_turn(self, players: Players):
        life_locations = Life_locations()
        luck_locations = Lucky_locations()
        board = Board()
        turn = Turn()
        position = Position()
        assets = Assets()

        if board.monopoly[str(self.current())] in life_locations.life:
            print(f"You landed on a 'life happens' location.\nDue to a(n) {board.monopoly[str(self.current())]}\nYou're  is over.")
        if board.monopoly[str(self.current())] in luck_locations.luck:
            print("It's your lucky day, you landed on a 'lucky location'.\n")
            if board.monopoly[str(self.current())] == "GO":
                print("You made a full trip around MONOPOLY 2021!\n$200 was added to your bank account!")
                assets.bot_account_balance += 200
            if board.monopoly[str(self.current())] == "BEGINNERS_LUCK":
                print("It pays to be a beginner!\n$500 was added to your bank account!")
                assets.bot_account_balance += 500
            if board.monopoly[str(self.current())] == "SPEEDING1":
                print("Too fast!\nThe SPEEDING TICKET cost you $200")
                assets.bot_account_balance -= 200
            if board.monopoly[str(self.current())] == "LOTTERY1":
                print("You just won the LOTTERY!\n$1000 was added to your bank account")
                assets.bot_account_balance += 1000
            if board.monopoly[str(self.current())] == "LOTTERY2":
                print("You just won the LOTTERY!\n$1000 was added to your bank account")
                assets.bot_account_balance += 1000
            if board.monopoly[str(self.current())] == "SPEEDING2":
                print("Too fast!\nThe SPEEDING TICKET cost you $300")
                assets.bot_account_balance -= 300
            if board.monopoly[str(self.current())] == "FOR_SALE1":
                print("AUCTION!!!!\nA credit of $300 has been added to your account to use towards your next purchase!")
                assets.bot_account_balance += 300
            if board.monopoly[str(self.current())] == "FOR_SALE2":
                print("AUCTION!!!!\nA credit of $300 has been added to your account to use towards your next purchase!")
                assets.bot_account_balance += 300
            if board.monopoly[str(self.current())] == "FORECLOSURE1":
                print("FORECLOSURE!!!!\nA credit of $100 has been added to your account to use towards your next purchase!")
                assets.bot_account_balance += 100
            if board.monopoly[str(self.current())] == "SPEEDING3":
                print("Too fast!\nThe SPEEDING TICKET cost you $300")
                assets.bot_account_balance -= 300
            if board.monopoly[str(self.current())] == "FORECLOSURE2":
                print("FORECLOSURE!!!!\nA credit of $100 has been added to your account to use towards your next purchase!")
                assets.bot_account_balance += 100
            
            
    # bot_roll_history = [0]
    def bot_current(self):
        bot_current_position = self.bot_roll_history[-1] + self.bot_roll_history[-2]
        if bot_current_position > 44:
            bot_current_position -= 44
        return bot_current_position

    def bot_turn(self, players: Players):
        life_locations = Life_locations()
        luck_locations = Lucky_locations()
        board = Board()
        bot_turn = Turn()
        # bot_position = Position()
        assets = Assets()

        if board.monopoly[str(self.bot_current())] in life_locations.life:
            print(f"{players.players[1]} landed on a 'life happens' location.\nDue to a(n) {board.monopoly[str(self.bot_current())]}\n{players.players[1]}'s turn is over.")
        if board.monopoly[str(self.bot_current())] in luck_locations.luck:
            if board.monopoly[str(self.bot_current())] == "GO":
                print(f"{players.players[1]} + $200")
                assets.bot_account_balance += 200
            if board.monopoly[str(self.bot_current())] == "BEGINNERS_LUCK":
                print(f"{players.players[1]} + $500")
                assets.bot_account_balance += 500
            if board.monopoly[str(self.bot_current())] == "SPEEDING1":
                print(f"{players.players[1]} - $200")
                assets.bot_account_balance -= 200
            if board.monopoly[str(self.bot_current())] == "LOTTERY1":
                print(f"{players.players[1]} + $1000")
                assets.bot_account_balance += 1000
            if board.monopoly[str(self.bot_current())] == "LOTTERY2":
                print(f"{players.players[1]} + $1000")
                assets.bot_account_balance += 1000
            if board.monopoly[str(self.bot_current())] == "SPEEDING2":
                print(f"{players.players[1]} - $300")
                assets.bot_account_balance -= 300
            if board.monopoly[str(self.bot_current())] == "FOR_SALE1":
                print(f"{players.players[1]} + $300")
                assets.bot_account_balance += 300
            if board.monopoly[str(self.bot_current())] == "FOR_SALE2":
                print(f"{players.players[1]} + $300")
                assets.bot_account_balance += 300
            if board.monopoly[str(self.bot_current())] == "FORECLOSURE1":
                print(f"{players.players[1]} + $100")
                assets.bot_account_balance += 100
            if board.monopoly[str(self.bot_current())] == "SPEEDING3":
                print(f"{players.players[1]} - $300")
                assets.bot_account_balance -= 300
            if board.monopoly[str(self.bot_current())] == "FORECLOSURE2":
                print(f"{players.players[1]} + $100")
                assets.bot_account_balance += 100
        #probability
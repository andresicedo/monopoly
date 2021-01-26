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
        
        #board.monopoly[str(self.current())]

        if board.monopoly[str(position.current(self))] in life_locations.life:
            print(f"You landed on a 'LIFE HAPPENS' location.\n\nDue to a(n) {board.monopoly[str(position.current(self))]},\nyour turn is over.\n")
        if board.monopoly[str(position.current(self))] in luck_locations.luck:
            print("It's your lucky day, you landed on a 'lucky location'.\n")
            if board.monopoly[str(position.current(self))] == "GO":
                print("You made a full trip around MONOPOLY 2021!\n$200 was added to your bank account!\n")
                assets.bot_account_balance += 200
            if board.monopoly[str(position.current(self))] == "BEGINNERS_LUCK":
                print("It pays to be a beginner!\n$500 was added to your bank account!\n")
                assets.bot_account_balance += 500
            if board.monopoly[str(position.current(self))] == "SPEEDING1":
                print("Too fast!\nThe SPEEDING TICKET cost you $200\n")
                assets.bot_account_balance -= 200
            if board.monopoly[str(position.current(self))] == "LOTTERY1":
                print("You just won the LOTTERY!\n$1000 was added to your bank account\n")
                assets.bot_account_balance += 1000
            if board.monopoly[str(position.current(self))] == "LOTTERY2":
                print("You just won the LOTTERY!\n$1000 was added to your bank account\n")
                assets.bot_account_balance += 1000
            if board.monopoly[str(position.current(self))] == "SPEEDING2":
                print("Too fast!\nThe SPEEDING TICKET cost you $300\n")
                assets.bot_account_balance -= 300
            if board.monopoly[str(position.current(self))] == "FOR_SALE1":
                print("AUCTION!!!!\nA credit of $300 has been added to your account to use towards your next purchase!\n")
                assets.bot_account_balance += 300
            if board.monopoly[str(position.current(self))] == "FOR_SALE2":
                print("AUCTION!!!!\nA credit of $300 has been added to your account to use towards your next purchase!\n")
                assets.bot_account_balance += 300
            if board.monopoly[str(position.current(self))] == "FORECLOSURE1":
                print("FORECLOSURE!!!!\nA credit of $100 has been added to your account to use towards your next purchase!\n")
                assets.bot_account_balance += 100
            if board.monopoly[str(position.current(self))] == "SPEEDING3":
                print("Too fast!\nThe SPEEDING TICKET cost you $300\n")
                assets.bot_account_balance -= 300
            if board.monopoly[str(position.current(self))] == "FORECLOSURE2":
                print("FORECLOSURE!!!!\nA credit of $100 has been added to your account to use towards your next purchase!\n")
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
        bot_position = Bot_position()
        assets = Assets()
        #board.monopoly[str(self.bot_current())]

        if board.monopoly[str(bot_position.bot_current(self))] in life_locations.life:
            print(f"{players.players[1]} landed on a 'LIFE HAPPPENS' location.\n\nDue to a(n) {board.monopoly[str(bot_position.bot_current(self))]},\n {players.players[1]}'s turn is over.")
        if board.monopoly[str(bot_position.bot_current(self))] in luck_locations.luck:
            if board.monopoly[str(bot_position.bot_current(self))] == "GO":
                print(f"{players.players[1]} + $200\n")
                assets.bot_account_balance += 200
            if board.monopoly[str(bot_position.bot_current(self))] == "BEGINNERS_LUCK":
                print(f"{players.players[1]} + $500\n")
                assets.bot_account_balance += 500
            if board.monopoly[str(bot_position.bot_current(self))] == "SPEEDING1":
                print(f"{players.players[1]} - $200\n")
                assets.bot_account_balance -= 200
            if board.monopoly[str(bot_position.bot_current(self))] == "LOTTERY1":
                print(f"{players.players[1]} + $1000\n")
                assets.bot_account_balance += 1000
            if board.monopoly[str(bot_position.bot_current(self))] == "LOTTERY2":
                print(f"{players.players[1]} + $1000\n")
                assets.bot_account_balance += 1000
            if board.monopoly[str(bot_position.bot_current(self))] == "SPEEDING2":
                print(f"{players.players[1]} - $300\n")
                assets.bot_account_balance -= 300
            if board.monopoly[str(bot_position.bot_current(self))] == "FOR_SALE1":
                print(f"{players.players[1]} + $300\n")
                assets.bot_account_balance += 300
            if board.monopoly[str(bot_position.bot_current(self))] == "FOR_SALE2":
                print(f"{players.players[1]} + $300\n")
                assets.bot_account_balance += 300
            if board.monopoly[str(bot_position.bot_current(self))] == "FORECLOSURE1":
                print(f"{players.players[1]} + $100\n")
                assets.bot_account_balance += 100
            if board.monopoly[str(bot_position.bot_current(self))] == "SPEEDING3":
                print(f"{players.players[1]} - $300\n")
                assets.bot_account_balance -= 300
            if board.monopoly[str(bot_position.bot_current(self))] == "FORECLOSURE2":
                print(f"{players.players[1]} + $100\n")
                assets.bot_account_balance += 100
        #probability
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
    def player_turn(self, players: Players):
        life_locations = Life_locations()
        luck_locations = Lucky_locations()
        board = Board()
        turn = Turn()
        position = Position()
        assets = Assets()

        if board.monopoly[str(position.current(turn))] in life_locations.life:
            print(f"You landed on a 'life happens' location.\nDue to a(n) {board.monopoly[str(position.current(turn))]}\nYou're turn is over.")
        if board.monopoly[str(position.current(turn))] in luck_locations.lucky_location:
            print("It's your lucky day, you landed on a 'lucky location'.\n")
            if board.monopoly[str(position.current(turn))] == "GO":
                print("You made a full trip around MONOPOLY 2021!\n$200 was added to your bank account!")
                assets.user_account_balance += 200
            if board.monopoly[str(position.current(turn))] == "BEGINNERS_LUCK":
                print("It pays to be a beginner!\n$500 was added to your bank account!")
                assets.user_account_balance += 500
            if board.monopoly[str(position.current(turn))] == "SPEEDING1":
                print("Too fast!\nThe SPEEDING TICKET cost you $200")
                assets.user_account_balance -= 200
            if board.monopoly[str(position.current(turn))] == "LOTTERY1":
                print("You just won the LOTTERY!\n$1000 was added to your bank account")
                assets.user_account_balance += 1000
            if board.monopoly[str(position.current(turn))] == "LOTTERY2":
                print("You just won the LOTTERY!\n$1000 was added to your bank account")
                assets.user_account_balance += 1000
            if board.monopoly[str(position.current(turn))] == "SPEEDING2":
                print("Too fast!\nThe SPEEDING TICKET cost you $300")
                assets.user_account_balance -= 300
            if board.monopoly[str(position.current(turn))] == "FOR_SALE1":
                print("AUCTION!!!!\nA credit of $300 has been added to your account to use towards your next purchase!")
                assets.user_account_balance += 300
            if board.monopoly[str(position.current(turn))] == "FOR_SALE2":
                print("AUCTION!!!!\nA credit of $300 has been added to your account to use towards your next purchase!")
                assets.user_account_balance += 300
            if board.monopoly[str(position.current(turn))] == "FORECLOSURE1":
                print("FORECLOSURE!!!!\nA credit of $100 has been added to your account to use towards your next purchase!")
                assets.user_account_balance += 100
            if board.monopoly[str(position.current(turn))] == "SPEEDING3":
                print("Too fast!\nThe SPEEDING TICKET cost you $300")
                assets.user_account_balance -= 300
            if board.monopoly[str(position.current(turn))] == "FORECLOSURE2":
                print("FORECLOSURE!!!!\nA credit of $100 has been added to your account to use towards your next purchase!")
                assets.user_account_balance += 100
            
            
    # bot_roll_history = [0]
    def bot_turn(self):
        pass
        #probability
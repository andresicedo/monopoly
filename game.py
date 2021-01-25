from purchase import Purchase
from dice import Dice
from players import Players
from turn import Turn
from assets import Assets
class Game:
    def menu(self, turn: Turn, players: Players):
        dice = Dice()
        assets = Assets()
        purchase = Purchase()
        print("What would like to do?\n")
        print("1. ENTER GAME\n2. MY ASSETS\n3. LEADERBOARD\n4. QUIT\n")
        user_input = input("ENTER HERE: ")
        if user_input == "1":
            dice.player_roll(players, turn)
            turn.player_turn(players)
            purchase.purchase(players, turn)
            dice.bot_roll(players, turn)
        if user_input =="2":
            print(f"Current Balance: {assets.user_account_balance}")
            print(f"Current Properties: {assets.user_properties}")
        if user_input == "3":
            print("Leaderboard:")
            if assets.user_account_balance > assets.bot_account_balance:
                print(f"First Place: {players.players[0]}")
                print(f"Second Place: {players.players[1]}")
            if assets.user_account_balance < assets.bot_account_balance:
                print(f"First Place: {players.players[1]}")
                print(f"Second Place: {players.players[0]}")
            if assets.user_account_balance == assets.bot_account_balance:
                print("Tie Game!")
                print(f"{players.players[0]}: {assets.user_account_balance}")
                print(f"{players.players[1]}: {assets.bot_account_balance}")
        if user_input == "4":
            Game()==False

        
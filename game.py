from dice import Dice

class Game:
    def menu(self, players):
        dice = Dice(players)
        print("What would like to do?\n")
        print("1. ENTER GAME\n2. MY ASSETS\n3. LEADERBOARD\n4. QUIT\n")
        user_input = input("ENTER HERE: ")
        if user_input == "1":
            dice.player_roll()
            dice.bot_roll()

        
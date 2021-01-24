class Players: 
    def __init__(self):
        self.players = []


    def choose_player(self):
        print("\nWelcome to MONOPOLY 2021!\n")
        print("You will be playing against Monopoly bot, UNCLE SAM!\n")
        user_input = input("Enter your player name: ").upper()
        self.players.append(user_input.upper())
        self.players.append("UNCLE SAM")
        print(f"Welcome {self.players[0]}!\n")
        
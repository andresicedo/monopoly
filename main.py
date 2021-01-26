from game import Game
from players import Players
from turn import Turn
from assets import Assets
def main():
    players = Players()
    game = Game()
    turn = Turn()
    assets = Assets()

    players.choose_player()
    print("\nYou will get the first turn of the game!\nENTER GAME to start!")
    while game:
       game.menu(turn, players)
    if assets.user_account_balance[0] <= 0:
        print("Game Over!")
        print("UNCLE SAM never loses! :)")
        print("Thank you for playing MONOPOLY 2021!")
        quit()
    if assets.bot_account_balance[0] <= 0:
        print("Game Over!")
        print("YOU WIN!!!")
        print("Thank you for playing MONOPOLY 2021!")
        quit()

main()
from game import Game
from players import Players
from dice import Dice
def main():
    players = Players()
    game = Game()


    players.choose_player()
    print("\nYou will get the first turn of the game!\nENTER GAME to start!")
    while game:
       game.menu(players)
        

main()
from game import Game
from players import Players
from turn import Turn
def main():
    players = Players()
    game = Game()
    turn = Turn()

    players.choose_player()
    print("\nYou will get the first turn of the game!\nENTER GAME to start!")
    while game:
       game.menu(turn, players)
        

main()
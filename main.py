# main.py
from game import Game

if __name__ == "__main__":
    # Crea una instancia del juego en modo desarrollador
    game = Game(developer_mode=True)
    # Inicia el juego
    game.start_game()




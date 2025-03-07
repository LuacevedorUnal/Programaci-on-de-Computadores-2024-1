# src/game.py
from board import Board
from dice import Dice
from player import Player

class Game:
    def __init__(self, developer_mode=False):
        # Tablero del juego
        self.board = Board()
        # Dados del juego
        self.dice = Dice()
        # Equipos del juego
        self.players = [
            Player("Gryffindor", "red", self.board.get_start_position("Gryffindor")),
            Player("Hufflepuff", "yellow", self.board.get_start_position("Hufflepuff")),
            Player("Ravenclaw", "blue", self.board.get_start_position("Ravenclaw")),
            Player("Slytherin", "green", self.board.get_start_position("Slytherin"))
        ]
        # Índice del equipo actual
        self.current_player_index = 0
        # Modo desarrollador (permite elegir los valores de los dados)
        self.developer_mode = developer_mode
        # Contador de pares consecutivos
        self.consecutive_pairs = 0

    def start_game(self):
        # Inicia el juego
        print("entrega final programacion de computadores grupo 1")
        print("integrantes: Luis felipe acevedo, jennyfer niño y casas")
        while not self.is_game_over():
            self.play_turn()
            self.next_player()

    def play_turn(self):
        # Lógica para un turno de juego
        player = self.players[self.current_player_index]
        print(f"\nTurno de {player.name} ({player.color})")
        
        # Reinicia el contador de pares consecutivos al inicio del turno
        self.consecutive_pairs = 0
        
        # Lanza los dados
        dice1, dice2 = self.roll_dices()
        
        print(f"Dados: {dice1}, {dice2}")
        
        # Verifica si el equipo sacó un par
        if dice1 == dice2:
            self.consecutive_pairs += 1
            print("¡Dados pares! Jugador lanza de nuevo.")
        
        # Verifica si el equipo ha sacado tres pares consecutivos
        if self.consecutive_pairs == 3:
            self.send_last_moved_piece_to_jail(player)
            self.consecutive_pairs = 0
            return
        
        # Verifica si el equipo debe sacar una ficha de la cárcel
        if (dice1 == 5 or dice2 == 5) and self.can_exit_jail(player):
            self.force_exit_jail(player, dice1, dice2)
            return

        # Obtiene los movimientos posibles
        possible_moves = self.get_possible_moves(player, dice1, dice2)
        
        # Verifica si el equipo tiene movimientos posibles
        if not possible_moves:
            print("No hay movimientos posibles para este turno.")
            return
        
        # Permite al equipo elegir un movimiento
        self.choose_and_execute_move(player, possible_moves, dice1, dice2)

        # Muestra el tablero
        self.board.display_board(self.get_board_state())

    def roll_dices(self):
        # Lanza los dados (o permite elegir los valores en modo desarrollador)
        if self.developer_mode:
            while True:
                try:
                    dice1 = int(input("Ingrese el valor del primer dado (1-6): "))
                    dice2 = int(input("Ingrese el valor del segundo dado (1-6): "))
                    if 1 <= dice1 <= 6 and 1 <= dice2 <= 6:
                        break
                    else:
                        print("Los valores de los dados deben estar entre 1 y 6.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
        else:
            dice1 = self.dice.roll()
            dice2 = self.dice.roll()
        return dice1, dice2

    def can_exit_jail(self, player):
        # Verifica si el equipo puede sacar una ficha de la cárcel
        for piece_index, piece_position in enumerate(player.pieces):
            if piece_position == -1:
                return True
        return False
    
    def force_exit_jail(self, player, dice1, dice2):
        # Fuerza la salida de una ficha de la cárcel
        for piece_index, piece_position in enumerate(player.pieces):
            if piece_position == -1:
                if dice1 == 5:
                # Actualiza la ficha y la saca de la cárcel
                    if player.move_piece(piece_index, 5, self.board, self.get_board_state()):
                        print(f"Ficha {piece_index + 1} salió de la cárcel con un 5 en el primer dado.")
                        return  # Exit after successfully moving a piece
                elif dice2 == 5:
                    if player.move_piece(piece_index, 5, self.board, self.get_board_state()):
                        print(f"Ficha {piece_index + 1} salió de la cárcel con un 5 en el segundo dado.")
                        return  # Exit after successfully moving a piece
    
    def get_possible_moves(self, player, dice1, dice2):
        # Obtiene los movimientos posibles para un equipo
        possible_moves = []
        for piece_index, piece_position in enumerate(player.pieces):
            # Check if the piece is in jail
            if piece_position == -1:
                # If the piece is in jail, a roll of 5 is required to exit
                if dice1 == 5 or dice2 == 5:
                    possible_moves.append({"piece_index": piece_index, "spaces": 5, "exit_jail": True})
            else:
                # Generate movement option for dice 1
                if self.is_valid_move(player, piece_index, dice1):
                    possible_moves.append({"piece_index": piece_index, "spaces": dice1, "exit_jail": False})

                # Generate movement option for dice 2
                if self.is_valid_move(player, piece_index, dice2):
                    possible_moves.append({"piece_index": piece_index, "spaces": dice2, "exit_jail": False})

                # Generate movement option for dice 1 and dice 2
                if self.is_valid_move(player, piece_index, dice1 + dice2):
                    possible_moves.append({"piece_index": piece_index, "spaces": dice1 + dice2, "exit_jail": False})
        return possible_moves
    
    def is_valid_move(self, player, piece_index, spaces):
        # Validate the movement
        current_position = player.pieces[piece_index]
        
        #If the player is in jail
        if current_position == -1:
            return False
        
        # Check if the new position is valid
        new_position = self.board.get_new_position(current_position, spaces, player.name)
        
        if new_position is None:
            return False
            
        # Check if the board is blocked
        board_state = self.get_board_state()
        if self.board.is_blocked(new_position, board_state):
            return False
        
        return True
    
    def choose_and_execute_move(self, player, possible_moves, dice1, dice2):
        # Permite al equipo elegir un movimiento y lo ejecuta
        print("Movimientos posibles:")
        for i, move in enumerate(possible_moves):
            piece_index = move['piece_index'] + 1
            spaces = move['spaces']
            if move['exit_jail']:
                print(f"{i + 1}. Ficha {piece_index} - Salir de la cárcel")
            else:
                print(f"{i + 1}. Ficha {piece_index} - Mover {spaces} casillas")
        
        while True:
            try:
                choice = int(input("Elige el número del movimiento que deseas realizar: ")) - 1
                if 0 <= choice < len(possible_moves):
                    break
                else:
                    print("Número de movimiento inválido. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
        
        chosen_move = possible_moves[choice]
        piece_index = chosen_move['piece_index']
        spaces = chosen_move['spaces']
        
        if chosen_move['exit_jail']:
            if player.move_piece(piece_index, spaces, self.board, self.get_board_state()):
                print(f"Ficha {piece_index + 1} salió de la cárcel.")
        else:
            if player.move_piece(piece_index, spaces, self.board, self.get_board_state()):
                print(f"Ficha {piece_index + 1} movida {spaces} casillas.")

    def get_board_state(self):
        # Obtiene el estado actual del tablero
        board_state = [[] for _ in range(68)]

        # Agrega las posiciones de las fichas de cada equipo al estado del tablero
        for player in self.players:
            for piece_index, piece_position in enumerate(player.pieces):
                if 0 <= piece_position < 68:
                    board_state[piece_position].append(player.name)
        return board_state

    def next_player(self):
        # Pasa al siguiente equipo
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def is_game_over(self):
        # Verifica si el juego ha terminado
        for player in self.players:
            if not player.has_won(self.board):
                return False
        print(f"¡El juego ha terminado!")
        return True

    def send_last_moved_piece_to_jail(self, player):
        # Envía la última ficha movida a la cárcel (por sacar tres pares consecutivos)
        print("Enviando la última ficha movida a la cárcel por sacar tres pares consecutivos.")

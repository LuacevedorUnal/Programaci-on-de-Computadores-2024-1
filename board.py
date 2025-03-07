# src/board.py
class Board:
    def __init__(self):
        # Casillas externas (68 en total)
        self.cells = [None] * 68
        # Casillas seguras
        self.safe_zones = [5, 12, 22, 29, 39, 46, 56, 63]
        # Posiciones de inicio para cada equipo
        self.start_positions = {
            "Gryffindor": 0,
            "Hufflepuff": 17,
            "Ravenclaw": 34,
            "Slytherin": 51
        }
        # Casillas de llegada para cada equipo (internas)
        self.arrival_cells = {
            "Gryffindor": list(range(68, 76)),
            "Hufflepuff": list(range(76, 84)),
            "Ravenclaw": list(range(84, 92)),
            "Slytherin": list(range(92, 100))
        }
        # Máximo de fichas por casilla
        self.max_pieces_per_cell = 2

    def is_safe(self, position):
        # Retorna True si la casilla es segura
        return position in self.safe_zones

    def is_start_position(self, position):
        # Retorna True si la casilla es una posición de inicio
        return position in self.start_positions.values()

    def get_start_position(self, team):
        # Retorna la posición de inicio para un equipo dado
        return self.start_positions[team]

    def is_arrival_cell(self, team, position):
        # Retorna True si la casilla es una casilla de llegada para un equipo
        return position in self.arrival_cells[team]

    def is_valid_move(self, start_position, move, team):
        # Valida si un movimiento es válido
        new_position = start_position + move

        # Valida si el movimiento está en el tablero principal
        if 0 <= new_position < 68:
            return True

        # Valida si el movimiento está en las casillas de llegada
        if 68 <= new_position < 100 and new_position in self.arrival_cells[team]:
            return True

        return False

    def get_new_position(self, current_position, move, team):
        # Obtiene la nueva posición después de un movimiento
        new_position = current_position + move

        # Si la ficha se está moviendo en el tablero principal
        if 0 <= new_position < 68:
            return new_position

        # Si la ficha está entrando a las casillas de llegada
        if 68 <= new_position < 100 and new_position in self.arrival_cells[team]:
            return new_position
        
        # Si la ficha está en una casilla de llegada y se mueve a otra casilla de llegada
        if current_position >= 68 and (68 <= new_position < 100) and new_position in self.arrival_cells[team]:
            return new_position
        
        return None

    def can_exit_jail(self, current_position):
        # Verifica si una ficha puede salir de la cárcel
        if current_position == 0:
            return True
        else:
            return False

    def is_blocked(self, position, board_state):
        # Verifica si una casilla está bloqueada
        if position is None:
            return True
        
        pieces_in_cell = board_state[position]
        if pieces_in_cell is None:
            return False
        
        if len(pieces_in_cell) == self.max_pieces_per_cell:
            return True
        return False

    def display_board(self, board_state):
        # Muestra el tablero en la consola
        print("\n--- TABLERO ---")
        board_display = [" "] * 68  # Initialize with empty spaces

        # Mark safe zones
        for i in self.safe_zones:
            board_display[i] = "S"

        # Mark piece locations
        for i, pieces in enumerate(board_state):
            if pieces:
                board_display[i] = "*".join([p[0].upper() for p in pieces])  # Use first letter of team names

        # Print the board in a readable format
        for i in range(68):
            print(f"{board_display[i]:3}", end="")  # Adjust spacing as needed
            if (i + 1) % 17 == 0:
                print()  # New line after 17 cells
        print("--- FIN DEL TABLERO ---")

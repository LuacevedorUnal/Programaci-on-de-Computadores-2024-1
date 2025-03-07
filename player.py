# src/player.py
class Player:
    def __init__(self, name, color, start_position):
        # Nombre del equipo
        self.name = name
        # Color del equipo
        self.color = color
        # Posiciones de las fichas (-1 significa en la cárcel, sino la casilla en el tablero)
        self.pieces = [-1] * 4
        # Posición de inicio del equipo
        self.start_position = start_position
        # Contador de pares consecutivos
        self.consecutive_pairs = 0

    def move_piece(self, piece_index, spaces, board, board_state):
        # Mueve una ficha
        current_position = self.pieces[piece_index]

        # Si la ficha está en la cárcel y sale con un 5
        if current_position == -1 and spaces == 5:
            self.pieces[piece_index] = self.start_position
            return True

        new_position = board.get_new_position(current_position, spaces, self.name)
        
        # Valida el movimiento
        if new_position is None:
            return False

        if board.is_blocked(new_position, board_state):
            return False
        
        self.pieces[piece_index] = new_position
        return True

    def send_to_jail(self, piece_index):
        # Envía una ficha a la cárcel
        self.pieces[piece_index] = -1

    def has_won(self, board):
        # Verifica si el equipo ha ganado
        for piece_position in self.pieces:
            if not board.is_arrival_cell(self.name, piece_position):
                return False
        return True

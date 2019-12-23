"""It's tic-tac-toe."""
# TODO: make getters for row and diagonals, have them return lists, for use in driver.py


class TicTacToe:
    """A game of tic-tac-toe."""

    MIN_GAME_SIZE = 1

    def __init__(self, game_size):
        """Initialize a game of tic-tac-toe.

        :param int game_size: Length of each row on the game board (and number of rows)
        :raises AssertionError: if game_size is not an int or if game_size >= MIN_GAME_SIZE
        """
        assert isinstance(game_size, int), 'game_size must be an int'
        assert game_size >= self.MIN_GAME_SIZE, 'game_size must be >= {}'.format(self.MIN_GAME_SIZE)

        self.game_size = game_size
        self.current_player = 'X'
        self.board = self.__initialize_board()
        self.winner = None

    @property
    def board_has_free_cells(self):
        """True if there are cells on the board that haven't been used. Else False."""
        for row in self.board:
            if ' ' in row:
                return True
        return False

    def __initialize_board(self):
        """Create a board with all empty spaces for a new game.

        :return: Empty board
        """
        # TODO: google factory pattern
        board = [None] * self.game_size
        for row in range(self.game_size):
            board[row] = [" " for _ in range(self.game_size)]
        print(board)
        return board

    def get_contents_of_cell(self, coordinates):
        """Get the contents of the cell with the specified coordinates"""
        return self.board[coordinates.row][coordinates.column]

    def make_move(self, coordinates):
        """Update the game board with a move.

        :param Coordinates coordinates: Coordinates at which to place move
        """
        self.board[coordinates.row][coordinates.column] = self.current_player

    def get_column(self, column_index):
        column = []
        for row in self.board:
            column.append(row[column_index])
        return column

    def change_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def display_board(self):
        """Print out the current state of the board."""
        for row in self.board:
            print(row)


# pylint: disable=too-few-public-methods
class Coordinates:
    """A pair of coordinates on a tic-tac-toe board."""

    def __init__(self, row, column):
        """Initialize coordinates.

        :param int row: Row on board
        :param int column: Column on board
        """
        self.row = row
        self.column = column

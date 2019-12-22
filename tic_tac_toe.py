"""It's tic-tac-toe."""
import errors


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
        for row in self.board:
            if ' ' in row:
                return True
        return False

    def __initialize_board(self):
        """Create a board with all empty spaces for a new game.

        :return: Empty board
        """
        board = [_ for _ in range(self.game_size)]
        for row in range(self.game_size):
            board[row] = [" " for _ in range(self.game_size)]
        print(board)
        return board

    def execute_turn(self, move):
        """Make move, check if game has been won, and if not change the current player

        :param Move move: Move with which to update the board
        """
        self.__make_move(move)
        self.__check_if_game_is_over()
        if not self.winner:
            self.__change_player()

    def __make_move(self, move):
        """Update the game board with a move.

        :param Move move: Move with which to update the board
        """
        if self.board[move.row][move.column] != ' ':
            raise errors.CellInUseError('This cell has already been used.')
        self.board[move.row][move.column] = self.current_player

    def __check_if_game_is_over(self):
        # TODO: Make sure game ends if all moves have been played, but no one has won
        self.__check_rows_for_win()
        self.__check_columns_for_win()
        self.__check_upper_left_to_lower_right_diagonal_for_win()
        self.__check_lower_left_to_upper_right_diagonal_for_win()
        if not self.board_has_free_cells:
            self.winner = 'No one'

    def __check_rows_for_win(self):
        for row in self.board:
            if self.__all_moves_are_equal(moves=row):
                self.winner = self.current_player

    def __check_columns_for_win(self):
        for column_index in range(self.game_size):
            column = self.__get_column(column_index)
            if self.__all_moves_are_equal(moves=column):
                self.winner = self.current_player

    def __get_column(self, column_index):
        column = []
        for row in self.board:
            column.append(row[column_index])
        return column

    def __check_upper_left_to_lower_right_diagonal_for_win(self):
        diagonal = []
        for _ in range(self.game_size):
            next_move = self.board[_][_]
            diagonal.append(next_move)
        if self.__all_moves_are_equal(moves=diagonal):
            self.winner = self.current_player

    def __check_lower_left_to_upper_right_diagonal_for_win(self):
        diagonal = []
        for _ in range(self.game_size):
            next_move = self.board[self.game_size - _ - 1][_]
            diagonal.append(next_move)
        if self.__all_moves_are_equal(moves=diagonal):
            self.winner = self.current_player

    def __all_moves_are_equal(self, moves):
        first_move = moves[0]
        if first_move != ' ':
            all_moves_are_the_same = all([moves[0] == move for move in moves])
            return all_moves_are_the_same

    def __change_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def display_board(self):
        """Print out the current state of the board."""
        for row in self.board:
            print(row)


class Move:
    """A move in tic-tac-toe."""

    def __init__(self, row, column):
        """Initialize move.

        :param int row: Row in which to place move
        :param int column: Column in which to place move
        """
        self.row = row
        self.column = column

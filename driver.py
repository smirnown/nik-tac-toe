"""Drive doc string."""
import errors
from tic_tac_toe import (
    TicTacToe,
    Coordinates,
)


class TicTacToeDriver:
    """Driver for TicTacToe game."""

    def __init__(self):
        """Initialize driver.

        :param TicTacToe game: A game of tic-tac-toe
        """
        self.game = self.__create_game()

    def __create_game(self):
        """Start a new game of tic-tac-toe.

        :raise AssertionError: if player doesn't pick a non-zero integer for the size of the game
        :return: A newly instantiated TicTacToe object
        """

        game = None
        while not game:
            try:
                game_size = int(input('What size board would you like to play with?'))
                game = TicTacToe(game_size)
            except AssertionError:
                print('Please pick an integer greater than 0')

        return game

    def run_game(self):
        """Run the game."""
        while not self.game.winner:
            coordinates = self.pick_coordinates_for_next_move()
            self.game.make_move(coordinates)
            self.check_if_game_is_over()
            self.game.change_player()
            self.game.display_board()

    def pick_coordinates_for_next_move(self):
        """Pick which row and column to make the next move in.

        :returns Coordinates: Coordinates at which to make next move
        """
        coordinates = None
        selecting_coordinates = True
        while selecting_coordinates:
            try:
                coordinates = self.__get_user_input()
                selecting_coordinates = False
            except IndexError:
                print('These coordinates are out of bounds. Please pick a different row and/or column.')
            except ValueError:
                print('You must pick integers for row and column.')
            except errors.CellInUseError:
                print('These coordinates are occupied. Please pick a different row and/or column.')
        return coordinates

    def __get_user_input(self):
        row = int(input('In what row would you like to make your move?'))
        column = int(input('In what column would you like to make your move?'))

        valid_user_inputs = [_ for _ in range(self.game.game_size)]
        if not (row in valid_user_inputs and column in valid_user_inputs):
            raise IndexError('These coordinates are out of bounds. Please pick a different row and/or column.')

        coordinates = Coordinates(row, column)
        contents_of_cell = self.game.get_contents_of_cell(coordinates)
        if contents_of_cell != ' ':
            raise errors.CellInUseError('This cell has already been used.')

        return coordinates

    def check_if_game_is_over(self):
        self.__check_rows_for_win()
        self.__check_columns_for_win()
        self.__check_upper_left_to_lower_right_diagonal_for_win()
        self.__check_lower_left_to_upper_right_diagonal_for_win()
        if not self.game.board_has_free_cells:
            self.game.winner = 'No one'

    def __check_rows_for_win(self):
        for row in self.game.board:
            if self.__all_moves_are_equal(moves=row):
                self.game.winner = self.game.current_player

    def __check_columns_for_win(self):
        for column_index in range(self.game.game_size):
            column = self.game.get_column(column_index)
            if self.__all_moves_are_equal(moves=column):
                self.game.winner = self.game.current_player

    def __check_upper_left_to_lower_right_diagonal_for_win(self):
        diagonal = []
        for _ in range(self.game.game_size):
            next_move = self.game.board[_][_]
            diagonal.append(next_move)
        if self.__all_moves_are_equal(moves=diagonal):
            self.game.winner = self.game.current_player

    def __check_lower_left_to_upper_right_diagonal_for_win(self):
        diagonal = []
        for _ in range(self.game.game_size):
            next_move = self.game.board[self.game.game_size - _ - 1][_]
            diagonal.append(next_move)
        if self.__all_moves_are_equal(moves=diagonal):
            self.game.winner = self.game.current_player

    def __all_moves_are_equal(self, moves):
        first_move = moves[0]
        if first_move != ' ':
            all_moves_are_the_same = all([moves[0] == move for move in moves])
            return all_moves_are_the_same
# TODO: Find a better way to implement this code than helper functions
from tic_tac_toe import TicTacToe, Move
import errors


def create_game():
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


def pick_move_to_make():
    """Pick which row and column to make the next move in.

    :returns Move: Move to be made
    """
    selecting_move = True
    while selecting_move:
        try:
            row = int(input('In what row would you like to make your move?'))
            column = int(input('In what column would you like to make your move?'))
            return Move(row, column)
        except ValueError:
            print('You must pick integers for row and column.')


def execute_turn(game, move):
    """"""
    try:
        game.execute_turn(move)
    except IndexError:
        print('This move is out of bounds. Please pick a different row and/or column.')
    except errors.CellInUseError:
        print('This cell is occupied. Please pick a different row and/or column.')

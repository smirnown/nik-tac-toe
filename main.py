"""Execute this file to play tic-tac-toe."""

from helpers import (
    create_game,
    pick_move_to_make,
    execute_turn,
)

GAME = create_game()
while not GAME.winner:
    MOVE = pick_move_to_make()
    execute_turn(GAME, MOVE)
    GAME.display_board()

print('Congratulations! {}s wins!'.format(GAME.winner))

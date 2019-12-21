from helpers import (
    create_game,
    pick_move_to_make,
    execute_turn,
)

game = create_game()
while not game.is_over:
    move = pick_move_to_make()
    execute_turn(game, move)
    game.display_board()

print('Congratulations! The player playing {}s wins!'.format(game.current_move_marker))

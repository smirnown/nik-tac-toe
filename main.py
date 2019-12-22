from helpers import (
    create_game,
    pick_move_to_make,
    execute_turn,
)

game = create_game()
while not game.winner:
    move = pick_move_to_make()
    execute_turn(game, move)
    game.display_board()

print('Congratulations! {}s wins!'.format(game.winner))

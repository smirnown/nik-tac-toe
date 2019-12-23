"""Execute this file to play tic-tac-toe."""

from driver import TicTacToeDriver

DRIVER = TicTacToeDriver()
DRIVER.run_game()
print('Congratulations! {}s wins!'.format(DRIVER.game.winner))

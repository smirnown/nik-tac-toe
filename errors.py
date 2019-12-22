"""Tic-Tac-Toe errors."""


class CellInUseError(Exception):
    """Error raised when trying to overwrite an in-use cell."""

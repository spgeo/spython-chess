import enum

class Color(enum.Enum):
    WHITE = 0
    BLACK = 1

class Piece(enum.Enum):
    EMPTY = enum.auto()
    PAWN = enum.auto()
    ROOK = enum.auto()
    KNIGHT = enum.auto()
    BISHOP = enum.auto()
    KING = enum.auto()
    QUEEN = enum.auto()

PIECES = {
    (Color.WHITE, Piece.EMPTY): "",
    (Color.WHITE, Piece.PAWN): "\u2659",
    (Color.WHITE, Piece.ROOK): "\u2656",
    (Color.WHITE, Piece.KNIGHT): "\u2658",
    (Color.WHITE, Piece.BISHOP): "\u2657",
    (Color.WHITE, Piece.KING): "\u2654",
    (Color.WHITE, Piece.QUEEN): "\u2655",
    (Color.BLACK, Piece.PAWN): "\u265F",
    (Color.BLACK, Piece.ROOK): "\u265C",
    (Color.BLACK, Piece.KNIGHT): "\u265E",
    (Color.BLACK, Piece.BISHOP): "\u265D",
    (Color.BLACK, Piece.KING): "\u265A",
    (Color.BLACK, Piece.QUEEN): "\u265B",
    (Color.BLACK, Piece.EMPTY): "\u25FC",
}

FEN_TO_PIECES = {
    ' ': (Color.WHITE, Piece.EMPTY),
    'R': (Color.WHITE, Piece.ROOK),
    'N': (Color.WHITE, Piece.KNIGHT),
    'B': (Color.WHITE, Piece.BISHOP),
    'Q': (Color.WHITE, Piece.QUEEN),
    'K': (Color.WHITE, Piece.KING),
    'P': (Color.WHITE, Piece.PAWN),
    'r': (Color.BLACK, Piece.ROOK),
    'n': (Color.BLACK, Piece.KNIGHT),
    'b': (Color.BLACK, Piece.BISHOP),
    'q': (Color.BLACK, Piece.QUEEN),
    'k': (Color.BLACK, Piece.KING),
    'p': (Color.BLACK, Piece.PAWN)
}

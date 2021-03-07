from tkinter import *
from tkinter import colorchooser

from globals import *
from drag_handler import DragHandler

HEX_INDEX = 1


class Board:
    """Used to represent a chess board drawn on a design canvas.
    Allows for parameterizing the scale as well as dynamically setting the square colors when run in debug mode.
    """

    root = Tk()
    scale_weight = 2
    scale_range = 25 * scale_weight
    num_rows = 8
    num_columns = 8

    COLOR_LIGHT = '#F0D9B5'
    COLOR_DARK = '#B58863'
    dnd = DragHandler(scale_range)
    debug = False
    elements = {}


    def __init__(self, debug=False):
        def change_color(squares):
            """Allows to select and dynamically change the color of squares

            Args:
                squares ([tkinter.Rectangle]): A list of squares to act upon

            Returns:
                str: a string representing the new color
            """

            color = colorchooser.askcolor(title="Choose color")[HEX_INDEX]
            for square in squares:
                self.canvas.itemconfig(square, fill=color)
            self.root.update_idletasks()
            self.root.update()
            return color


        def update_dark_color():
            """Updates the color for the dark squares of the board"""
            self.COLOR_DARK = change_color(self.dark_squares)
            print(f"light: {self.COLOR_LIGHT}, dark: {self.COLOR_DARK}")


        def update_light_color():
            """Updates the color for the light squares of the board"""
            self.COLOR_LIGHT = change_color(self.light_squares)
            print(f"light: {self.COLOR_LIGHT}, dark: {self.COLOR_DARK}")


        if debug is True:
            self.debug = debug
            self.light_squares = []
            self.dark_squares = []

        self.root.title("Spichess")
        self.canvas = Canvas(
            self.root,
            width=self.num_columns * self.scale_range,
            height=self.num_rows * self.scale_range
        )
        self.canvas.pack()

        self.draw_board()

        if self.debug is True:
            light_color_btn = Button(self.root, text="Select light-square color", command=update_light_color)
            light_color_btn.pack()
            dark_color_btn = Button(self.root, text="Select dark-square color", command=update_dark_color)
            dark_color_btn.pack()

        self.root.geometry(f"{self.num_columns * self.scale_range}x{self.num_rows * self.scale_range}")

        self.set_position()

        self.root.mainloop()


    def draw_board(self):
        """Draws the chess board, i.e., a set of 8x8 inversely-colored squares.
        The bottom-right corner should always be a light square.
        """

        for i in range(self.num_rows):
            for j in range(self.num_columns):
                square_color = self.COLOR_LIGHT if (i + j) % 2 == 0 else self.COLOR_DARK
                square = self.canvas.create_rectangle(
                    j * self.scale_range,
                    i * self.scale_range,
                    (j + 1) * self.scale_range,
                    (i + 1) * self.scale_range,
                    fill=square_color,
                    outline=square_color
                )
                if self.debug is True:
                    if square_color == self.COLOR_LIGHT:
                        self.light_squares.append(square)
                    else:
                        self.dark_squares.append(square)


    def set_position(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
        # fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2'
        def expand_fen_row(fen_row):
            expanded_fen_row = ''
            for c in fen_row:
                if c.isdigit():
                    expanded_fen_row += ' ' * int(c)
                else:
                    expanded_fen_row += c
            return expanded_fen_row


        print(f"FEN: {fen}")
        piece_placement, active_color, castling_availability, en_passant_square, halfmove_clock, fullmove_number = fen.split(' ')
        fen_rows = piece_placement.split('/')

        for i in range(self.num_rows):
            fen_row = expand_fen_row(fen_rows[i])
            print(fen_row)
            for j in range(self.num_columns):
                element = self.canvas.create_text(
                    j * self.scale_range + self.scale_range / 2,
                    i * self.scale_range + self.scale_range / 2,
                    text=PIECES.get(FEN_TO_PIECES[fen_row[j]]),
                    font=('Helvetica', -self.scale_range),
                )
                print(element)
                print(j * self.scale_range + self.scale_range / 2, i * self.scale_range + self.scale_range / 2)
                self.elements[element] = self.dnd.make_draggable(self.canvas, element)
        print(self.elements)




from tkinter import *
from tkinter import colorchooser
from functools import partial

HEX_INDEX = 1

class Board():
    """Used to represent a chess board drawn on a design canvas. Allows for parameterizing the scale as well as dynamically
    setting the square colors when run in debug mode."""

    root = Tk()
    scale_weight = 2
    scale_range = 50 * scale_weight
    num_rows = 8
    num_columns = 8

    COLOR_LIGHT = '#F0D9B5'
    COLOR_DARK = '#B58863'

    debug = False

    def __init__(self, debug=False):
        def change_color(canvas, squares):
            """Allows to select and dynamically change the color of squares on a given canvas

            Args:
                canvas (tkinter.Canvas): The concerned canvas
                squares ([tkinter.Rectanle]): A list of squares to act upon

            Returns:
                str: a string representing the new color
            """

            color = colorchooser.askcolor(title ="Choose color")[HEX_INDEX]
            for square in squares:
                canvas.itemconfig(square, fill=color)
            self.root.update_idletasks()
            self.root.update()
            return color

        def update_dark_color(canvas):
            """Updates the color for the dark squares of the board

            Args:
                canvas (tkinter.Canvas): The concerned canvas
            """
            self.COLOR_DARK = change_color(canvas, self.dark_squares)
            print(f"light: {self.COLOR_LIGHT}, dark: {self.COLOR_DARK}")

        def update_light_color(canvas):
            """Updates the color for the light squares of the board

            Args:
                canvas (tkinter.Canvas): The concerned canvas
            """
            self.COLOR_LIGHT = change_color(canvas, self.light_squares)
            print(f"light: {self.COLOR_LIGHT}, dark: {self.COLOR_DARK}")

        if debug is True:
            self.debug = debug
            light_squares = []
            dark_squares = []

        self.root.title("Spichess")
        canvas = Canvas(
            self.root,
            width=self.num_columns * self.scale_range,
            height=self.num_rows * self.scale_range
        )
        canvas.pack()
        self.draw_board(canvas)

        if self.debug is True:
            light_color_btn = Button(self.root, text="Select light-square color", command=partial(update_light_color, canvas))
            light_color_btn.pack()
            dark_color_btn = Button(self.root, text="Select dark-square color", command=partial(update_dark_color, canvas))
            dark_color_btn.pack()

        self.root.geometry(f"{self.num_columns * self.scale_range}x{self.num_rows * self.scale_range}")
        self.root.mainloop()

    def draw_board(self, canvas):
        """Draws the chess board, i.e., a set of 8x8 inversely-colored squares.
        The bottom-right corner should always be a light square.

        Args:
            canvas (tkinter.Canvas): The concerned canvas
        """

        for i in range(self.num_rows):
            for j in range(self.num_columns):
                square_color = self.COLOR_LIGHT if (i+j) % 2 == 0 else self.COLOR_DARK
                square = canvas.create_rectangle(
                    i * self.scale_range,
                    j * self.scale_range,
                    (i+1) * self.scale_range,
                    (j+1) * self.scale_range,
                    fill=square_color,
                    outline=square_color
                )
                if self.debug is True:
                    if square_color == self.COLOR_LIGHT:
                        self.light_squares.append(square)
                    else:
                        self.dark_squares.append(square)

if __name__ == '__main__':
    board = Board()

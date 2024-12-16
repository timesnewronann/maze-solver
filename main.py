import tkinter as tk
from window import Window
from shapes import Point, Line
from cell import Cell


def main():
    # Set up Tkinter window and canvas
    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=400, bg='white')
    canvas.pack()

    # Create a few Cell instances at different coordinates for testing
    cells = [
        Cell(50, 50, 150, 150, True, False, True, True),
        Cell(150, 150, 250, 250, False, True, True, False),
        Cell(250, 50, 350, 150, False, True, False, True)
    ]

    # Modify cells to simulate different wall configurations
    # cells[0].has_right_wall = False
    # cells[1].has_left_wall = False
    # cells[1].has_bottom_wall = False
    # cells[2].has_left_wall = False

    # Draw each cell on the canvas
    for cell in cells:
        cell.draw(canvas)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()

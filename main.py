import tkinter as tk
from cell import Cell
from maze import Maze


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

    # Draw each cell on the canvas
    for cell in cells:
        cell.draw(canvas)

    # Create a Maze instance: Adjust parameters as necessary for your logic.
    # The necessity of Window object depends on its role.
    maze = Maze(
        x1=0, y1=0,
        num_rows=10,
        num_cols=10,
        cell_size_x=40,
        cell_size_y=40,
        win=None  # Placeholder if Window is not yet interacting
    )
    maze._create_cells()  # Initiate maze logic with drawing

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()

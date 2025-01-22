from cell import Cell
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win,):
        # intialize data members for all inputs then calls _create_cells() method
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        # call _create_cells() method
        self._create_cells()

    # Fill a self._cells list with lists of cells. Each top-level list is a column of Cell objects
    def _create_cells(self):
        # fill the self._cells  with Cell objects, use a nested loop structure
        # intialize list that will hold the columns
        self._cells = []
        # 1. Outer loop for columns: Iterate over num_cols to build the outer list
        for i in range(self.num_cols):
            column = []  # initialize the list for the current column
            # 2. Inner Loop for Rows: For each column, iterate over num_rows, creating Cell instances and adding them to the current column list
            for j in range(self.num_rows):
                # 3. Appending the column: Append each completed column list to self._cells
                # create a new cell instance and add it to the current column
                x_position = self.x1 + i * self.cell_size_x
                y_position = self.y1 + j * self.cell_size_y
                cell = Cell(x_position, y_position, x_position + self.cell_size_x, y_position + self.cell_size_y, has_left_wall=True,
                            has_right_wall=True, has_top_wall=True, has_bottom_wall=True)
                column.append(cell)
            self._cells.append(column)

    # Determine where to draw each Cell in relation to the Maze's position and cell size -> invoke the cell's drawing method
    def _draw_cell(self, i, j):
        # 1. Calculate the cell's position
        # Use the i and j values -> calculate the cell's x and y positions with respect to the maze's starting position and cell size
        x_position = self.x1 + i * self.cell_size_x
        y_position = self.y1 + j * self.cell_size_y
        # 2. Call the cell's draw method:
        # Each cell might have its own draw() method to render itself using those coordinates
        self._cells[i][j].draw(x_position, y_position)
        # 3. Animation
        # After drawing a cell, invoke the maze's _animate() method to update the visual display
        self._animate()

    def _animate(self):
        # 1. Redraw the window
        self.win.redraw()

        # Puase so the animation can be seen
        time.sleep(0.05)

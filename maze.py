from cell import Cell


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
        self._create_cells(self)

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

    def _draw_cell(self, i, j):
        pass

    def _animate(self):
        pass

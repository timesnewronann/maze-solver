class Cell:
    def __init__(self, x1, y1, x2, y2, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1, self._y1 = x1, y1
        self._x2, self._y2 = x2, y2

    # Cell class needs to be able to draw itself to its canvas
    # Take x/y coordinates of it's top left corner and bottom right corner as input
    # If the cell has a left wall, draw it
    # If the cell has a top wall draw it
    def draw(self, canvas):
        line_color = "black"
        # Draw the left wall if it exists.
        if self.has_left_wall:
            canvas.create_line(self._x1, self._y1, self._x1,
                               self._y2, fill=line_color)
        # Draw the right wall if it exists.
        if self.has_right_wall:
            canvas.create_line(self._x2, self._y1, self._x2,
                               self._y2, fill=line_color)
        # Draw the top wall if it exists.
        if self.has_top_wall:
            canvas.create_line(self._x1, self._y1, self._x2,
                               self._y1, fill=line_color)
        # Draw the bottom wall if it exists.
        if self.has_bottom_wall:
            canvas.create_line(self._x1, self._y2, self._x2,
                               self._y2, fill=line_color)

    # main difference between methods -> instead of drawing along the edges/walls. I will be drawing from one cell center to another cell center
    # Do we know how to find the x,y coordinates for a wall?
    # How would I modify these calculations to another cell's center?
    # draw a path between 2 cells. Draw a line from the center of one cell to another

    # self -> starting cell (where the line starts)
    # to_cell -> destination cell (where the line ends)
    def draw_move(self, to_cell, canvas, undo=False):
        # If the undo flag is not set -> the line should be "red"
        # Else line should be "gray"
        # Why: when we draw the path, whenever we backtrack we can show that in a different color to better visualize what's happening

        # 1. calculate the center point of my current cell
        current_center_x = (self._x1 + self._x2) / 2
        current_center_y = (self._y1 + self._y2) / 2

        # 2. Calculate the center of to_cell (destination cell)
        to_cell_center_x = (to_cell._x1 + to_cell._x2) / 2
        to_cell_center_y = (to_cell._y1 + to_cell._y2) / 2

        # 3. Draw a line between these two points
        if undo == False:
            canvas.create_line(current_center_x, current_center_y,
                               to_cell_center_x, to_cell_center_y, fill="red")

        else:
            canvas.create_line(current_center_x, current_center_y,
                               to_cell_center_x, to_cell_center_y, fill="gray")

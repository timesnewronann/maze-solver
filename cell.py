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

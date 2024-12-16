class Point:
    # simply store 2 public data members
    def __init__(self, x, y):
        self.x = x  # x-coordinate (horizontal) in pixels of the point
        self.y = y  # y-coordinate (vertical) in pixels of the point


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color = 'black'):
        # use the coordinates from the point objects to draw the line on the canvas
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y

        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )

from window import Window
from shapes import Point, Line


def main():
    # define a window size
    width = 800
    height = 600
    # create a window instance
    window = Window(width, height)

    # define points
    point1 = Point(50, 50)
    point2 = Point(200, 200)
    point3 = Point(300, 100)
    point4 = Point(100, 300)

    # Create lines using the points
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)

    # Draw lines on the window
    window.draw_line(line1, "red")
    window.draw_line(line2, "blue")

    window.wait_for_close()


if __name__ == "__main__":
    main()

from tkinter import Tk, BOTH, Canvas
from shapes import Line, Point


class Window:

    # constructor: Tk() an object that manages a window on our screen
    # 1. Create a window (self.__root = Tk())
    # 2. Setting up window property
    # 3. Creating a canvas inside to draw
    # 4. Running state initalization
    # 5. Protocol Setup
    def __init__(self, width, height):
        self.__root = Tk()  # create the window frame
        self.__root.title("Maze Solver")  # set title property of root widget

        self.__canvas = Canvas(self.__root, width=width,
                               height=height)  # create a canvas widget

        # organize widgets in our window (pack boxes in a container)
        self.__canvas.pack(fill=BOTH, expand=1)

        # create a private running state variable (initialized to False)
        # set up the protocol for handling window closure
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # Method we can call that will redraw all the graphics in the window
    def redraw(self):
        # simply call root widget's update_idletasks() and update()
        self.__root.update_idletasks()
        self.__root.update()

    # Method should set the running state of the window to True
    # Then call self.redraw over and over as long running state is True
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    # set the running state to False, add another line to constructor to call protocol method on the widge to connect cose
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

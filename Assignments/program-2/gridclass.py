from graphics import *
import json
import random

class Grid(object):
    """
    a value is passed in to the constructor and continues if the value is a perfect square
    a window is created and white background is drawn to the screen
    a list which holds color values is created
    calls the draw grid method
    """
    def __init__(self, gridSize):
        if not self.__isSquare(gridSize):
            print "%d not so much" % gridSize
            exit()
        self.square = (int(round(gridSize ** .5)))
        self.cols = gridSize
        self.rows = gridSize
        self.height = 500
        self.width = 500
        self.win = GraphWin("Grid", self.width, self.height)
        self.win.setCoords(0, 0, self.rows, self.cols)
        self.bkgrnd = Rectangle(Point(0, 0), Point(self.width, self.height))
        self.bkgrnd.setFill(color_rgb(255,255,255))
        self.nrows = gridSize
        self.color_wheel = []
        self.cur_color = None

        self.__make_color_wheel()
        self.cur_color = self.__get_next_color()

        self.__draw_grid()

    def __make_color_wheel(self):
        """
        opens colors.json and appends the hexadecimal color values to self.color_wheel
        """
        with open("colors.json") as file:
            colors = file.read()
        colors = json.loads(colors)

        for color in colors:
            self.color_wheel.append(color["html"])

    def __get_cur_color(self):
        """
        returns a color using the int self.cur_color as in index in self.color_wheel
        """
        return self.color_wheel[self.cur_color]

    def __get_next_color(self):
        """
        if self.cur_color has a value, pop it from the list self.color_wheel
        if self.color_wheel has no values, populate the list again
        assign self.cur_color to a random integer which will be used as the index
        in self.color_wheel
        """
        if self.cur_color:
            self.color_wheel.pop(self.cur_color)
        if not len(self.color_wheel):
            self.__make_color_wheel()
        self.cur_color = random.randint(0,len(self.color_wheel) - 1)
        return self.cur_color

    def __draw_grid(self):
        """
        the grid is populated with large cells and subgrids in each cell
        that have the same number of columns and rows (3 x 3 grid has a smaller 3 x 3 grid in each cell)
        each cell in the large grid has a different color chosen randomly from the color wheel list
        """
        for row in range(self.square):
            for col in range(self.square):
                for sub_row in range(row * self.square, row * self.square + self.square):
                    for sub_col in range(col * self.square, col * self.square + self.square):
                        self.__fill_cell(sub_row, sub_col, self.__get_cur_color())
                self.cur_color = self.__get_next_color()

    def __fill_cell(self, row, col, color):
        """Fill cell[row,col] with color.
        
        Args: 
            row:  which row the selected cell is in.  Row 0 is the top row, 
            row 1 is the next row down, etc.  Row should be between 0 
            and one less than the number of rows in the grid. 
            col:  which column the selected cell is in.  Column 0 is 
            the leftmost row, column 1 is the next row to the right, etc. 
            Col should be between 0 and one less than the number of columns
            in the grid. 
        """
        left = col
        right = col + 1
        top = self.nrows - (row + 1)
        bottom = self.nrows - row
        mark = Rectangle(Point(left,bottom), Point(right,top))
        mark.setFill(color)
        mark.draw(self.win)

    def close(self):
        """
        close the graphics window (shut down graphics). 
        and exit the program
        """
        self.win.close()
        exit()

    def __isSquare(self, num):
        """
        determines if a number is a perfect square
        (I haven't found the threshold, but does not work for very large numbers)

        rounds the square root of a number to the nearest whole number
        casts the result to type int
        squares that result and compares it to the original number
        returns num instead of true, for case when user enters 0
        """
        if int(round(num ** .5)) ** 2 == num:
            return num
        else:
            return False

square = Grid(49)
raw_input("Press enter to continue")
square.close()
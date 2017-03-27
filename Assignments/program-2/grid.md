``` python
"""
Program:
--------
    program 2 - gridception

Description:
------------
    this program either accepts a command line argument or asks user to enter a number
    which is used to define the dimensions of a square. If the number is a perfect square
    a grid will be created and drawn to the screen with two sides that are equal to the
    square root of that number
    in each cell will be another grid with the same dimensions. Each larger cell will have
    a different color
    
Name: Coty Hamilton
Date: 28 Mar 2016
"""

from graphics import *
import json
import random
import sys

class Grid(object):
    """ this class defines a grid and draws it to the screen

    Attributes:
        square: square root of the number the user defined, used in creation of grid
        cols: number of columns in grid
        rows: number of rows in grid
        nrows: number of rows in grid
        height: height in px of graphics window
        width: width in px of graphics window
        win: instance of graphics object
        color_wheel: list of hex color values
        cur_color: index of current color in color_wheel
    """

    def __init__(self, gridSize):
        """
        a value is passed in to the constructor and continues if the value is a
        perfect square
        a window is created and white background is drawn to the screen
        a list which holds color values is created
        calls the draw grid method
        """
        if not self.__isSquare(gridSize):
            print "%f not so much" % gridSize
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
        """ populates color_wheel list

        opens colors.json and appends the hexadecimal color values to self.color_wheel
        
        Args:
            none
        Returns:
            none
        """
        with open("colors.json") as file:
            colors = file.read()
        colors = json.loads(colors)

        for color in colors:
            self.color_wheel.append(color["html"])

    def __get_cur_color(self):
        """ returns hex color value using the int self.cur_color as in index
        in self.color_wheel
        """
        return self.color_wheel[self.cur_color]

    def __get_next_color(self):
        """ updates cur_color with a random value

        if self.cur_color has a value, pop it from the list self.color_wheel
        if self.color_wheel has no values, populate the list again
        assign self.cur_color to a random integer which will be used as the index
        in self.color_wheel

        Args:
            none
        Returns:
            cur_color
        """
        if self.cur_color:
            self.color_wheel.pop(self.cur_color)
        if not len(self.color_wheel):
            self.__make_color_wheel()
        self.cur_color = random.randint(0,len(self.color_wheel) - 1)
        return self.cur_color

    def __draw_grid(self):
        """ draws the grid to the screen
        
        the grid is populated with large cells and subgrids in each cell
        that have the same number of columns and rows (3 x 3 grid has a smaller 3 x 3 grid in each cell)
        each cell in the large grid has a different color chosen randomly from the color wheel list
        
        Args:
            none
        Returns:
            none
        """
        for row in range(self.square):
            for col in range(self.square):
                for sub_row in range(row * self.square, row * self.square + self.square):
                    for sub_col in range(col * self.square, col * self.square + self.square):
                        self.__fill_cell(sub_row, sub_col, self.__get_cur_color())
                self.cur_color = self.__get_next_color()

    def __fill_cell(self, row, col, color):
        """ fill cell[row,col] with color.
        
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
        """ closes the graphics window and exits the program
        
        Args:
            none
        Returns:
            none
        """
        self.win.close()
        exit()

    def __isSquare(self, num):
        """ determines if a number is a perfect square
        (I haven't found the threshold, but does not work for very large numbers)

        rounds the square root of a number to the nearest whole number
        casts the result to type int
        squares that result and compares it to the original number

        Args:
            num: number that needs to be determined to having perfect square
        Returns:
            False: if num is not perfect square
            num: if num is perfect square. num instead of true because of case 0,
                which passes this test but doesn't need to be drawn to screen
        """
        if int(round(num ** .5)) ** 2 == num:
            return num
        else:
            return False

if __name__ == "__main__":
    if len(sys.argv) == 2:
        option = float(sys.argv[1])
    else:
        option = input("Enter a Number: ")
    square = Grid(option)
    raw_input("Press enter to continue")
    square.close()
    
    ```

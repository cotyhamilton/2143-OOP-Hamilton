from graphics import *

class Grid(object):
    def __init__(self, gridSize):
        if not self.__isSquare(gridSize):
            print "%d not so much" % gridSize
            exit()
        square = (int(round(gridSize ** .5)))
        self.cols = gridSize
        self.rows = gridSize
        self.height = 500
        self.width = 500
        self.win = GraphWin("Grid", self.width, self.height)
        self.win.setCoords(0, 0, self.rows, self.cols)
        self.bkgrnd = Rectangle(Point(0, 0), Point(self.width, self.height))
        self.bkgrnd.setFill(color_rgb(255,255,255))
        self.nrows = self.rows
        self.color_wheel = [  color_rgb(255,0,0), color_rgb(0,255,0), color_rgb(0,0,255),
                        color_rgb(255,255,0), color_rgb(255,0,255), color_rgb(0,255,255),
                        color_rgb(127,255,0), color_rgb(0,127,255), color_rgb(127,0,255),
                        color_rgb(255,127,0), color_rgb(0,255,127), color_rgb(255,0,127),
                        color_rgb(127,127,0), color_rgb(127,0,127), color_rgb(0,127,127),
                        color_rgb(255,255,127), color_rgb(255,127,255), color_rgb(127,255,255) ]

        self.cur_color = 0

        for row in range(square):
            for col in range(square):
                for sub_row in range(row * square, row * square + square):
                    for sub_col in range(col * square, col * square + square):
                        self.__fill_cell(sub_row, sub_col, self.__get_cur_color())
                self.cur_color = self.__get_next_color()

    def __make_color_wheel(self):
        self.color_wheel = []

        

    def __get_cur_color(self):
        """Return the currently chosen color in the color wheel.  

        The color wheel is a list of colors selected to be contrast with each other. 
        The first few entries are bright primary colors; as we cycle through the color
        wheel, contrast becomes less, but colors should remain distinct to those with 
        normal color vision until the color wheel cycles all the way around in 18 
        choices and starts recycling previously used colors.   The color wheel starts
        out in position 0, so get_cur_color() may be called before get_next_color() has 
        been called. 
        
        Args:  none
        Returns:  
            a 'color' that can be passed to fill_cell
            
        FIXME: The color wheel should produce colors of contrasting brightness
        as well as hue, to maximize distinctness for dichromats (people with 
        "color blindness".  Maybe generating a good color wheel can be part of a 
        project later in CIS 210.   (This is not a required or expected change 
        for the week 4 project.) 
        """
        return self.color_wheel[self.cur_color]

    def __get_next_color(self):
        """Advance the color wheel, returning the next available color. 

        The color wheel is a list of colors selected to be contrast with each other. 
        The first few entries are bright primary colors; as we cycle through the color
        wheel, contrast becomes less, but colors should remain distinct to those with 
        normal color vision until the color wheel cycles all the way around in 18 
        choices and starts recycling previously used colors. 
        
        Args:  none
        Returns:  
            a 'color' that can be passed to fill_cell    
        """
        self.cur_color += 1
        if self.cur_color >= len(self.color_wheel) :
            self.cur_color = 0
        return self.cur_color

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
            color: What color to fill fill the selecte cell with.  Valid colors
            include grid.white, grid.black, and values returned by 
            grid.get_next_color() and grid.get_cur_color()

        """
        left = col
        right = col + 1
        top = self.nrows - (row + 1)
        bottom = self.nrows - row
        mark = Rectangle(Point(left,bottom), Point(right,top))
        mark.setFill(color)
        mark.draw(self.win)

    def close(self):
        """ Close the graphics window (shut down graphics). 
        
        Args: none
        Returns: nothing
        Effect:  the grid graphics window is closed. 
        """
        self.win.close()
        exit()

    def __isSquare(self, num):
        if int(round(num ** .5)) ** 2 == num:
            return True
        else:
            return False

square = Grid(25)
input("Press enter to exit")
square.close()
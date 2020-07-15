CANVAS = [["","","","","","","","","",""],
         ["","","","","","","","","",""],
         ["","","","","","","","","",""],
         ["","","","","","","","","",""],
         ["","","","","","","","","",""],
         ["","","","","","","","","",""],
         ["","","","","","","","","",""],
         ["","","","","","","","","",""],
         ["","","","","","","","","",""],
         ["","","","","","","","","",""]]


class Canvas (object):
    """A Canvas Object"""

    def __init__(self, col, row):

        self.length = length
        self.width = width
        self.matrix = [["" for char in range(self.length)] for row in range(self.width)]

    def __repr__(self):
        """Debugger-friendly representation of canvas"""

        return f'Canvas length {self.length} x width {self.width}'

    def add(self, shape):
        """Add a shape to the canvas"""

        curr_row = shape.start_x
        curr_col = shape.start_y

        while curr_row < shape.end_x:
            
            while curr_col < shape.end_y:

                self.matrix[curr_row][curr_col] = shape.fill_char

                curr_col += 1
            
            curr_row += 1
            curr_col = shape.start_y

    def render(self):
        """Print the canvas and shapes to standard output"""

        print(self.matrix)

        

class Rectangle (object):
    """A rectangle object"""

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        """Initialize a Rectangle"""

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

    def __repr__(self):
        """Debugger-friendly representation of rectangle"""

        return f'<Rectangle start {(self.start_x, self.start_y)}, end {(self.end_x, self.end_y)} fill {self.fill_char}'

    def change_fill(self, char):
        """Change the character used to fill the Rectangle"""

        self.fill_char = char

    def translate(self, axis, num):
        """Move rectangle along an axis (right/left along x axis  or up/down along y axis)"""

        if axis == 'x':
            self.start_x += num
            self.end_x += num
        
        elif axis == 'y':
            self.start_y += num
            self.end_y += num

        else:
            print('Invalid move')



    
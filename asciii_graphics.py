class Canvas (object):
    """A Canvas Object"""

    def __init__(self, length, width):
        """Initiate a canvas based on the length and width provided. The unit of length and width is 1 character of a string."""

        self.length = length
        self.width = width
        self.matrix = [[" " for char in range(self.length)] for row in range(self.width)]
        self.shapes = []

    def __repr__(self):
        """Debugger-friendly representation of canvas"""

        return f'Canvas length {self.length} x width {self.width}'

    def add(self, shape):
        """Add a shape to the canvas"""

        self.shapes.append(shape)

    def clear(self):
        """Remove all shapes from canvas"""

        self.shapes = []

    def draw(self, shape):
        """Draw a shape onto the canvas"""

        #Define starting point of the shape - set to (0,0) if starting point is off-canvas
        curr_row = shape.start_y if shape.start_y >=0 else 0
        curr_col = shape.start_x if shape.start_x >=0 else 0

        #Loop through each row and column and fill in the shape into the matrix
        while curr_row <= shape.end_y and curr_row < self.width:
            
            while curr_col <= shape.end_x and curr_col < self.length:

                self.matrix[curr_row][curr_col] = shape.fill_char

                curr_col += 1
            
            curr_row += 1
            curr_col = shape.start_x if shape.start_x >=0 else 0


    def render(self):
        """Print the canvas and shapes to standard output"""

        #Clear canvas
        for i, row in enumerate(self.matrix):
            for j, point in enumerate(row): 
                self.matrix[i][j] = " " if point != " " else point

        #Draw shapes
        for shape in self.shapes:
            self.draw(shape)

        #Print to standard output
        for row in self.matrix:
            print("".join(row))

        
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

        return f'<Rectangle start={(self.start_x, self.start_y)}, end={(self.end_x, self.end_y)} fill=\'{self.fill_char}\'>'

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

    
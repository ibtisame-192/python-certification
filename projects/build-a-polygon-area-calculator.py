
from math import sqrt 
class Rectangle :
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
         return self.width*self.height
    def get_perimeter(self):
        return 2*(self.width + self.height)
    def get_diagonal(self):
        return (sqrt(self.width**2 + self.height**2))
    def get_picture(self):
        if self.width > 50 or self.height>50 :
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture +="*"*self.width+"\n"
        return picture

    def get_amount_inside(self,shape):
        # h : this will present how many heights it can fit
        h = self.height // shape.height
        l = self.width // shape.width
        return h*l

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
class Square(Rectangle):
    def __init__(self,length):
        self.side_length = length
        super().__init__(length,length)

    def set_width(self, side_length):
        self.width = side_length
        self.length = side_length
        self.side_length = side_length
    
    def set_height(self, side_length):
        self.width = side_length
        self.length = side_length
        self.side_length = side_length
    
    def set_side(self,side_length):
        self.width = side_length
        self.length = side_length
        self.side_length = side_length

    def get_picture(self):
        if self.width > 50 or self.height>50 :
            return "Too big for picture."
        picture = ""
        for _ in range(self.side_length):
            picture +="*"*self.side_length+"\n"
        return picture

    def __str__(self):
        return f"Square(side={self.side_length})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())




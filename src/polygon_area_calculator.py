class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        return (2*self.width) + (2*self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2)**0.5
         
    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture." 
        else:
            for i in range(self.height):
                picture += "*" * self.width
                picture += "\n"
            return picture

    def get_amount_inside(self, other_shape):
        return (self.width * self.height)//(other_shape.width * other_shape.height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_height(self, height):
        self.height = height
        self.width = height
        self.side = height

    def set_width(self, width):
        self.width = width
        self.height = width
        self.side = width

    def get_diagonal(self):
        return self.side * (2**0.5)

    def __repr__(self):
        return f"Square(side={self.side})"


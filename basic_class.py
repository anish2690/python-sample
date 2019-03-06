class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def area(self):  # better to keep self for understanding
        return self.width * self.height

    def to_string(self):
        return 'rectangle : width = {0} , height = {1}'.format(self.width, self.height)

    def __str__(self):
        return 'rectangle : width = {0} , height = {1}'.format(self.width, self.height)

    def __repr__(self):
        return 'rectangle : width = {0} , height = {1}'.format(self.width, self.height)
    # equal

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False
    #  less  than

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
print(r1.width)
print(r1.area())

print(str(r1))
print(hex(id(r1)))
print(r1.to_string())

# access string method as def
print(str(r1))

# repersentation

print(r1)


# new object

r2 = Rectangle(10, 20)

# // compare  objects
print(r1 is not r2)
print(r1 == r2)
print(r1 == 100)

# Less than __lt__


print(r1 < r2)

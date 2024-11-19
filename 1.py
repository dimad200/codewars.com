class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError
    def area(self):
        return self.__width * self.__height

bublik=Rectangle(10,20)
print(bublik.area())
a=bublik.width
print(a)
bublik.width=0
print(bublik.width)
# print(bublik.area())
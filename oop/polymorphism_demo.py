import math

class Shape:
    def area(self):
        """
        Base Class - Shape
        Method: area(self) - raises NotImplementedError
        Derived classes must override this method
        """
        raise NotImplementedError("Subclasses must implement area() method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Derived Class - Rectangle
        Inherits from Shape
        Attributes: length and width
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Overrides the area() method from Shape
        Calculates rectangle's area: length × width
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """
        Derived Class - Circle
        Inherits from Shape
        Attributes: radius
        """
        self.radius = radius
    
    def area(self):
        """
        Overrides the area() method from Shape
        Calculates circle's area: π × radius²
        """
        return math.pi * (self.radius ** 2)
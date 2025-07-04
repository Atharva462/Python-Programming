from abc import ABC, abstractmethod

# Define an interface using an abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Method to calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate the perimeter of the shape."""
        pass

# Implement the interface in a concrete class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Implement the interface in another concrete class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Instantiate objects of the concrete classes
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Demonstrate the use of the interface
def print_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

print("Rectangle Information:")
print_shape_info(rectangle)

print("\nCircle Information:")
print_shape_info(circle)

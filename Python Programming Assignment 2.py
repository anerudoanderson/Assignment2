# Question 1

# Base class
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

# Subclass Car
class Car(Vehicle):
    def start(self):
        print("Car engine roars to life 🚗")

# Subclass Bike
class Bike(Vehicle):
    def start(self):
        print("Bike engine starts with a vroom 🏍️")

# Example usage
v = Vehicle()
c = Car()
b = Bike()

v.start()
c.start()
b.start()



# Question 2

import math


class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def total_area(shapes):
    return sum(shape.area() for shape in shapes)


# Example usage
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
print("Total area:", total_area(shapes))



# Question 3

class Shape:
    def __init__(self, name="Shape"):
        self.name = name

    def calculate_area(self):
        pass  # Base does nothing


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")  # Call Shape’s constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        # Explicitly call Shape's calculate_area (though it does nothing)
        super().calculate_area()
        return self.width * self.height


# Example usage
rect = Rectangle(5, 10)
print(f"{rect.name} area:", rect.calculate_area())



# Question 4

class Dog:
    def make_sound(self):
        return "Woof! 🐶"

class Cat:
    def make_sound(self):
        return "Meow! 🐱"

def process_sound(sound_object):
    print(sound_object.make_sound())

# Example usage
dog = Dog()
cat = Cat()

process_sound(dog)
process_sound(cat)



# Question 5

from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        print("Reading text file...")

    def write(self, data):
        print(f"Writing text data: {data}")

class BinaryFileHandler(FileHandler):
    def read(self):
        print("Reading binary file...")

    def write(self, data):
        print(f"Writing binary data: {data}")

# Example usage
txt_handler = TextFileHandler()
bin_handler = BinaryFileHandler()

txt_handler.read()
txt_handler.write("Hello, world!")

bin_handler.read()
bin_handler.write(b"\x00\x01\x02")

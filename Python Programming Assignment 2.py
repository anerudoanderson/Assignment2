# Question 1: Create a simple class hierarchy involving a Vehicle class as the base class and two subclasses Car and Bike. Show how you would implement a method in the base class and override it in the subclasses.

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



# Question 2: Write a function that takes a list of different shapes (such as Circle and Rectangle) and calculates the total area of all shapes using polymorphism.

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



# Question 3: Scenario: You have a base class Shape with a method calculate_area(). You then create a derived class Rectangle that inherits from Shape. The Rectangle class needs to implement its own calculate_area() method, but you also want to utilize some initialization logic from the Shape class&#39;s constructor. Demonstrate how to use the super() function within the Rectangle class&#39;s calculate_area() method (even if the shape class area method does nothing) to call the Shape class&#39;s constructor (__init__).

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



# Question 4: Scenario: You have a function process_sound(sound_object) that expects an object with a make_sound() method. You have two classes, Dog and Cat, both of which implement the make_sound() method, but in different ways. Provide example code demonstrating how the process_sound() function can work with both Dog and Cat objects without needing to know their specific types.

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



# Question 5: Scenario: You are designing a system for handling different types of files. You want to ensure that all file handler classes implement certain essential methods, such as read() and write(). Provide example code demonstrating how to create an ABC FileHandler with abstract methods read() and write(), and how to create concrete classes like TextFileHandler and BinaryFileHandler that inherit from FileHandler.

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

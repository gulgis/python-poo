# Python Object Oriented Programming by Joe Marini course example

# Create a basic class
class Book:
    def __init__(self, title):
        self.title = title

# instances of the class
b1 = Book("DevOps Cookbook")
b2 = Book("Accelerate")

# print the class and property
print(b1)
print(b1.title)
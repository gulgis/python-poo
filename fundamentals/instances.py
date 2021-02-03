# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes

class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.year = year
        self.__secret = "secret attribute"
    #  instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount

# some book instances
b1 = Book("DevOps CookBook", "Gene kim", 509, 39.87, 2016)
b2 = Book("Accelerate", "James the fast", 765, 43.76, 2019)

# print the price of book1
print(b1.getprice())

# setting the discount
print(b2.getprice())
b2.setdiscount(0.30)
print(b2.getprice())

# properties with double underscores are hidden by the interpreter
print(b2._Book__secret)
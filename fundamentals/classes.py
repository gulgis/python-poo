# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = (
        "HARDCOVER",
        "PAPERBACK",
        "EBOOK"
    )

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None
    # create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

# access the class attribute
print("Book types: ", Book.getbooktypes())

# Create some book instances
b1 = Book("Title 1", "EBOOK")
b2 = Book("Title 2", "HARDCOVER")

# Use the static method to access a singleton object
books = Book.getbooklist()
books.append(b1)
books.append(b2)
print(books)
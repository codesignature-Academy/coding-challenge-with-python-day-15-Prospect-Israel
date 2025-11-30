class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}"

# Create book instances (outside the class)
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 218)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

# Print book descriptions
print("Book 1:")
print(book1.description())
print("\nBook 2:")
print(book2.description())

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
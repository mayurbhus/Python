import json
import random

class Book:
    def __init__(self, title, author, isbn=None):
        self.title = title
        self.author = author
        self.isbn = isbn if isbn else self.generate_isbn()

    def generate_isbn(self):
        """Generates a unique 13-digit ISBN"""
        return "978-" + "".join(str(random.randint(0, 9)) for _ in range(10))

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, isbn=None):
        book = Book(title, author, isbn)
        if book.isbn in self.books:
            print("This ISBN already exists. Try again.")
            return
        self.books[book.isbn] = book
        print(f"Added: {book}")

    def search_book(self, isbn):
        return self.books.get(isbn, "Book not found!")

    def delete_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print("Book deleted.")
        else:
            print("ISBN not found.")

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books.values():
                print(book)

    def save_books(self, filename="books.json"):
        with open(filename, "w") as file:
            json.dump({isbn: vars(book) for isbn, book in self.books.items()}, file)
        print("Library saved.")

    def load_books(self, filename="books.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.books = {isbn: Book(**info) for isbn, info in data.items()}
            print("Library loaded.")
        except FileNotFoundError:
            print("No saved data found.")

# Example Usage
library = Library()

library.load_books()
library.add_book("The Hobbit", "J.R.R. Tolkien")
library.add_book("Harry Potter", "J.K. Rowling", "9780747532743")
library.list_books()
library.save_books() 

#Using command line
book_name= " ".join(input("Enter the name of Book : ").split())
author = " ".join(input("Enter author name : ").split())
library.add_book(book_name, author)
library.save_books()

print("Your book is added.")
print("Here is the list of books : ")
library.load_books() 
library.list_books()
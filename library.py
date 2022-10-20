from book import Book


class Library():
    def __init__(self):
        """Initialize the empty book list"""
        self.books = []


    def add_title(self, title, author):
        """Add a Book object with the given title and author to the book list"""
        book_object = {}
        book_object['title'] = title
        book_object['author'] = author
        book_object = Book(title, author)
        self.books.append(book_object)

    def count_books(self):
        """Return the number of books currently in the booklist"""
        return len(self.books)
        pass

    def remove_title(self, title):
        """Remove a book from the book list"""
        for book in self.books:
            if title == book.title:
                self.books.remove(book)
        

    def is_empty(self):
        """Return True if the book list is empty, False if not"""
        return self.books == []

    def display_books(self):
        for book in self.books:
           print(f'{book.title} - {book.author}') 
           

import datetime
class Book:
    def __init__(self, title:str, author:str, isbn:str, total_copies:int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self) -> bool:
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False
        
    def return_book(self) -> bool:
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Available: {self.available_copies}/{self.total_copies}"

        
    
class Member:
    def __init__(self, id:str, name:str):
        self.id = id
        self.name = name
        self.borrowed_books = {}

    def borrow_book(self, isbn:str, borrow_date: datetime.datetime):
        self.borrowed_books[isbn] = borrow_date

    def return_book(self, isbn:str):
        if isbn in self.borrowed_books:
            del self.borrowed_books[isbn]

    def __str__(self):
        return f"Member {self.member_id}: {self.name}"
    
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book:Book):
        if book in self.books:
            sel_book = self.books[book.isbn]
            sel_book.total_copies += book.total_copies
            sel_book.available_copies += book.total_copies
        else:
            self.books[book.isbn] = book

    def register_member(self, member:Member):
        self.members[member.id] = member
    
    def search_books(self, title: str = None, author: str = None, isbn: str = None):
        res = []
        for book in self.books.values():
            if isbn and book.isbn != isbn:
                continue
            if author and author.lower() not in book.author.lower():
                continue
            if title and title.lower() not in book.title.lower():
                continue
            res.append(book)
        return res

    def borrow_book(self, member_id:str, isbn:str, borrow_date: datetime.datetime):
        if member_id not in self.members:
            print(f"member not present")
            return False

        if isbn not in self.books:
            print(f"book not present")
            return False
        
        book = self.books[isbn]
        member = self.members[member_id]

        if book.borrow():
            member.borrow_book(isbn,borrow_date)
            print(f"borrowed book successfully")
            return True
        else:
            print(f"book copy not available")
            return False
        
    def return_book(self, member_id:str, isbn:str) -> bool:
        if member_id not in self.members:
            print(f"member not present")
            return False

        if isbn not in self.books:
            print(f"book not present")
            return False
        
        book = self.books[isbn]
        member = self.members[member_id]

        if book.return_book():
            member.return_book(isbn)
            print(f"book returned successfully")
            return True
        else:
            print(f"error returning book")
            return False
        
def main():
    library = Library()

    member1 = Member("M1","Ash")
    member2 = Member("M2","Pikachu")

    book1 = Book("Fault in our stars","JK","B1",5)
    book2 = Book("My my","KJJJ","B2",15)
    book3 = Book("Joy of life","LOL","B3",2)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.register_member(member1)
    library.register_member(member2)

    search_res = library.search_books(author="JK")
    for b in search_res:
        print(b)

    
    borrow = datetime.datetime.now()
    library.borrow_book("M1","B2",borrow)

    print("\nAfter borrowing:")
    print(library.books["B2"])

    # Return the book.
    library.return_book("M1", "B2")
    print("\nAfter returning:")
    print(library.books["B2"])

if __name__ == "__main__":
    main()




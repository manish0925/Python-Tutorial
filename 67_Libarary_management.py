class Library:
    def __init__(self):
        self.no_of_book=0
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        self.no_of_book+=1
        print(f"{book} is added into Library")
    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            self.no_of_book-=1
            print(f"{book} is sucessfully remove from the library")
        else:
            print(f"{book} is not found in Library")
    def info(self):
        print(f"There are {self.no_of_book} books availbale in the Library")
        for book in self.books:
            print(book)
book1=Library()

book1.info()


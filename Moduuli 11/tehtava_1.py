class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Chief editor: {self.chief_editor}")


pub = Publication("Test Publication")
print(f"Publication: {pub.name}")

book = Book("Test Book", "Test Author", 150)
print(f"Book: {book.name} by {book.author}, {book.page_count} pages")

mag = Magazine("Test Magazine", "Test Editor")
print(f"Magazine: {mag.name}, chief editor: {mag.chief_editor}")

donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
print(f"Name: {donald_duck.name}, Chief Editor: {donald_duck.chief_editor}")

compartment = Book("Compartment No. 6", "Rosa Liksom", 192)
print(f"Name: {compartment.name}, Author: {compartment.author}, Pages: {compartment.page_count}")
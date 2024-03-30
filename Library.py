
class Library:
    books = []
    Arch = []
    b = []
    sear = []
    def __init__(self, title="", publisher="", isbn10="", isbn13="", other=None, copies=1):
        self.title = title
        self.publisher = publisher
        self.isbn10 = isbn10
        self.isbn13 = isbn13
        self.other = other
        self.copies = copies

    def loead(self,Book , arch, b):
        self.books = b
        self.Arch = arch
        self.b = Book
    def add_book(self):
        b = {}
        for x in self.books:
            if x["ISBN-10"] == self.isbn10 and x["ISBN-13"] == self.isbn13 :
                choice = input("Book already exists. Do you want to replace it or add a new copy? (replace/add): ")
                if choice.lower() == "replace":
                    self.books = [n for n in self.books if n["ISBN-10"] != self.isbn10 and n["ISBN-13"] != self.isbn13]
                    break
                elif choice.lower() == "add":
                    x["copies"] += 1
                    return
        b["Title"] = self.title
        b["publisher"] = self.publisher
        b["ISBN-10"] = self.isbn10
        b["ISBN-13"] = self.isbn13
        b["copies"] = self.copies
        b.update(self.other)
        self.books.append(b)
    def print_books(self):
        print("\n")
        for book in self.books:
            for key, value in book.items():
                print(f"{key}: {value}")
            print()
    def search_books(self):
        choice = input("What is the parameters you want to use in the search?")
        X=input("Enter its value")
        j = 0
        for i in self.books:
            if choice in i and i[choice] == X:
                print(self.books[j])
                self.sear.append(self.books[j])
            j = j+1
        choice = input("Do you want to save the information to a file(Y,F) ")
        if choice.lower() == 'y':
            file = open("Sear.txt", "w")
            for i in self.sear:
                for key, value in i.items():
                    file.write(str(key) + "  :  " + str(value) + "\n")
                file.write("\n")
            file.close()
    def Editing_book(self):
        f = 1
        choice = input("Enter the Title or ISBN-13 number or ISBN-10 number of the book you want to update: ")
        x = input(f"Enter the value of {choice}: ")
        found_in_books = False
        found_in_archive = False

        for i in self.books:
            if choice in i and i[choice] == x:
                found_in_books = True
                break

        for i in self.Arch:
            if choice in i and i[choice] == x:
                found_in_archive = True
                break

        if not found_in_books and not found_in_archive:
            print("Book not found.")
            return

        C = input("What parameters do you want to update for this book: ")
        while f:
            new_value = input("Enter the new value: ")
            Q = input("Are you sure you want to update? (Y/N): ")
            if Q == "Y":
                if found_in_books:
                    for i in self.books:
                        if choice in i and i[choice] == x:
                            i[C] = new_value
                if found_in_archive:
                    for i in self.Arch:
                        if choice in i and i[choice] == x:
                            i[C] = new_value
            elif Q == "N":
                return
            C = input(
                "Do you want to update another parameter of this book? If yes, enter the parameter; if no, enter 'No': ")
            if C == "No":
                break
    def Archiving_books(self):
        choice = input("You want to archive the book by (ISBN-13 or ISBN-10)?")
        x = input(f"f Enter the value of {choice}")
        Q = input("are you sure (Y/N)")
        if Q == "Y":
            j = 0
            for i in self.books:
                if choice in i and i[choice] == x:
                    if int(i["copies"]) > 1:
                        A = int(input("There are more than one copy of this book. How many copies do you want to archive?"))
                        if A < i["copies"]:
                            #i["copies"] -= 1
                            d = self.books[j]
                            d["copies"] = A
                            self.Arch.append(d)
                        elif A == int(i["copies"]):
                            d = self.books[j]
                            self.Arch.append(d)
                    else:
                        d = self.books[j]
                        self.Arch.append(d)

                j += 1

    def Removing_Book(self):
        choice = input("You want to delete the book by (ISBN-13 or ISBN-10)?")
        x = input(f"f Enter the value of {choice}")
        Q = input("Are you sure you want to delete it (Y/N)")
        if Q == "Y":
            j = 0
            for i in self.Arch:
                if choice in i and i[choice] == x:
                    if int(i["copies"]) > 1:
                        A = int(input("There are more than one copy of this book. How many copies do you want to delete?"))
                        if A < int(i["copies"]):
                            i["copies"] -= 1
                        elif A == int(i["copies"]):
                            del self.Arch[j]
                    else:
                        del self.Arch[j]

                j += 1
    def reports(self):
        all_Books = 0
        a_Booka_Arc = 0
        num_Book = 0
        for i in self.books:
            all_Books += i["copies"]
        print(f"number of  books are in the LMS {all_Books}")
        d_Book = len(self.books)
        print(f"number of  different books are offered in the LMS {d_Book}")
        for i in self.Arch:
            a_Booka_Arc += i["copies"]
        print(f"number of books archived in the LMS {a_Booka_Arc}")
        Q = int(input("Please provide the desired year, and I will inform you of the number of books published thereafter."))
        grouped_publisher = {}
        for book in self.books:
            if "publisher" in book:
                name = book["publisher"]
                if name in grouped_publisher:
                    grouped_publisher[name].append(book)  # Add the book to the existing group
                else:
                    grouped_publisher[name] = [book]  # Create a new group with the book

        # Print the information of each group
        for name, group in grouped_publisher.items():
            print(f"Publisher: {name}")
            for book in group:
                print(f"Title: {book['Title']}, ISBN-10: {book['ISBN-10']}, ISBN-13: {book['ISBN-13']}")
            print()

        grouped_book1 = {}
        for book in self.books:
            if 'Year' in book:
                name = book["Year"]
                # Check if the name exists as a key in the dictionary
                if name in grouped_book1:
                    grouped_book1[name].append(book)  # Add the book to the existing group
                else:
                    grouped_book1[name] = [book]  # Create a new group with the book

        # Print the information of each group
        for name, group in grouped_book1.items():
            print(f"Year: {name}")
            for book in group:
                print(f"Title: {book['Title']}, ISBN-10: {book['ISBN-10']}, ISBN-13: {book['ISBN-13']}")
            print()

    def save_file(self):
        file = open("Arch.txt", "w")
        for i in self.Arch:
            for key, value in i.items():
                file.write(str(key) + "  :  " + str(value) + "\n")
            file.write("\n")
        file.close()
        n=0
        for j in self.books:
            for i in self.Arch:
                if i["ISBN-10"] == j["ISBN-10"]:
                    if i["copies"] == j["copies"]:
                        del self.books[n]
                    elif i["copies"] != j["copies"]:
                        j["copies"] = int(j["copies"]) - int(i["copies"])
            n += 1
        file = open("LMS.txt", "w")
        for i in self.books:
            for key, value in i.items():
                file.write(str(key) + "  :  " + str(value) + "\n")
            file.write("\n")
        file.close()
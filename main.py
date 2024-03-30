# Import the Library class from the Library module
from Library import Library
def load_Book_Arch(books):
    try:
        # Open the Arch.txt file in read mode
        with open('Arch.txt', 'r') as file:
            lines = file.readlines()
        current_book = {} # Dictionary to store Basic information for the book
        current1_book = {} # Dictionary to store additional information for the current book
        for line in lines:
            line = line.strip()
            if line:
                key, value = line.split(' : ')
                if key.strip() == "Title" or key.strip() == "Publisher":
                    current_book[key.strip()] = value.strip()
                elif key.strip() == "ISBN-10":
                    current_book[key.strip()] = value.strip()
                elif key.strip() == "ISBN-13":
                    current_book[key.strip()] = value.strip()
                else:
                    current1_book[key.strip()] = value.strip()
            else:
                current_book.update(current1_book)
                for i in books:
                    if i["ISBN-10"] == current_book["ISBN-10"]:
                        i["copies"] = int(i["copies"] ) + int(current_book["copies"])
                        break
                else:
                    books.append(current_book)
                current_book = {}
                current1_book = {}

        # Append the last book dictionary if there's any
        if current_book:
            current_book.update(current1_book)
            for i in books:
                if i["ISBN-10"] == current_book["ISBN-10"]:
                    print(i["ISBN-10"])
                    i["copies"] = int(i["copies"]) + int(current_book["copies"])
                    break
            books.append(current_book)


    except FileNotFoundError:
        print(f"Error: File Arc.txt not found.")
    except Exception as e:
        print(f"Error: An error occurred while loading books from the file: {e}")
    return books
def load_books_from_file():
    try:
        #Book after book is read and cut according to:
        with open('LMS.txt', 'r') as file:
            lines = file.readlines()
            books = []
        current_book = {} # Dictionary to store Basic information for the book
        current1_book = {}# Dictionary to store additional information for the current book
        for line in lines:
            line = line.strip()
            if line:
                key, value = line.split(' : ')
                if key.strip() == "Title" or key.strip() == "Publisher":
                    current_book[key.strip()] = value.strip()
                elif key.strip() == "ISBN-10":
                    current_book[key.strip()] = value.strip()
                elif key.strip() == "ISBN-13":
                    current_book[key.strip()] = value.strip()
                else:
                    current1_book[key.strip()] = value.strip()
            else:
                # If "copies" key is not present, set its value to 1
                if "copies" not in current1_book:
                    current1_book["copies"] = 1
                # Update the current book dictionary with the additional information
                current_book.update(current1_book)

                # Append the current book to the list of books
                books.append(current_book)

                # Reset the dictionaries for the next book
                current_book = {}
                current1_book = {}

        # Append the last book dictionary if there's any
        if current_book:
            # If "copies" key is not present, set its value to 1
            if "copies" not in current1_book:
                current1_book["copies"] = 1
            current_book.update(current1_book)
            books.append(current_book)


    except FileNotFoundError:
        print(f"Error: File LMS.txt not found.")
    except Exception as e:
        print(f"Error: An error occurred while loading books from the file: {e}")
    return books
def read_file (Book,Arc,n):
    file_name = input("Enter the name of the file containing the information about the new books: ")
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        current_book = {}
        b0 = ""
        b1 = ""
        b2 = 0
        b3 = 0
        copies = 1
        for line in lines:
            line = line.strip()
            if line:
                key, value = line.split(' : ')
                if key.strip() == "Title":
                    b0 = value.strip()
                elif key.strip() == "Publisher":
                    b1 = value.strip()
                elif key.strip() == "ISBN-10":
                    b2 = value.strip()
                elif key.strip() == "ISBN-13":
                    b3 = value.strip()
                else:
                    current_book[key.strip()] = value.strip()

            else:
                b = Library(b0, b1, b2, b3, current_book, copies)
                b.loead(Book,Arc ,n)
                b.add_book()
                current_book = {}
        # Append the last book dictionary if there's any
        if current_book:
            B = Library(b0, b1, b2, b3, current_book, copies)
            B.loead(Book,Arc ,n)
            B.add_book()




    except FileNotFoundError:
        print(f"Error: File LMS.txt not found.")
    except Exception as e:
        print(f"Error: An error occurred while loading books from the file: {e}")
# Function to load books from the Arch.txt file
def load_Arch():
    try:
        #Book after book is read and cut according to:
        with open('Arch.txt', 'r') as file:
            lines = file.readlines()
            books = []
        current_book = {}
        current1_book = {}
        for line in lines:
            line = line.strip()
            if line:
                key, value = line.split(' : ')
                if key.strip() == "Title" or key.strip() == "Publisher":
                    current_book[key.strip()] = value.strip()
                elif key.strip() == "ISBN-10":
                    current_book[key.strip()] = value.strip()
                elif key.strip() == "ISBN-13":
                    current_book[key.strip()] = value.strip()
                else:
                    current1_book[key.strip()] = value.strip()
            else:
                if "copies" not in current1_book:
                    current1_book["copies"] = 1
                current_book.update(current1_book)
                books.append(current_book)
                current_book = {}
                current1_book = {}

        # Append the last book dictionary if there's any
        if current_book:
            if "copies" not in current1_book:
                current1_book["copies"] = 1
            current_book.update(current1_book)
            books.append(current_book)


    except FileNotFoundError:
        print(f"Error: File LMS.txt not found.")
    except Exception as e:
        print(f"Error: An error occurred while loading books from the file: {e}")
    return books
def main():
    flag = 1
    n = Library()
    book = load_books_from_file()  # Load books from LMS.txt file
    Arch = load_Arch()  # Load books from Arch.txt file
    b = load_Book_Arch(book)  # Load books from Arch.txt and update copies in LMS.txt
    n.loead(book, Arch, b)  # Load books into the Library object

    while(flag):
        print("""
        1. Adding new books to the library collection
        2. Searching for books within the library collection
        3. Editing the information of existing books
        4. Archiving books
        5. Removing books from the LMS
        6. Generating reports about the books available in the LMS
        7. Exit
        """)

        choice = int(input("Enter the choice: "))
        if choice == 1:
            read_file(book, Arch, b)  # Read books from a file and add them to the library
            n.print_books()
        elif choice == 2:
            n.search_books()  # Search for books in the library
        elif choice == 3:
            n.Editing_book()  # Edit the information of existing books
        elif choice == 4:
            n.Archiving_books()  # Archive books
        elif choice == 5:
            n.Removing_Book()  # Remove books from the LMS
        elif choice == 6:
            n.reports()  # Generate reports about the books
            n.print_books()
        elif choice == 7:
            n.save_file()
            break
        else:
            print("Invalid input. Please enter a valid choice.")
            continue


if __name__ == "__main__":
    main()
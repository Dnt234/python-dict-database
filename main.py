library = {
    "1984": {"Author": "George Orwell", "Year Published": "1949", "Genre": "Dystopian"},
    "To Kill a Mockingbird": {"Author": "Harper Lee", "Year Published": "1960", "Genre": "Fiction"},
    "The Great Gatsby": {"Author": "F. Scott Fitzgerald", "Year Published": "1925", "Genre": "Tragedy"},
    "Moby Dick": {"Author": "Herman Melville", "Year Published": "1851", "Genre": "Adventure"}
}


def display_books():
    for book, details in library.items():
        print(f"Name: {book}, Author: {details['Author']}, Year Published: {details['Year Published']}, Genre: {details['Genre']}")

def update_book():
    book = input("Which book would you like to update? ")
    library[book]["Author"] = input("What is the new author? ")
    library[book]["Year Published"] = input("What is the new year published? ")
    library[book]["Genre"] = input("What is the new genre? ")
    print("The book has been updated.")

def add_book():
    book = input("What is the name of the book? ")
    library[book] = {"Author": input("What is the author? "), "Year Published": input("What is the year published? "), "Genre": input("What is the genre? ")}
    print("The book has been added.")

def delete_book():
    book = input("Which book would you like to delete? ")
    del library[book]
    print("The book has been deleted.")

def main():
    while True:
        print("What would you like to do?")
        print("1. Display books")
        print("2. Update book")
        print("3. Add book")
        print("4. Delete book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_books()
        elif choice == "2":
            display_books()
            update_book()
        elif choice == "3":
            add_book()
        elif choice == "4":
            display_books()
            delete_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
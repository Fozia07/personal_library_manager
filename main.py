import json
class BookCollection:
  def __init__(self):
    """ Intialize a new book list with an empty list and setup the file storage"""

    self.book_list =[]
    self.storage_file ="book_data.json"
    self.read_from_file()

  def read_from_file(self):
    """Load save book from a json file into memory .
    if the file dosnt exist or is corrupted, start with an empty collection"""   

    try:
         with open(self.storage_file, "r") as file:
            self.book_list =json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        self.book_list =[]

  def save_to_file(self):
    """store the current book collectin into Json file for permenant storage"""
    with open(self.storage_file,"w") as file:
        json.dump(self.book_list,file, indent=4)

  def create_new_book(self):
    """Add a new book to the collection by gathering input from the user"""
    book_title =input("Enter the title of the book: ")
    book_author = input("Enter the author name: ")
    publication =input("Enter publication year: ")
    book_genre=input("Enter the genre of the book: ")
    is_book_read=(input("Have yo read the book? yes/no").strip().lower() == "yes" )

    new_book = {
       "title" : book_title,
       "author" :book_author,
       "publication": publication,
       "genre" :book_genre,
       "read" :is_book_read,    
    }

    self.book_list.append(new_book)
    self.save_to_file()
    print("successfully added book")

  def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return
        print("Book not found!\n")

  def find_book(self):
        """Search for books in the collection by title or author name."""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]

        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("No matching books found.\n")    



  def start_application(self):
   """start application and give a attractive interface to user"""
   while True:
        print(" ****welcome to my personal manager library ****")
        print("1 :add a new book")
        print("2 :delete a book")
        print("3 :search the book")
        print("4 : exit")
        user_choice = input("Please choose an option (1-4): ")

        if user_choice == "1":
          self.create_new_book()
        elif user_choice == "2":
           self.delete_book()
        elif user_choice == "3":
             self.find_book()
        elif user_choice == "4":
             self.save_to_file()
             print("Thank you for using Book Collection Manager. Goodbye!")
             break
        else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
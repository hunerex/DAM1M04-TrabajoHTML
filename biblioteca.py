import pickle

# Save books data
def save(books):
    """
    Save books data structure
    """
    try:
        with open('books.pkl', 'wb') as file:
            pickle.dump(books, file)
        return True
    except Exception as e:
        print(f"Error opening books.pkl:", {e})
        return False

# Load books data
def load():
    """
    Load books data structure
    """
    try:
        with open('books.pkl', 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Error opening books.pkl:", {e})
        return -1

def add_book():

def delete_book(book_id):

def find_books_by_title(query):

def make_menu(options):

# Books data structure
Books = [
    {
        "book_id": 1,
        "title": "A Game of Thrones",
        "year_published": 1996,
        "pages": 694,
        "isbn": "978-0553103540",
        "user_id": 0
    }
]

menu_options = ["Load data", "Save data", "Add a book", "Delete a book", "Find books"]

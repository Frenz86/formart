import json
from typing import List, Optional
from pydantic import BaseModel


class Author(BaseModel):
    name: str
    verified: bool

class Book(BaseModel):
    """Represents a book with that you can read from a JSON file."""
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str] # not all books have
    isbn_13: Optional[str] # not all books have
    subtitle: Optional[str] # not all books have
    #author2: Optional[Author] # Depend on Author

def main() -> None:
    """Main function."""

    # Read data from a JSON file
    with open("./data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        # print(books)
        print(books[0])
        #print(books[0].dict(exclude={"price"}))
        #print(books[0].dict(exclude={"price","isbn_10","isbn_13"}))
        # print(books[1].copy())

if __name__ == "__main__":
    main()
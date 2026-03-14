from fastapi import FastAPI, HTTPException
from database import books
from schemas import Book, BookCreate

app = FastAPI()

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if(book_id == book["id"]):
            return book
    
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books")
def create_book(book: BookCreate):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author
    }
    books.append(new_book)
    return new_book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate):
    for b in books:
        if b["id"] == book_id:
            b["title"] = book.title
            b["author"] = book.author
            return b
    
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(i)
            return {"message": "Book deleted"}
    
    raise HTTPException(status_code=404, detail="Book not found")

    

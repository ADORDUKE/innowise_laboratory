from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import engine, get_db
import crud
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book API")

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books/", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, new_data: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id, new_data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_book(db, book_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}

@app.get("/books/search/", response_model=list[schemas.Book])
def search(title: str = None, author: str = None, year: int = None, db: Session = Depends(get_db)):
    return crud.search_books(db, title, author, year)
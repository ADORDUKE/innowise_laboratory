from sqlalchemy.orm import Session
from models import Book
import schemas

def create_book(db: Session, book: schemas.BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, book_data: schemas.BookUpdate):
    db_book = get_book(db, book_id)
    if not db_book:
        return None

    for field, value in book_data.dict(exclude_unset=True).items():
        setattr(db_book, field, value)

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return True

def search_books(db: Session, title=None, author=None, year=None):
    query = db.query(Book)

    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if year:
        query = query.filter(Book.year == year)

    return query.all()


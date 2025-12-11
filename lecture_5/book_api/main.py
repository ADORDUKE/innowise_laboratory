from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import engine, get_db
import crud
import schemas


# Создаём таблицы в базе, если их ещё нет
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book API")


@app.post(
    "/books/",
    response_model=schemas.Book,
    description="Add a new book"
)
def create_book(
    book: schemas.BookCreate,
    db: Session = Depends(get_db)
) -> schemas.Book:
    """
    Создаёт новую книгу.

    Args:
        book (schemas.BookCreate): Данные для создания книги.
        db (Session): Сессия базы данных (DI).

    Returns:
        schemas.Book: Созданная книга.
    """
    return crud.create_book(db, book)


@app.get(
    "/books/",
    response_model=List[schemas.Book],
    description="Get all books"
)
def read_books(db: Session = Depends(get_db)) -> List[schemas.Book]:
    """
    Возвращает список всех книг.

    Args:
        db (Session): Сессия базы данных.

    Returns:
        List[schemas.Book]: Список книг.
    """
    return crud.get_books(db)


@app.delete(
    "/books/{book_id}",
    description="Delete a book by ID"
)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
) -> dict:
    """
    Удаляет книгу по ID.

    Args:
        book_id (int): ID книги.
        db (Session): Сессия базы данных.

    Raises:
        HTTPException: Если книга не найдена.

    Returns:
        dict: Сообщение об успешном удалении.
    """
    ok = crud.delete_book(db, book_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}


@app.put(
    "/books/{book_id}",
    response_model=schemas.Book,
    description="Update book details"
)
def update_book(
    book_id: int,
    new_data: schemas.BookUpdate,
    db: Session = Depends(get_db)
) -> schemas.Book:
    """
    Обновляет данные книги.

    Args:
        book_id (int): ID книги.
        new_data (schemas.BookUpdate): Изменённые данные.
        db (Session): Сессия базы данных.

    Raises:
        HTTPException: Если книга не найдена.

    Returns:
        schemas.Book: Обновлённая книга.
    """
    book = crud.update_book(db, book_id, new_data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.get(
    "/books/search/",
    response_model=List[schemas.Book],
    description="Search books by title, author, or year"
)
def search(
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[int] = None,
    db: Session = Depends(get_db)
) -> List[schemas.Book]:
    """
    Выполняет поиск книг по названию, автору или году.

    Args:
        title (Optional[str]): Подстрока в названии.
        author (Optional[str]): Подстрока в имени автора.
        year (Optional[int]): Год издания.
        db (Session): Сессия базы данных.

    Returns:
        List[schemas.Book]: Список найденных книг.
    """
    return crud.search_books(db, title, author, year)

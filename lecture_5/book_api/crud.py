from typing import List, Optional, Union
from sqlalchemy.orm import Session
from models import Book
import schemas


def create_book(db: Session, book: schemas.BookCreate) -> Book:
    """
    Создаёт новую книгу в базе данных.

    Args:
        db (Session): Сессия SQLAlchemy.
        book (schemas.BookCreate): Входные данные для создания книги.

    Returns:
        Book: Сохранённая книга.
    """
    # Создаем ORM-объект на основе pydantic-схемы
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)  # Обновляем после вставки
    return db_book


def get_books(db: Session) -> List[Book]:
    """
    Возвращает список всех книг.

    Args:
        db (Session): Сессия SQLAlchemy.

    Returns:
        List[Book]: Список книг.
    """
    return db.query(Book).all()


def get_book(db: Session, book_id: int) -> Optional[Book]:
    """
    Возвращает книгу по ID.

    Args:
        db (Session): Сессия SQLAlchemy.
        book_id (int): Идентификатор книги.

    Returns:
        Optional[Book]: Книга или None, если не найдена.
    """
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(
    db: Session,
    book_id: int,
    book_data: schemas.BookUpdate
) -> Optional[Book]:
    """
    Обновляет данные существующей книги.

    Args:
        db (Session): Сессия SQLAlchemy.
        book_id (int): Идентификатор книги.
        book_data (schemas.BookUpdate): Поля для обновления (только изменённые).

    Returns:
        Optional[Book]: Обновлённая книга или None, если книга не найдена.
    """
    db_book = get_book(db, book_id)
    if not db_book:
        return None

    # Обновляем только те поля, что пользователь прислал
    for field, value in book_data.dict(exclude_unset=True).items():
        setattr(db_book, field, value)

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int) -> bool:
    """
    Удаляет книгу по ID.

    Args:
        db (Session): Сессия SQLAlchemy.
        book_id (int): Идентификатор книги.

    Returns:
        bool: True если удалена, False если книга не найдена.
    """
    db_book = get_book(db, book_id)
    if not db_book:
        return False

    db.delete(db_book)
    db.commit()
    return True


def search_books(
    db: Session,
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[int] = None
) -> List[Book]:
    """
    Поиск книг по фильтрам.

    Args:
        db (Session): Сессия SQLAlchemy.
        title (Optional[str]): Подстрока в названии.
        author (Optional[str]): Подстрока в имени автора.
        year (Optional[int]): Год издания.

    Returns:
        List[Book]: Книги, подходящие под фильтры.
    """
    query = db.query(Book)

    # Добавляем фильтры только если параметры переданы
    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if year:
        query = query.filter(Book.year == year)

    return query.all()

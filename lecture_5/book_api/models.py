from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    """
    Модель ORM для таблицы `books`.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания.
    """

    __tablename__ = "books"

    # Уникальный ID книги (Primary Key)
    id: int = Column(Integer, primary_key=True, index=True)

    # Название книги
    title: str = Column(String, nullable=False)

    # Автор книги
    author: str = Column(String, nullable=False)

    # Год издания
    year: int = Column(Integer, nullable=False)

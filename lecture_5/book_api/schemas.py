from pydantic import BaseModel, Field
from typing import Optional


class BookBase(BaseModel):
    """
    Базовая схема книги.

    Используется для общих полей, разделяемых между моделями:
    - title
    - author
    - year
    """

    title: str = Field(
        ...,
        min_length=1,
        description="Название книги (не может быть пустым)"
    )
    author: str = Field(
        ...,
        min_length=1,
        description="Автор книги (не может быть пустым)"
    )
    year: Optional[int] = Field(
        None,
        description="Год издания книги (необязательное поле)"
    )


class BookCreate(BookBase):
    """
    Схема для создания книги.

    Наследует все поля из BookBase без изменений.
    """
    pass


class BookUpdate(BaseModel):
    """
    Схема для обновления книги.

    Все поля необязательные, чтобы можно было менять частично.
    """

    title: Optional[str] = Field(
        None,
        min_length=1,
        description="Новое название книги"
    )
    author: Optional[str] = Field(
        None,
        min_length=1,
        description="Новый автор книги"
    )
    year: Optional[int] = Field(
        None,
        description="Новый год издания"
    )


class Book(BookBase):
    """
    Схема возврата книги.

    Используется в response_model FastAPI.
    """

    id: int = Field(
        ...,
        description="Уникальный идентификатор книги"
    )

    class Config:
        orm_mode = True  # Позволяет работать с ORM объектами SQLAlchemy

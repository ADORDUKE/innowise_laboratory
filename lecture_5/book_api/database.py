from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

DATABASE_URL = "sqlite:///books.db"


class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей SQLAlchemy.

    Используется как основа для декларативного стиля описания ORM-моделей.
    """
    pass


# Создаём движок для подключения к базе данных
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # Требуется для SQLite в многопоточности
)

# Фабрика сессий для работы с БД
SessionLocal = sessionmaker(bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    Генератор, возвращающий сессию базы данных.

    Используется как dependency в FastAPI:

        def endpoint(db: Session = Depends(get_db)):
            ...

    Yields:
        Session: Активная сессия SQLAlchemy.

    Ensures:
        Сессия будет закрыта после выполнения.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        # Закрываем сессию чтобы избежать утечек соединений
        db.close()

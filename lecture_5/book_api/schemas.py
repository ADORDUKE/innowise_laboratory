from pydantic import BaseModel,Field
from typing import Optional

class BookBase(BaseModel):
    title: str =Field(..., min_length=1)
    author: str =Field(..., min_length=1)
    year: Optional[int] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    year: Optional[int]

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
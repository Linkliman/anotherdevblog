# Define the request models
from pydantic import BaseModel
from datetime import datetime
from typing import List

class ArticleCreate(BaseModel):
    title: str
    summary: str
    datetime: datetime
    author: str
    content: str
    tags: List[str]

class ArticleRead(BaseModel):
    id: int
    title: str
    summary: str
    datetime: datetime
    author: str
    tags: List[str]

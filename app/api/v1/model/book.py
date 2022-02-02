from typing import Dict

from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str = Field(alias="Title")
    author: str = Field(alias="Author")
    category: str = Field(alias="Category")
    formats: Dict[str, str] = Field(alias="Formats")
from typing import Optional, List
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Column, JSON


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True

        schema_extra = {
            "example": {
                "title": "FastAPI BookLaunch",
                "image": "https://linktoimage.com/image.png",
                "description": "Discussing about FastAPI",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }



class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI BookLaunch",
                "image": "https://linktoimage.com/image.png",
                "description": "Discussing about FastAPI",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class MovieFields(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    genre: str = Field(min_length=1, max_length=40)
    release_year: int = Field(ge=1888, le=2100)
    rating: float = Field(ge=0, le=10)
    watched: bool = False
    poster_url: Optional[str] = None

    @field_validator("title", "genre")
    @classmethod
    def trim_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("This field cannot be blank")
        return value


class Movie(MovieFields):
    id: int


class WatchedUpdate(BaseModel):
    watched: bool

from typing import Optional, TypedDict


class MovieFields(TypedDict):
    title: str
    genre: str
    release_year: int
    rating: float
    watched: bool
    poster_url: Optional[str]


class MovieRecord(MovieFields):
    id: int

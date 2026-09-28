from typing import Optional

from fastapi import FastAPI, HTTPException, Query, Response, status
from fastapi.middleware.cors import CORSMiddleware
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


# This sample list is kept in memory so the API stays easy to learn.
movies: list[dict] = [
    {
        "id": 1,
        "title": "Inception",
        "genre": "Sci-Fi",
        "release_year": 2010,
        "rating": 8.8,
        "watched": True,
        "poster_url": "https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
    },
    {
        "id": 2,
        "title": "Parasite",
        "genre": "Thriller",
        "release_year": 2019,
        "rating": 8.5,
        "watched": False,
        "poster_url": "https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
    },
    {
        "id": 3,
        "title": "Spider-Man: Across the Spider-Verse",
        "genre": "Animation",
        "release_year": 2023,
        "rating": 8.7,
        "watched": True,
        "poster_url": "https://image.tmdb.org/t/p/w500/8Vt6mWEReuy4Of61Lnj5Xj704m8.jpg",
    },
    {
        "id": 4,
        "title": "Whiplash",
        "genre": "Drama",
        "release_year": 2014,
        "rating": 8.5,
        "watched": False,
        "poster_url": "https://image.tmdb.org/t/p/w500/7fn624j5lj3xTme2SgiLCeuedmO.jpg",
    },
    {
        "id": 5,
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "release_year": 2014,
        "rating": 8.7,
        "watched": True,
        "poster_url": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
    },
    {
        "id": 6,
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "release_year": 1994,
        "rating": 9.3,
        "watched": False,
        "poster_url": "https://image.tmdb.org/t/p/w500/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
    },
    {
        "id": 7,
        "title": "The Godfather",
        "genre": "Crime",
        "release_year": 1972,
        "rating": 9.2,
        "watched": True,
        "poster_url": None,
    },
    {
        "id": 8,
        "title": "The Grand Budapest Hotel",
        "genre": "Comedy",
        "release_year": 2014,
        "rating": 8.1,
        "watched": False,
        "poster_url": "https://image.tmdb.org/t/p/w500/eWdyYQreja6JGCzqHWXpWHDrrPo.jpg",
    },
    {
        "id": 9,
        "title": "Mad Max: Fury Road",
        "genre": "Action",
        "release_year": 2015,
        "rating": 8.1,
        "watched": True,
        "poster_url": "https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg",
    },
    {
        "id": 10,
        "title": "Spirited Away",
        "genre": "Animation",
        "release_year": 2001,
        "rating": 8.6,
        "watched": False,
        "poster_url": "https://image.tmdb.org/t/p/w500/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
    },
    {
        "id": 11,
        "title": "The Truman Show",
        "genre": "Comedy",
        "release_year": 1998,
        "rating": 8.2,
        "watched": True,
        "poster_url": "https://image.tmdb.org/t/p/w500/vuza0WqY239yBXOadKlGwJsZJFE.jpg",
    },
    {
        "id": 12,
        "title": "Coco",
        "genre": "Animation",
        "release_year": 2017,
        "rating": 8.4,
        "watched": False,
        "poster_url": "https://image.tmdb.org/t/p/w500/gGEsBPAijhVUFoiNpgZXqRVWJt2.jpg",
    },
    {
        "id": 13,
        "title": "Get Out",
        "genre": "Horror",
        "release_year": 2017,
        "rating": 7.8,
        "watched": True,
        "poster_url": "https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg",
    },
    {
        "id": 14,
        "title": "La La Land",
        "genre": "Musical",
        "release_year": 2016,
        "rating": 8.0,
        "watched": False,
        "poster_url": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg",
    },
    {
        "id": 15,
        "title": "The Dark Knight",
        "genre": "Action",
        "release_year": 2008,
        "rating": 9.0,
        "watched": True,
        "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
    },
    {
        "id": 16,
        "title": "3 Idiots",
        "genre": "Comedy",
        "release_year": 2009,
        "rating": 8.4,
        "watched": True,
        "poster_url": None,
    },
    {
        "id": 17,
        "title": "Dangal",
        "genre": "Drama",
        "release_year": 2016,
        "rating": 8.3,
        "watched": False,
        "poster_url": None,
    },
    {
        "id": 18,
        "title": "Baahubali: The Beginning",
        "genre": "Action",
        "release_year": 2015,
        "rating": 8.0,
        "watched": True,
        "poster_url": None,
    },
    {
        "id": 19,
        "title": "Baahubali 2: The Conclusion",
        "genre": "Action",
        "release_year": 2017,
        "rating": 8.2,
        "watched": False,
        "poster_url": None,
    },
    {
        "id": 20,
        "title": "RRR",
        "genre": "Action",
        "release_year": 2022,
        "rating": 7.8,
        "watched": True,
        "poster_url": None,
    },
    {
        "id": 21,
        "title": "Drishyam",
        "genre": "Thriller",
        "release_year": 2013,
        "rating": 8.3,
        "watched": False,
        "poster_url": None,
    },
    {
        "id": 22,
        "title": "Jai Bhim",
        "genre": "Drama",
        "release_year": 2021,
        "rating": 8.7,
        "watched": True,
        "poster_url": None,
    },
    {
        "id": 23,
        "title": "K.G.F: Chapter 1",
        "genre": "Action",
        "release_year": 2018,
        "rating": 8.2,
        "watched": False,
        "poster_url": None,
    },
    {
        "id": 24,
        "title": "Sita Ramam",
        "genre": "Romance",
        "release_year": 2022,
        "rating": 8.5,
        "watched": True,
        "poster_url": None,
    },
    {
        "id": 25,
        "title": "Premam",
        "genre": "Romance",
        "release_year": 2015,
        "rating": 8.3,
        "watched": False,
        "poster_url": None,
    },
]
next_movie_id = 26

app = FastAPI(title="Movie Collection API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/genres", response_model=list[str])
def get_genres():
    return sorted({movie["genre"] for movie in movies})


@app.get("/movies", response_model=list[Movie])
def get_movies(
    search: str = Query(default="", max_length=120),
    genre: str = Query(default=""),
):
    results = movies

    if search:
        search_text = search.casefold()
        results = [
            movie
            for movie in results
            if search_text in movie["title"].casefold()
        ]

    if genre:
        results = [
            movie for movie in results if movie["genre"].casefold() == genre.casefold()
        ]

    return results


@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@app.post("/movies", response_model=Movie, status_code=status.HTTP_201_CREATED)
def create_movie(movie_fields: MovieFields):
    global next_movie_id

    movie = {"id": next_movie_id, **movie_fields.model_dump()}
    movies.append(movie)
    next_movie_id += 1
    return movie


@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie_fields: MovieFields):
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(movie_fields.model_dump())
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@app.patch("/movies/{movie_id}/watched", response_model=Movie)
def update_watched_status(movie_id: int, update: WatchedUpdate):
    for movie in movies:
        if movie["id"] == movie_id:
            movie["watched"] = update.watched
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@app.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail="Movie not found")
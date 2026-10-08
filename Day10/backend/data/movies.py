import json
from pathlib import Path

from ..models.movie import MovieFields, MovieRecord

DEFAULT_MOVIES: list[MovieRecord] = [
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

DATA_FILE = Path(__file__).resolve().parent.parent / "movies.json"


def save_movies() -> None:
    DATA_FILE.write_text(json.dumps(movies, indent=2), encoding="utf-8")


def _load_movies() -> list[MovieRecord]:
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))

    movies = [movie.copy() for movie in DEFAULT_MOVIES]
    DATA_FILE.write_text(json.dumps(movies, indent=2), encoding="utf-8")
    return movies


movies = _load_movies()
_next_movie_id = max((movie["id"] for movie in movies), default=0) + 1


def get_all_movies() -> list[MovieRecord]:
    return movies


def get_movie_by_id(movie_id: int) -> MovieRecord | None:
    return next((movie for movie in movies if movie["id"] == movie_id), None)


def add_movie(fields: MovieFields) -> MovieRecord:
    global _next_movie_id

    movie: MovieRecord = {"id": _next_movie_id, **fields}
    movies.append(movie)
    _next_movie_id += 1
    save_movies()
    return movie


def update_movie(movie_id: int, fields: MovieFields) -> MovieRecord | None:
    movie = get_movie_by_id(movie_id)
    if movie is None:
        return None

    movie.update(fields)
    save_movies()
    return movie


def update_watched_status(movie_id: int, watched: bool) -> MovieRecord | None:
    movie = get_movie_by_id(movie_id)
    if movie is None:
        return None

    movie["watched"] = watched
    save_movies()
    return movie


def delete_movie(movie_id: int) -> bool:
    movie = get_movie_by_id(movie_id)
    if movie is None:
        return False

    movies.remove(movie)
    save_movies()
    return True

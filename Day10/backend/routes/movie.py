from fastapi import APIRouter, HTTPException, Query, Response, status

from ..data import movies as movie_data
from ..models.movie import MovieFields as MovieFieldsData, MovieRecord
from ..schemas.movie import Movie, MovieFields, WatchedUpdate

router = APIRouter()


def _movie_fields_data(fields: MovieFields) -> MovieFieldsData:
    return MovieFieldsData(
        title=fields.title,
        genre=fields.genre,
        release_year=fields.release_year,
        rating=fields.rating,
        watched=fields.watched,
        poster_url=fields.poster_url,
    )


@router.get("/genres", response_model=list[str])
def get_genres() -> list[str]:
    return sorted({movie["genre"] for movie in movie_data.get_all_movies()})


@router.get("/movies", response_model=list[Movie])
def get_movies(
    search: str = Query(default="", max_length=120),
    genre: str = Query(default=""),
) -> list[MovieRecord]:
    results = movie_data.get_all_movies()

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


@router.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int) -> MovieRecord:
    movie = movie_data.get_movie_by_id(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.post("/movies", response_model=Movie, status_code=status.HTTP_201_CREATED)
def create_movie(movie_fields: MovieFields) -> MovieRecord:
    return movie_data.add_movie(_movie_fields_data(movie_fields))


@router.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie_fields: MovieFields) -> MovieRecord:
    movie = movie_data.update_movie(movie_id, _movie_fields_data(movie_fields))
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.patch("/movies/{movie_id}/watched", response_model=Movie)
def update_watched_status(movie_id: int, update: WatchedUpdate) -> MovieRecord:
    movie = movie_data.update_watched_status(movie_id, update.watched)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int) -> Response:
    if not movie_data.delete_movie(movie_id):
        raise HTTPException(status_code=404, detail="Movie not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

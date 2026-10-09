from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.db_models import MovieDB
from ..schemas.movie import Movie, MovieFields, WatchedUpdate

router = APIRouter()


@router.get("/genres", response_model=list[str])
def get_genres(db: Session = Depends(get_db)) -> list[str]:
    statement = select(MovieDB.genre).distinct().order_by(MovieDB.genre)
    return list(db.scalars(statement).all())


@router.get("/movies", response_model=list[Movie])
def get_movies(
    search: str = Query(default="", max_length=120),
    genre: str = Query(default=""),
    db: Session = Depends(get_db),
) -> list[MovieDB]:
    statement = select(MovieDB).order_by(MovieDB.id)

    if search:
        statement = statement.where(MovieDB.title.ilike(f"%{search}%"))

    if genre:
        statement = statement.where(MovieDB.genre.ilike(genre))

    return list(db.scalars(statement).all())


@router.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int, db: Session = Depends(get_db)) -> MovieDB:
    movie = db.get(MovieDB, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.post("/movies", response_model=Movie, status_code=status.HTTP_201_CREATED)
def create_movie(
    movie_fields: MovieFields,
    db: Session = Depends(get_db),
) -> MovieDB:
    movie = MovieDB(**movie_fields.model_dump())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie


@router.put("/movies/{movie_id}", response_model=Movie)
def update_movie(
    movie_id: int,
    movie_fields: MovieFields,
    db: Session = Depends(get_db),
) -> MovieDB:
    movie = db.get(MovieDB, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    for field, value in movie_fields.model_dump().items():
        setattr(movie, field, value)
    db.commit()
    db.refresh(movie)
    return movie


@router.patch("/movies/{movie_id}/watched", response_model=Movie)
def update_watched_status(
    movie_id: int,
    update: WatchedUpdate,
    db: Session = Depends(get_db),
) -> MovieDB:
    movie = db.get(MovieDB, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    movie.watched = update.watched
    db.commit()
    db.refresh(movie)
    return movie


@router.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, db: Session = Depends(get_db)) -> Response:
    movie = db.get(MovieDB, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

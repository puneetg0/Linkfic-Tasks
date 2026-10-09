from sqlalchemy import select

from database import SessionLocal
from models.db_models import MovieDB


with SessionLocal() as session:
    statement = select(MovieDB).where(MovieDB.title == "Inception")
    movie = session.scalars(statement).first()

    if movie is None:
        print("No Inception row found")
    else:
        print(f"Found: {movie.title} ({movie.release_year})")
        print(f"Watched: {movie.watched}")
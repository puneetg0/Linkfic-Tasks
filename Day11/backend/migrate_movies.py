import json
from pathlib import Path

from sqlalchemy import select

from .database import SessionLocal
from .models.db_models import MovieDB


def migrate_movies() -> tuple[int, int]:
    data_file = Path(__file__).resolve().parent / "movies.json"
    movies_data = json.loads(data_file.read_text(encoding="utf-8"))
    imported = 0
    skipped = 0

    with SessionLocal.begin() as session:
        existing_titles = {
            title.casefold() for title in session.scalars(select(MovieDB.title))
        }

        for movie_data in movies_data:
            title = movie_data["title"]
            if title.casefold() in existing_titles:
                skipped += 1
                continue

            session.add(
                MovieDB(
                    title=title,
                    genre=movie_data["genre"],
                    release_year=movie_data["release_year"],
                    rating=movie_data["rating"],
                    watched=movie_data["watched"],
                    poster_url=movie_data["poster_url"],
                )
            )
            existing_titles.add(title.casefold())
            imported += 1

    return imported, skipped


if __name__ == "__main__":
    imported_count, skipped_count = migrate_movies()
    print(f"Imported {imported_count} movies; skipped {skipped_count} already in the database.")

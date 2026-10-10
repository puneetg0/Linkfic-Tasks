from sqlalchemy import Index, inspect, text

if __package__:
    from .auth_day13 import AuthBase
    from .database import engine
    from .models.db_models import MovieDB
else:
    from auth_day13 import AuthBase
    from database import engine
    from models.db_models import MovieDB


def migrate() -> None:
    AuthBase.metadata.create_all(bind=engine)

    with engine.begin() as connection:
        movie_columns = {
            column["name"]
            for column in inspect(connection).get_columns("movies")
        }

        if "owner_id" not in movie_columns:
            connection.execute(
                text(
                    "ALTER TABLE movies "
                    "ADD COLUMN owner_id INTEGER "
                    "REFERENCES day13_users (id) ON DELETE SET NULL"
                )
            )

        first_user_id = connection.scalar(
            text("SELECT id FROM day13_users ORDER BY id LIMIT 1")
        )
        claimed_movies = 0
        if first_user_id is not None:
            result = connection.execute(
                text(
                    "UPDATE movies SET owner_id = :owner_id "
                    "WHERE owner_id IS NULL"
                ),
                {"owner_id": first_user_id},
            )
            claimed_movies = result.rowcount

    Index("ix_movies_owner_id", MovieDB.owner_id).create(
        bind=engine,
        checkfirst=True,
    )
    print(
        "CineShelf migration complete: "
        f"{claimed_movies} legacy movie(s) assigned to the first account."
    )


if __name__ == "__main__":
    migrate()

from sqlalchemy import inspect, text

if __package__:
    from .database import engine
    from .migrate_day14 import migrate as migrate_day14
else:
    from database import engine
    from migrate_day14 import migrate as migrate_day14


def migrate() -> None:
    migrate_day14()

    with engine.begin() as connection:
        user_columns = {
            column["name"]
            for column in inspect(connection).get_columns("day13_users")
        }
        if "role" not in user_columns:
            connection.execute(
                text(
                    "ALTER TABLE day13_users "
                    "ADD COLUMN role VARCHAR(20) NOT NULL DEFAULT 'user'"
                )
            )

    print("CineShelf Day 15 migration complete: user roles are ready.")


if __name__ == "__main__":
    migrate()

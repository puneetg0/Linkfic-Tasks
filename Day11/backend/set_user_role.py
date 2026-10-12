import argparse

from sqlalchemy import text

if __package__:
    from .database import SessionLocal
else:
    from database import SessionLocal


def set_user_role(email: str, role: str) -> None:
    with SessionLocal() as db:
        result = db.execute(
            text(
                "UPDATE day13_users SET role = :role "
                "WHERE lower(email) = :email RETURNING email"
            ),
            {"email": email.lower(), "role": role},
        )
        updated_email = result.scalar_one_or_none()
        if updated_email is None:
            raise SystemExit(f"No CineShelf account exists for {email}.")
        db.commit()

    print(f"Updated {updated_email} to role '{role}'.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Set a CineShelf account role using trusted backend access."
    )
    parser.add_argument("email", help="Email address of the existing account")
    parser.add_argument("role", choices=("user", "admin"))
    arguments = parser.parse_args()
    set_user_role(arguments.email.strip(), arguments.role)


if __name__ == "__main__":
    main()

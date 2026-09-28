# 1. Data: this list holds every movie while the program is running.
movies = []


# 2. CRUD operations: these functions create, read, update, and delete movies.
def create_movie(title, genre, release_year, rating, watched=False):
    movie_id = 1
    for saved_movie in movies:
        if saved_movie["id"] >= movie_id:
            movie_id = saved_movie["id"] + 1

    movie = {
        "id": movie_id,
        "title": title,
        "genre": genre,
        "release_year": release_year,
        "rating": rating,
        "watched": watched,
    }
    movies.append(movie)
    return movie


def get_movies():
    return movies


def get_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return None


def update_movie(movie_id, title, genre, release_year, rating, watched):
    movie = get_movie(movie_id)
    if movie is None:
        return False

    movie.update(
        {
            "title": title,
            "genre": genre,
            "release_year": release_year,
            "rating": rating,
            "watched": watched,
        }
    )
    return True


def delete_movie(movie_id):
    movie = get_movie(movie_id)
    if movie is None:
        return False

    movies.remove(movie)
    return True


def display_movie(movie):
    watched_text = "Yes" if movie["watched"] else "No"
    print(
        f"{movie['id']}: {movie['title']} | {movie['genre']} | "
        f"{movie['release_year']} | Rating: {movie['rating']:.1f} | "
        f"Watched: {watched_text}"
    )


# 3. Menu: ask the user what they want to do, then call a CRUD function.
def run_menu():
    while True:
        print("\nMovie Collection Manager")
        print("1. Add movie")
        print("2. View all movies")
        print("3. View movie details")
        print("4. Update movie")
        print("5. Delete movie")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Title: ")
            genre = input("Genre: ")
            release_year = int(input("Release year: "))
            rating = float(input("Rating (0-10): "))
            watched = input("Watched? (y/n): ").lower() == "y"
            movie = create_movie(title, genre, release_year, rating, watched)
            print(f"Added movie with ID {movie['id']}.")
        elif choice == "2":
            if not get_movies():
                print("Your collection is empty.")
            else:
                for movie in get_movies():
                    display_movie(movie)
        elif choice == "3":
            movie_id = int(input("Movie ID: "))
            movie = get_movie(movie_id)
            if movie is None:
                print("Movie not found.")
            else:
                display_movie(movie)
        elif choice == "4":
            movie_id = int(input("Movie ID: "))
            movie = get_movie(movie_id)
            if movie is None:
                print("Movie not found.")
            else:
                title = input("New title: ")
                genre = input("New genre: ")
                release_year = int(input("New release year: "))
                rating = float(input("New rating (0-10): "))
                watched = input("Watched? (y/n): ").lower() == "y"
                update_movie(
                    movie_id, title, genre, release_year, rating, watched
                )
                print("Movie updated.")
        elif choice == "5":
            movie_id = int(input("Movie ID: "))
            if delete_movie(movie_id):
                print("Movie deleted.")
            else:
                print("Movie not found.")
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Choose one of the listed options.")


if __name__ == "__main__":
    run_menu()
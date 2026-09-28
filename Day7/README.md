# Movie Collection Manager

A learning project that grows from basic Python CRUD into a full-stack application. You can use this guide to run the app, understand how its files fit together, and explain the project in an interview or class presentation.

## What It Does

The app manages a personal movie collection. A user can:

- Add a movie and its title, genre, release year, rating, and watched status
- Browse the collection and open a movie's details
- Edit or delete a movie
- Mark a movie watched or unwatched
- Search by title and filter by genre

The collection starts with 25 sample movies, including Indian films. Movie data is currently stored in the FastAPI process's memory, not in a database.

## Project Structure

```text
Day7/
|-- main.py                         # Part 1: Python-list CRUD practice
|-- README.md                       # This guide
|-- backend/
|   |-- main.py                     # FastAPI app, data, validation, and routes
|   `-- requirements.txt            # Python packages for the API
`-- frontend/
        |-- index.html                  # Browser page that loads React
        |-- package.json                # JavaScript packages and commands
        `-- src/
                |-- App.jsx                 # Main page state and app workflow
                |-- api.js                  # HTTP requests from React to FastAPI
                |-- style.css               # Layout, colors, and responsive styles
                `-- components/
                        |-- Navbar.jsx          # Search, genre filter, add button
                        |-- MovieForm.jsx       # Add and edit form
                        |-- MovieList.jsx       # Empty, loading, or movie-list view
                        |-- MovieCard.jsx       # One movie in the collection
                        `-- MovieDetails.jsx    # Selected movie and its actions
```

### Why Are There Two `main.py` Files?

The root `main.py` is the small first lesson: CRUD with a Python list and a text menu. `backend/main.py` is the next version of that idea, exposed through web API routes so React can use it. The first file is kept for learning; the full website uses the backend folder.

## Run It On Windows

You need Python, Node.js, and npm installed. Start the backend and frontend in two separate PowerShell terminals. Keep both terminals running while using the website.

### Terminal 1: Start FastAPI

From the project root, run:

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

The API is at `http://localhost:8000`. FastAPI also creates an interactive API page at `http://localhost:8000/docs`.

### Terminal 2: Start React

Open a second PowerShell terminal at the project root and run:

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL printed in the terminal. It is usually `http://localhost:5173`.

### Run The Part 1 Exercise

To run only the original Python-list exercise, open a terminal at the project root and run:

```powershell
python main.py
```

This text-menu program is separate from the React website.

## The Movie Data

Each movie is represented as a Python dictionary and sent between the backend and frontend as JSON:

```json
{
    "id": 1,
    "title": "Inception",
    "genre": "Sci-Fi",
    "release_year": 2010,
    "rating": 8.8,
    "watched": true,
    "poster_url": "https://example.com/poster.jpg"
}
```

`poster_url` is optional. `watched` is a Boolean: `true` means watched and `false` means not watched. The extra poster field is used by the website; the main movie fields are ID, title, genre, release year, rating, and watched status.

In `backend/main.py`, the `MovieFields` Pydantic model checks incoming data. For example, the rating must be between 0 and 10, the release year must be between 1888 and 2100, and title and genre cannot be blank. The `Movie` model adds the ID to those fields.

## How The Full-Stack Flow Works

```text
Person using the browser
                    |
                    v
React page and components
                    |
                    v
frontend/src/api.js sends an HTTP request
                    |
                    v
FastAPI checks the request and runs a route
                    |
                    v
The Python movies list is read or changed
                    |
                    v
FastAPI returns JSON to React
                    |
                    v
React updates the page
```

### Example: Add A Movie

1. The user clicks **Add a movie**. `App.jsx` opens `MovieForm.jsx`.
2. The user fills in the form. The form keeps its input values in React state.
3. On submit, `MovieForm.jsx` calls the `onSave` function it received from `App.jsx`.
4. `App.jsx` calls `createMovie` from `api.js`.
5. `api.js` sends a `POST /movies` request with the movie data as JSON.
6. FastAPI validates the request using `MovieFields`, assigns the next ID, and adds a dictionary to the `movies` list.
7. FastAPI returns the new movie as JSON.
8. React reloads the movie list and renders the new movie card.

The other actions follow the same pattern. The component handles the interaction, `App.jsx` coordinates state, `api.js` sends the request, and FastAPI performs the data operation.

## React Components

| File | Beginner explanation |
| --- | --- |
| `App.jsx` | The main coordinator. It stores movies, search, genre, and selected movie in state, and connects child components to API functions. |
| `Navbar.jsx` | Shows the search box, genre selector, API connection status, and add button. |
| `MovieForm.jsx` | Displays the form for creating or editing a movie. |
| `MovieList.jsx` | Chooses between a loading message, an empty-state message, or the movie cards. |
| `MovieCard.jsx` | Displays a movie's poster, title, year, genre, rating, and watched control. |
| `MovieDetails.jsx` | Shows one selected movie and offers watched, edit, and delete actions. |
| `api.js` | Keeps the HTTP request code in one place instead of putting `fetch` calls in every component. |

### React Ideas Used Here

- **Component:** A reusable piece of the page, written as a JavaScript function that returns JSX.
- **Props:** Values and event handlers passed from a parent component to a child. For example, `App.jsx` gives `MovieList.jsx` the movies to display.
- **State:** Values React remembers and uses to render the page. `useState` stores the current collection, filters, form, and selected movie.
- **Event:** Something the user does, such as typing, submitting a form, or clicking a button.
- **Effect:** `useEffect` loads movies when the page opens and when the search or genre filter changes.
- **API request:** A message sent from the browser to the backend over HTTP. `api.js` uses `fetch` to send and receive JSON.

## CRUD And API Routes

CRUD means **Create, Read, Update, Delete**. HTTP methods communicate which operation the client wants to perform.

| CRUD action | HTTP method and route | What it does |
| --- | --- | --- |
| Create | `POST /movies` | Validates and adds a movie; returns the new movie and ID. |
| Read all | `GET /movies` | Returns the movies. Optional `search` and `genre` query parameters filter the results. |
| Read one | `GET /movies/{movie_id}` | Returns one movie by ID, or a 404 response if it does not exist. |
| Update | `PUT /movies/{movie_id}` | Replaces that movie's editable fields. |
| Update watched status | `PATCH /movies/{movie_id}/watched` | Changes only whether the movie is watched. |
| Delete | `DELETE /movies/{movie_id}` | Removes the movie. |
| List genres | `GET /genres` | Returns the genres currently used by movies. |
| Health check | `GET /health` | Confirms that the API is running. |

### Search And Filter Examples

```text
GET http://localhost:8000/movies?search=star
GET http://localhost:8000/movies?genre=Drama
GET http://localhost:8000/movies?search=the&genre=Action
```

Search is case-insensitive and checks movie titles. Genre matching is also case-insensitive.

## Try The API In Swagger Or Postman

The easiest way to explore the API is to open `http://localhost:8000/docs` while the backend is running. Expand a route, click **Try it out**, enter values, and click **Execute**.

For Postman, create a request to `http://localhost:8000/movies` and choose `POST`. Set the body type to **raw** and **JSON**, then send a body such as:

```json
{
    "title": "Arrival",
    "genre": "Sci-Fi",
    "release_year": 2016,
    "rating": 8.0,
    "watched": false,
    "poster_url": null
}
```

The response contains the saved movie and its assigned ID. Use that ID with `GET`, `PUT`, `PATCH`, or `DELETE` to try the other routes.

## How To Explain This Project

### Short Presentation

> I built a movie collection manager with a React frontend and a FastAPI backend. React displays the movies and handles user input. When someone adds, edits, searches, or deletes a movie, the frontend sends an HTTP request through a small API helper file. FastAPI validates the data, performs the CRUD operation on a Python list, and returns JSON. React then uses that response to update the page. The data is currently in memory, so it resets when the backend restarts.

### Questions You May Be Asked

**What does full stack mean here?**

The project includes the frontend that the user sees and the backend that validates and manages movie data. The two parts communicate through HTTP requests and JSON responses.

**Why use FastAPI?**

FastAPI lets Python functions become API routes. It validates request data using Pydantic models and automatically provides interactive documentation at `/docs`.

**Why does the frontend not edit the Python list directly?**

The frontend runs in the browser and the Python list lives in the backend process. HTTP requests are the bridge between them. The backend owns the data changes and sends results back to the browser.

**What is JSON?**

JSON is a common text format for structured data. Here it carries movie fields from React to FastAPI and carries movie results back to React.

**What is CORS?**

The browser treats the frontend and backend ports as different origins. The FastAPI CORS middleware allows the local React development server to make requests to the API.

**Where is the database?**

There is no database yet. The backend stores movies in a Python list, which keeps the CRUD example simple. Restarting the backend resets the list to the sample movies. A next step could replace the list with SQLite or PostgreSQL.

## Important Limitations

- Movie data is in memory. New changes disappear when the FastAPI process restarts.
- This is a learning/demo project, not a production account-based application.
- Poster images use remote URLs when provided. Movies without a poster URL show a generated title treatment instead.

## Troubleshooting

- **The page says it cannot reach the API:** Make sure the backend terminal is still running at port 8000, then refresh the browser.
- **The API docs do not load:** Start the backend command from inside the `backend` folder and open `http://localhost:8000/docs`.
- **The `npm` command is not found:** Install Node.js, open a new terminal, and try again.
- **A port is already in use:** Stop the other process using that port, or start the relevant server on a different port and update the frontend API URL if the backend port changes.
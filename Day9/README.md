# Reel Movies: Day 9 State And Effects

Day 9 continues the movie collection from Day 8. The React app uses the Day 8 FastAPI backend, which saves the movie collection in `Day8/backend/movies.json` so additions and changes survive server restarts.

## Run The App

Open two PowerShell terminals in the `Linkfic Tasks` folder. Start the Day 8 backend in the first:

```powershell
cd Day8\backend
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload --port 8000
```

Start the Day 9 frontend in the second:

```powershell
cd Day9
npm install
npm run dev
```

Open the local URL printed by Vite, usually `http://localhost:5173`.

## Three Views

- **Home** shows collection totals and a few movies.
- **All Movies** shows every movie, with title search and a genre filter.
- **To Watch** shows only movies that are not marked as watched.
- **Add movie** opens a form and saves the new entry to the Day 8 backend.

The navigation changes `activePage`. Movie cards are rendered from the API data, so the totals and To Watch page update when a movie's watched status changes.

## Tailwind CSS

Tailwind CSS v4 is connected to Vite with `@tailwindcss/vite`. The theme colors and fonts are in `src/index.css`; the navigation, page layout, and add-movie form use Tailwind utility classes directly in `src/App.jsx`. `src/style.css` keeps a few custom rules for the poster layout and decorative details.

## How The Hooks Work

### `useState`

`useState` remembers a value while the component is on screen. In `src/App.jsx`, it stores the movie list, selected page, search text, genre, loading/error messages, and which movie is being updated. Call a setter, such as `setActivePage('movies')`, to update the value and ask React to render again.

### `useEffect`

`useEffect` runs after React renders. The effect in `src/App.jsx` requests `/movies` from the Day 8 backend when the app first opens. Its empty dependency array (`[]`) means “run once after the first render.” The cleanup function aborts the request if the component is removed before it finishes.

### Updating A Movie

Click the circle/check button on a movie card. The app sends a `PATCH` request to Day 8, then updates the matching movie in React state. React renders the new status and recalculates the To Watch count.

Submit the Add movie form to send a `POST` request. On success, React adds the returned movie to its state and opens All Movies.

## Try Explaining It

“The backend gives React the movie data. `useEffect` loads that data when the page opens. `useState` remembers the data and which page I selected. When I click a navigation button, React changes the page. When I mark a movie watched, the app updates the backend and then updates React state, so the list and counts refresh.”

The API creates `Day8/backend/movies.json` on its first run. Keep this file to preserve added movies and watched-status changes. Delete it only if you want to reset the collection to its 25 starter movies.

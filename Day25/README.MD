# Day 25: Frontend Development and Backend API Integration

## Task Description

Build the main user interface pages for the project, integrate the React frontend with the FastAPI backend, display data dynamically from backend APIs, and create forms to submit user input. Focus on reusable React components, responsive design, API integration using Axios, and consistent UI design.

The objective is to connect the frontend and backend into a functional application where data can be fetched, displayed, and submitted through the user interface.

## Assigned Tasks

1. Build the main UI pages.
2. Connect the frontend with the backend.
3. Display data dynamically.
4. Add forms for user input and data submission.
5. Create reusable React components.
6. Implement responsive layouts for different screen sizes.
7. Integrate APIs using Axios.
8. Handle loading states, errors, and API responses.
9. Practice JSON serialization and React rendering concepts.
10. Implement basic search functionality.
11. Test frontend and backend integration.
12. Update the GitHub repository with completed work.

---

## 1. Build the Main UI Pages

### Objective

Create the main pages required for the application and organize the user interface into reusable components.

### Tasks

- Create the main dashboard page.
- Add a header or navigation bar.
- Create reusable cards for displaying information.
- Add sections to display records retrieved from the backend.
- Create forms for adding new records.
- Add buttons for actions such as submit, search, edit, or delete, where applicable.
- Maintain consistent spacing, colors, typography, and button styles.

### Implementation

Organize the frontend into components instead of writing the entire interface inside a single file.

Suggested folder structure:

```text
frontend/
├── src/
│   ├── components/
│   │   ├── Navbar.jsx
│   │   ├── DataCard.jsx
│   │   └── Loading.jsx
│   ├── pages/
│   │   ├── Dashboard.jsx
│   │   └── AddRecord.jsx
│   ├── services/
│   │   └── api.js
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
├── package.json
└── .env
```

Adjust the folder names and pages according to the existing project structure. Avoid duplicating components that already exist.

### Expected Outcome

- Main UI pages are implemented.
- Components are organized and reusable.
- Navigation and page layouts are consistent.
- UI elements are connected to the intended application features.

---

## 2. Connect the Frontend with the Backend

### Objective

Connect the React application to the FastAPI backend so the frontend can retrieve and submit data through REST APIs.

### Concepts to Learn

**Frontend:** React manages the user interface and user interactions.

**Backend:** FastAPI processes requests, applies validation and business logic, and communicates with the database.

**API:** An interface that allows the frontend and backend to exchange data.

**Axios:** A JavaScript library used to send HTTP requests to an API.

### Tasks

- Install Axios in the React project.
- Identify the existing FastAPI endpoints.
- Configure the backend base URL.
- Create a reusable API service.
- Send GET requests to retrieve data.
- Send POST requests to submit new records.
- Handle successful responses and failed requests.
- Verify that the frontend receives the expected data.

### Install Axios

Run the following command inside the frontend project directory:

```bash
npm install axios
```

### Configure the API Service

Create `src/services/api.js`:

```javascript
import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
```

Add the backend URL to the frontend `.env` file:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Restart the Vite development server after changing environment variables.

Use the actual backend URL and port configured for the project. Keep secrets out of frontend environment variables because values exposed to browser code are not private.

### Example GET Request

```javascript
import api from "../services/api";

const response = await api.get("/items");
console.log(response.data);
```

Replace `/items` with an endpoint that actually exists in the FastAPI application.

### Important Points

- Confirm that the backend server is running.
- Use the correct API endpoint and HTTP method.
- Check the response structure before accessing its fields.
- Configure CORS in FastAPI if the frontend and backend run on different origins.
- Avoid repeating the base URL in every component.

### Expected Outcome

The React frontend can communicate with the FastAPI backend and receive API responses successfully.

---

## 3. Display Data Dynamically

### Objective

Retrieve data from the backend and render it in the React interface instead of displaying only hardcoded information.

### Concepts to Learn

**State:** Stores data that can change while the application runs.

**useEffect:** Runs side-effect logic, such as fetching data when a component loads.

**Rendering:** Converts React components and their data into the visible user interface.

**Dynamic rendering:** Generates UI elements from the current application data.

### Tasks

- Create state variables to store API data.
- Fetch records when the page loads.
- Store the returned data in React state.
- Use `.map()` to display multiple records.
- Add a loading indicator while data is being fetched.
- Display an appropriate message when no records are available.
- Handle errors when the API request fails.
- Refresh the displayed data when appropriate.

### Example: Fetch and Display Records

```jsx
import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchItems() {
      try {
        const response = await api.get("/items");
        setItems(response.data);
      } catch (err) {
        setError("Unable to load records.");
      } finally {
        setLoading(false);
      }
    }

    fetchItems();
  }, []);

  if (loading) {
    return <p>Loading records...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  if (items.length === 0) {
    return <p>No records found.</p>;
  }

  return (
    <div>
      <h1>Dashboard</h1>

      {items.map((item) => (
        <div key={item.id}>
          <h3>{item.name}</h3>
          <p>{item.description}</p>
        </div>
      ))}
    </div>
  );
}

export default Dashboard;
```

This example assumes that the endpoint returns an array of objects containing `id`, `name`, and `description`. Adjust the field names and response handling to match the actual API.

### Expected Outcome

- Records are loaded from the backend.
- The interface updates when state changes.
- Loading, empty, and error states are handled.
- Multiple records are rendered dynamically.

---

## 4. Add Forms for User Input

### Objective

Build forms that collect user input and submit it to the backend for validation and processing.

### Tasks

- Create a form with the required input fields.
- Use React state to manage form values.
- Handle input changes.
- Prevent the browser's default form submission behavior.
- Validate required fields.
- Send the form data using an Axios POST request.
- Display success or error feedback.
- Clear the form after a successful submission, where appropriate.
- Refresh the displayed records after adding a new record.

### Example: Add a Record

```jsx
import { useState } from "react";
import api from "../services/api";

function AddRecord({ onCreated }) {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [message, setMessage] = useState("");
  const [submitting, setSubmitting] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();
    setMessage("");

    if (!name.trim()) {
      setMessage("Name is required.");
      return;
    }

    try {
      setSubmitting(true);

      await api.post("/items", {
        name: name.trim(),
        description: description.trim(),
      });

      setName("");
      setDescription("");
      setMessage("Record added successfully.");

      if (onCreated) {
        await onCreated();
      }
    } catch (err) {
      setMessage("Unable to add the record.");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Record</h2>

      <label htmlFor="name">Name</label>
      <input
        id="name"
        value={name}
        onChange={(event) => setName(event.target.value)}
        required
      />

      <label htmlFor="description">Description</label>
      <textarea
        id="description"
        value={description}
        onChange={(event) => setDescription(event.target.value)}
      />

      <button type="submit" disabled={submitting}>
        {submitting ? "Submitting..." : "Add Record"}
      </button>

      {message && <p role="status">{message}</p>}
    </form>
  );
}

export default AddRecord;
```

The `/items` endpoint and its fields are examples. Match the request body to the Pydantic schema defined in FastAPI.

### Expected Outcome

- The form accepts and validates input.
- Data is sent to the backend.
- Success and error messages are displayed.
- The interface reflects newly created records.

---

## 5. Create Reusable React Components

### Objective

Reduce code duplication and maintain a consistent UI by creating components that can be used in multiple pages.

### Tasks

- Identify repeated UI elements.
- Extract reusable components such as navigation bars, cards, buttons, and loading indicators.
- Pass information into components using props.
- Keep each component focused on a clear responsibility.
- Use consistent naming conventions.
- Avoid unnecessary duplication of API request logic.

### Example

```jsx
function DataCard({ title, description }) {
  return (
    <article className="data-card">
      <h3>{title}</h3>
      <p>{description}</p>
    </article>
  );
}

export default DataCard;
```

Use the component wherever a record needs to be displayed:

```jsx
<DataCard
  title={item.name}
  description={item.description}
/>
```

### Expected Outcome

- Components can be reused across pages.
- UI changes are easier to maintain.
- The project structure is easier to understand.

---

## 6. Implement Responsive Design

### Objective

Make the application usable on desktop computers, tablets, and mobile devices.

### Tasks

- Use flexible layouts with Flexbox or CSS Grid.
- Add appropriate spacing and responsive font sizes.
- Ensure forms fit smaller screens.
- Make buttons and input fields easy to use on mobile.
- Prevent horizontal overflow.
- Check navigation and cards at different viewport widths.
- Use media queries when required.

### Example CSS

```css
.dashboard {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.data-card {
  padding: 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  min-width: 0;
}

form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

input,
textarea,
button {
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}

@media (max-width: 768px) {
  .dashboard {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 480px) {
  .dashboard {
    grid-template-columns: 1fr;
  }
}
```

Adapt the class names to the actual project CSS. If Tailwind CSS is already configured, use its responsive utilities instead of introducing an unnecessary styling approach.

### Expected Outcome

The application layout adjusts correctly to different screen sizes without breaking the main functionality.

---

## 7. Handle API Loading, Errors, and Responses

### Objective

Improve the user experience by handling different API request outcomes.

### Tasks

- Display a loading indicator during API requests.
- Show a useful message when a request fails.
- Disable submission buttons while forms are processing.
- Handle empty API responses.
- Display confirmation after successful operations.
- Avoid showing raw server errors directly to users.
- Check browser console and network requests when troubleshooting.

### Common Issues

| Issue | What to Check |
|---|---|
| Network error | Confirm the backend is running and the URL is correct. |
| CORS error | Check FastAPI CORS middleware and allowed origins. |
| 404 Not Found | Verify the API route and HTTP method. |
| 422 Unprocessable Entity | Check the request body against the Pydantic schema. |
| 500 Internal Server Error | Review backend logs and server-side exceptions. |
| Data not updating | Check state updates and whether the data is fetched again. |

### Expected Outcome

API requests fail gracefully, and the interface provides meaningful feedback.

---

## 8. Practice JSON Serialization

### Objective

Understand how data is exchanged between React and FastAPI using JSON.

### Concepts

**JSON (JavaScript Object Notation)** is a common format for sending structured data between applications.

**Serialization** converts data into a format suitable for transmission or storage.

**Deserialization** converts encoded data back into a usable data structure.

### Tasks

- Inspect JSON returned by a GET endpoint.
- Understand objects, arrays, strings, numbers, booleans, and `null`.
- Send JavaScript objects through Axios.
- Verify that FastAPI receives the expected request data.
- Check how backend models and schemas shape API responses.
- Handle missing or optional fields safely.

### Example JSON

```json
{
  "id": 1,
  "name": "Sample Record",
  "description": "Learning API integration",
  "completed": false
}
```

Axios automatically serializes ordinary JavaScript objects into JSON request bodies and parses JSON responses when appropriate. FastAPI uses request schemas and response serialization to validate and return data.

### Expected Outcome

A clear understanding of how JSON data travels between the frontend and backend.

---

## 9. Understand the React Rendering Lifecycle

### Objective

Understand when React renders components and how state and effects affect the interface.

### Topics to Learn

- Initial rendering.
- Component re-rendering.
- State updates with `useState`.
- Side effects with `useEffect`.
- Dependency arrays.
- Rendering lists with `.map()`.
- Stable keys for list items.
- Cleanup functions for effects when required.

### Tasks

- Observe the component before and after an API response.
- Change a state variable and observe the UI update.
- Fetch initial data using `useEffect`.
- Understand why state updates cause re-renders.
- Avoid unnecessary effects and repeated API calls.
- Use stable keys when rendering lists.

### Expected Outcome

A basic understanding of how React updates the interface when application data changes.

---

## 10. Implement Basic Search Functionality

### Objective

Allow users to search through records displayed on the dashboard.

### Tasks

- Add a search input.
- Store the search term in React state.
- Filter records based on the entered text.
- Display matching results.
- Show a message when no results match.
- Decide whether filtering should happen on the frontend or through a backend search endpoint.

### Example: Frontend Filtering

```jsx
const [searchTerm, setSearchTerm] = useState("");

const filteredItems = items.filter((item) =>
  item.name
    .toLowerCase()
    .includes(searchTerm.trim().toLowerCase())
);
```

Render the filtered array instead of the original array.

This approach works well for small datasets already loaded into the browser. For large datasets, consider backend search and pagination.

### Expected Outcome

Users can search the displayed records and find relevant information quickly.

---

## 11. DSA and Coding Practice

### A. Python / Backend: JSON Serialization

Tasks:

- Understand JSON-compatible Python data types.
- Convert a Python dictionary into a JSON string using `json.dumps()`.
- Convert a JSON string into a Python object using `json.loads()`.
- Understand how FastAPI returns JSON responses.
- Identify data that cannot be serialized directly without conversion.

Example:

```python
import json

data = {
    "name": "Sample Record",
    "completed": False
}

json_string = json.dumps(data)
python_data = json.loads(json_string)

print(json_string)
print(python_data)
```

### B. Frontend / React: Rendering Concepts

Tasks:

- Render a list using `.map()`.
- Use a unique, stable key for every list item.
- Update UI state with `useState`.
- Fetch data with `useEffect`.
- Display loading and empty states.

### C. Problem Solving / DSA: Search Algorithms

Tasks:

- Understand linear search.
- Understand binary search.
- Implement both algorithms in Python.
- Compare their time complexities.
- Identify when binary search can be used.

Linear search checks elements one by one and takes \(O(n)\) time in the worst case.

Binary search repeatedly halves the search space and takes \(O(\log n)\) time in the worst case, provided the input is sorted.

### Practice Problems

1. Find an element in a list using linear search.
2. Find an element in a sorted list using binary search.
3. Return the index of the target element.
4. Return `-1` when the element is not found.
5. Test both algorithms with empty lists and duplicate values.

### Expected Outcome

Improved understanding of JSON handling, React rendering, and basic search algorithms.

---



## Deliverables

1. Main frontend pages completed.
2. Frontend connected to the FastAPI backend.
3. Dynamic data displayed through API responses.
4. Forms implemented for data submission.
5. Reusable React components created or improved.
6. Responsive UI implemented.
7. Loading, empty, success, and error states handled.
8. Basic search functionality implemented.
9. JSON serialization and React rendering concepts practiced.
10. Linear search and binary search implemented in Python.
11. Frontend and backend integration tested.
12. GitHub repository updated with the completed work.

## Final Completion Criteria

Day 25 is complete when the main UI pages are functional, data is fetched from the backend and displayed dynamically, forms submit data successfully, the interface is responsive, and the completed changes are pushed to GitHub.

Focus on completing and testing the core functionality before adding optional styling or advanced features.

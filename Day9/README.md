# **Day 9 - React Hooks, Navigation & DSA**

## **Overview**

Day 9 focused on learning advanced React fundamentals, especially **React Hooks, multiple-view navigation, dynamic data, and improving user experience**.

The day also included Python and DSA practice covering **Reverse a List, Find Maximum Value, Binary Search, and Valid Parentheses**.

The main goal was to understand how a React application can behave like a **Single Page Application (SPA)**. Reel Movies switches between views using React state. It does not currently use React Router or change the browser URL for each view.

---

# **1. Tasks Assigned**

### **React**

- Learn React Hooks:
  - `useState`
  - `useEffect`
- Learn React Router.
- Create multiple pages.
- Add navigation.
- Display dynamic data.
- Improve user experience.

### **Learning Along the Way**

- Understand Single Page Applications (SPA).
- Understand client-side routing.
- Learn basic component lifecycle.
- Understand why Hooks replaced Class Components.

### **DSA / Coding Practice**

#### **Python / Backend**

- Reverse a List.
- Find Maximum Value.

#### **Frontend / React**

- Difference between `useState` and `useEffect`.
- Explain React Routing.

#### **Problem Solving / DSA**

- Binary Search.
- Valid Parentheses.

---

# **2. React Hooks**

## **useState**

`useState` is a React Hook used to store and update data inside a component.

Example:

```jsx
const [count, setCount] = useState(0);
```

Here:

- `count` stores the current value.
- `setCount` updates the value.
- `0` is the initial value.

### **Simple Explanation for Presentation**

> "I used `useState` to store data that can change in my React application. When the state changes, React automatically updates the UI."

---

## **useEffect**

`useEffect` is used when we want React to perform an action after rendering or when a particular value changes.

Example:

```jsx
useEffect(() => {
    console.log("Count changed");
}, [count]);
```

The effect runs when `count` changes.

It can also be used for:

- API calls
- Fetching data
- Timers
- Updating the browser title
- Other side effects

### **Simple Explanation for Presentation**

> "I used `useEffect` for operations that should happen after a component renders or when some data changes. For example, it can be used to fetch data from an API."

---

# **3. Difference Between useState and useEffect**

| useState | useEffect |
|---|---|
| Stores component data | Performs side effects |
| Updates the UI when state changes | Runs code based on rendering or dependencies |
| Uses a setter function | Uses an effect function |
| Example: counter value | Example: API request |

### **Easy Way to Remember**

> **useState = What data should I remember?**

> **useEffect = What should I do when something changes?**

---

# **4. React Router and Website Navigation**

React Router is a library used to connect browser URLs to views in a React application without completely reloading the browser page.

Reel Movies does not currently use React Router. Its navigation uses the `activePage` state in `src/App.jsx`, so the displayed view changes while the browser URL stays the same.

The navigation labels on the website are:

```text
Home | All Movies | To Watch
```

The separate **Add movie** button opens a form dialog. It is an action, not a navigation page.

The app uses these view IDs:

```text
home
movies
watchlist
```

For example, clicking **All Movies** changes the active view:

```jsx
const [activePage, setActivePage] = useState('home')

<button onClick={() => setActivePage('movies')}>
  All Movies
</button>
```

### **Simple Explanation for Presentation**

> "React Router connects URLs to pages. In my website I used `activePage` state to switch between Home, All Movies, and To Watch without reloading the page."

---

# **5. Multiple Pages**

Reel Movies displays three main views:

```text
Home       - collection totals and a few movies
All Movies - full collection, title search, and genre filter
To Watch   - movies that are not marked as watched
```

The **Add movie** form opens as a dialog from any view.

### **Why this structure is useful**

It keeps the project organized and makes the different parts of the movie collection easier to browse.

### **Simple Explanation for Presentation**

> "I created different views for the movie collection so users can browse all movies or focus on movies they still want to watch."

---

# **6. Navigation**

The website navigation lets users move between the three views:

```text
Home -> All Movies -> To Watch
```

The user can click these buttons to switch views. The Reel Movies brand button returns to Home. The separate **Add movie** button opens the add form.

When a navigation button is clicked, `setActivePage` updates the `activePage` state. React then displays the selected view without a full browser reload.

### **Simple Explanation for Presentation**

> "I added navigation so users can move between Home, All Movies, and To Watch. The selected view is managed with React state."

---

# **7. Dynamic Data**

Dynamic data means the content displayed by the application can change based on state, user actions, or data received from an API.

For example:

```jsx
const [movies, setMovies] = useState([]);
```

Reel Movies loads its movie list when the app opens. When a movie is added or its watched status changes, the movie data and visible list update.

### **Simple Explanation for Presentation**

> "I learned how to display dynamic data using React state. Instead of hardcoding everything, the UI can update when the underlying data changes."

---

# **8. Single Page Application (SPA)**

A Single Page Application is an application where the browser generally loads the main application once and React updates the displayed content as the user navigates.

In Reel Movies:

```text
User opens the website
       |
       v
React application loads
       |
       v
User clicks All Movies
       |
       v
The full movie collection appears
       |
       v
User clicks To Watch
       |
       v
Only unwatched movies appear
```

The application does not need to completely reload the website for every navigation action.

### **Simple Explanation for Presentation**

> "A Single Page Application loads the main application once and updates the required content dynamically instead of performing a complete page reload for every navigation."

---

# **9. Client-Side Routing**

Client-side routing can map browser URLs such as `/movies` to views without requesting an entirely new HTML page from the server.

Reel Movies currently uses state-based view switching rather than URL routes. `activePage` selects `home`, `movies`, or `watchlist`, and the URL stays the same. Refreshing the browser returns to Home. React Router could be added if each view needs its own shareable URL.

### **Simple Explanation for Presentation**

> "Client-side routing usually connects the URL to the displayed view. My website currently changes the displayed view using React state instead."

---

# **10. Component Lifecycle**

A React component has different stages during its existence.

Basic lifecycle:

```text
Component Created
       |
       v
Component Rendered
       |
       v
Component Updated
       |
       v
Component Removed
```

`useEffect` is commonly used when we need to perform side effects related to these stages.

### **Simple Explanation for Presentation**

> "The component lifecycle describes the different stages of a React component, from being created and rendered to being updated and eventually removed."

---

# **11. Why Hooks Replaced Class Components**

Older React applications commonly used Class Components.

Modern React mainly uses Function Components with Hooks.

### **Class Component**

```jsx
class App extends React.Component {
    ...
}
```

### **Modern Function Component**

```jsx
function App() {
    const [count, setCount] = useState(0);
}
```

Hooks make it easier to manage state and side effects inside function components.

### **Simple Explanation for Presentation**

> "Hooks provide a simpler way to use state and other React features inside function components. They reduce the need for class components and make React code easier to organize and reuse."

---

# **12. DSA Practice**

## **12.1 Reverse a List**

### Problem

Reverse the elements of a list.

Example:

```python
numbers = [1, 2, 3, 4, 5]
```

Result:

```text
[5, 4, 3, 2, 1]
```

### Approach

I used the **two-pointer approach**.

One pointer starts from the beginning and another from the end. The values are swapped while the pointers move toward the center.

### Key Concept

**Two Pointers**

### Time Complexity

```text
O(n)
```

### Presentation Explanation

> "I reversed the list using two pointers. One pointer starts from the beginning and the other from the end. I swap the values and move both pointers toward the center."

---

## **12.2 Find Maximum Value**

### Problem

Find the largest value from a list.

Example:

```python
numbers = [10, 5, 25, 8, 15]
```

Result:

```text
25
```

### Approach

I started with the first element as the maximum value and compared every other element with it.

If a larger value was found, I updated the maximum.

### Key Concept

**List Traversal**

### Time Complexity

```text
O(n)
```

### Presentation Explanation

> "I initialized the maximum value with the first element and traversed the list. Whenever I found a larger value, I updated the maximum."

---

## **12.3 Binary Search**

### Problem

Find a target value in a sorted list.

Example:

```python
numbers = [10, 20, 30, 40, 50, 60, 70]
target = 60
```

Result:

```text
Index: 5
```

### Approach

Binary Search works only when the data is sorted.

I compare the target with the middle element.

- If they are equal, the value is found.
- If the target is greater, search the right half.
- If the target is smaller, search the left half.

### Key Concept

**Divide and Conquer**

### Time Complexity

```text
O(log n)
```

### Presentation Explanation

> "Binary Search works on sorted data. Instead of checking every element, I check the middle element and eliminate half of the search space after every comparison."

---

## **12.4 Valid Parentheses**

### Problem

Check whether brackets are correctly matched.

Example:

```text
()
[]{}
{[()]}
```

These are valid.

Example:

```text
(]
([)]
```

These are invalid.

### Approach

I used a **Stack**.

Opening brackets are pushed into the stack:

```text
(
[
{
```

When a closing bracket is found, I check whether it matches the most recently opened bracket.

### Key Concepts

- Stack
- LIFO
- `append()`
- `pop()`

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

### Presentation Explanation

> "I used a stack to solve Valid Parentheses. Opening brackets are pushed into the stack. When I find a closing bracket, I compare it with the top of the stack. If they match, I remove the opening bracket. At the end, the stack should be empty."

---


# **13. What I Learned and Challenges I Faced**

I learned to use `useState` for changing views and movie data, and `useEffect` to load movies from the API. I also practiced SPA navigation, learned how state-based views differ from React Router URL routes, and worked on the four DSA problems above.

One challenge was getting the frontend and backend working together and understanding why added movies disappeared after the API stopped. The backend originally kept movies only in memory, so I updated it to save the collection in `Day8/backend/movies.json`. Another challenge was distinguishing the website's Home, All Movies, and To Watch views from URL routes; these views are selected with `activePage` state.

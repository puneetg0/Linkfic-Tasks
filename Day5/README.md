# Day 3 - React Fundamentals

## Objective

The objective of Day 3 was to understand the fundamentals of React and learn how to convert a traditional HTML/CSS landing page into a component-based React application.

The main focus areas were:

* React installation and project setup
* React project structure
* JSX
* Components
* Props
* State
* React Hooks
* Component-based Architecture
* Virtual DOM
* Single Page Application
* Converting the existing landing page into React
* Python List vs Dictionary
* Frontend Props vs State
* Missing Number problem
* Two Sum problem
* Git and GitHub workflow

---

# 1. React

## What is React?

React is a JavaScript library used to build user interfaces.

Instead of creating the complete webpage in one large file, React allows us to divide the user interface into smaller and reusable components.

For example, a landing page can be divided into:

```text
Landing Page
│
├── Navbar
├── Hero Section
├── About Section
├── Services Section
├── Contact Section
└── Footer
```

Each section can be created as a separate React component.

This makes the application easier to understand, maintain, reuse, and update.

## Why React is useful

React helps developers:

* Build reusable UI components
* Organize large applications
* Manage changing data
* Update the user interface efficiently
* Maintain cleaner project structures
* Build Single Page Applications

---

# 2. React Project Setup

## Project Creation

The React application was created using Vite.

The project was initialized using:

```bash
npm create vite@latest react-landing-page
```

The selected options were:

```text
Framework: React
Variant: JavaScript
```

Dependencies were installed using:

```bash
npm install
```

The development server was started using:

```bash
npm run dev
```

Vite provides a fast development environment for building and testing the React application locally.

---

# 3. React Project Structure

The basic project structure is:

```text
react-landing-page/
│
├── node_modules/
├── public/
│
├── src/
│   ├── assets/
│   ├── components/
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
│
├── .gitignore
├── index.html
├── package.json
├── package-lock.json
└── vite.config.js
```

## Important Folders and Files

### `src`

The `src` folder contains the main source code of the React application.

Most of the development work is performed inside this folder.

### `components`

The `components` folder contains reusable React components.

For example:

```text
components/
├── Navbar.jsx
├── Hero.jsx
├── About.jsx
├── Services.jsx
├── Contact.jsx
└── Footer.jsx
```

### `App.jsx`

`App.jsx` is the main application component.

It combines the different components and creates the overall application structure.

Example:

```jsx
function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <About />
      <Footer />
    </>
  );
}
```

### `main.jsx`

`main.jsx` is the entry point of the React application.

It connects the React application to the HTML element where React will be rendered.

A simplified example is:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <App />
);
```

The basic flow is:

```text
main.jsx
   ↓
App.jsx
   ↓
Components
   ↓
User Interface
```

### `public`

The `public` folder contains static files that can be served directly.

### `package.json`

`package.json` contains information about the project and its dependencies and scripts.

For example:

```json
{
  "scripts": {
    "dev": "vite"
  }
}
```

---

# 4. JSX

## What is JSX?

JSX stands for JavaScript XML.

JSX allows us to write HTML-like syntax inside JavaScript.

Example:

```jsx
function App() {
  return (
    <h1>Hello React</h1>
  );
}
```

The `<h1>` looks like HTML, but it is being written inside a JavaScript React component.

JSX makes it easier to describe what the user interface should look like.

---

## JSX and JavaScript

JavaScript values can be displayed inside JSX using curly brackets.

Example:

```jsx
const name = "Puneet";

function App() {
  return (
    <h1>Hello {name}</h1>
  );
}
```

The output will be:

```text
Hello Puneet
```

The curly brackets:

```text
{ }
```

allow JavaScript expressions to be used inside JSX.

---

## JSX `className`

In HTML, we normally use:

```html
<div class="container">
```

In JSX, we use:

```jsx
<div className="container">
```

This is because `class` has a special meaning in JavaScript, so JSX uses `className`.

---

## JSX Parent Element

A React component should return one parent structure.

For example:

```jsx
return (
  <div>
    <h1>Hello</h1>
    <p>Welcome</p>
  </div>
);
```

We can also use a Fragment:

```jsx
return (
  <>
    <h1>Hello</h1>
    <p>Welcome</p>
  </>
);
```

The Fragment allows multiple elements to be returned without adding an extra HTML element.

---

# 5. Components

## What is a Component?

A component is a reusable part of a React user interface.

For example:

```text
App
│
├── Navbar
├── Hero
├── About
├── Services
├── Contact
└── Footer
```

Each section can be created as a separate component.

---

## Example Component

```jsx
function Navbar() {
  return (
    <nav>
      <h2>My Website</h2>
    </nav>
  );
}

export default Navbar;
```

The component can then be used inside `App.jsx`.

```jsx
import Navbar from "./components/Navbar";

function App() {
  return (
    <Navbar />
  );
}

export default App;
```

---

## Why Components are useful

Components provide:

* Reusability
* Better organization
* Easier maintenance
* Separation of responsibilities
* Cleaner code
* Easier debugging

For example, if the Navbar needs to be changed, we can modify `Navbar.jsx` without changing the entire application.

---

# 6. Component-Based Architecture

## What is Component-Based Architecture?

Component-based architecture means building an application using small, independent, reusable components.

Instead of thinking about the entire application as one large page, we divide it into smaller pieces.

Example:

```text
React Application
│
├── Navbar
├── Hero
├── About
├── Services
├── Contact
└── Footer
```

Each component has a specific responsibility.

For example:

```text
Navbar → Navigation
Hero → Main introduction
About → Information about the website
Services → Services provided
Contact → Contact information/form
Footer → Footer information
```

This makes the application easier to develop and maintain.

---

# 7. Props

## What are Props?

Props means properties.

Props are used to pass data from a parent component to a child component.

The basic flow is:

```text
Parent Component
       ↓
      Props
       ↓
Child Component
```

Example:

```jsx
function User(props) {
  return (
    <h1>Hello {props.name}</h1>
  );
}
```

The parent can provide the value:

```jsx
<User name="Puneet" />
```

The child receives:

```text
props.name
```

and displays:

```text
Hello Puneet
```

---

## Why Props are useful

Props allow components to be reusable.

For example, instead of creating separate components for every user, we can use one component and provide different data.

```jsx
<User name="Puneet" />
<User name="Rahul" />
<User name="Amit" />
```

The same component can display different information.

---

# 8. Props vs State

Props and State are important concepts in React.

| Props                                              | State                               |
| -------------------------------------------------- | ----------------------------------- |
| Data passed from parent                            | Data managed by the component       |
| Used to pass information                           | Used to manage changing information |
| Generally read-only inside the receiving component | Can be updated                      |
| Parent → Child                                     | Component manages its own state     |

Simple way to remember:

```text
Props = Data coming into a component

State = Data managed by a component
```

Example:

```text
Props
Parent
  ↓
Child
```

State:

```text
Component
   ↓
State changes
   ↓
UI updates
```

---

# 9. State

## What is State?

State is data that can change during the lifetime of a component.

For example, a counter:

```text
0
↓
1
↓
2
↓
3
```

The counter value is state because it changes when the user interacts with the application.

---

# 10. `useState`

React provides the `useState` Hook to create and manage state.

Example:

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <>
      <h1>{count}</h1>

      <button onClick={() => setCount(count + 1)}>
        Increase
      </button>
    </>
  );
}

export default Counter;
```

The following line is important:

```jsx
const [count, setCount] = useState(0);
```

It creates:

```text
count
```

which stores the current value.

And:

```text
setCount
```

which is used to update the value.

The initial value is:

```text
0
```

When `setCount()` changes the state, React updates the component and displays the new value.

---

# 11. React Hooks

## What are Hooks?

Hooks are special functions provided by React that allow functional components to use React features.

Some commonly used Hooks are:

```text
useState
useEffect
useContext
useRef
```

For this task, the main focus was understanding `useState` and the basic concept of Hooks.

---

## `useState`

`useState` is used when a component needs to store changing data.

Example:

```jsx
const [count, setCount] = useState(0);
```

---

## `useEffect`

`useEffect` is commonly used for side effects.

Examples of side effects include:

* Fetching data from an API
* Running code after a component renders
* Working with external systems
* Setting up subscriptions or timers

A basic example:

```jsx
import { useEffect } from "react";

useEffect(() => {
  console.log("Component loaded");
}, []);
```

The empty dependency array means the effect runs after the initial render.

---

# 12. Virtual DOM

## What is Virtual DOM?

The Virtual DOM is a lightweight representation of the user interface used by React to determine what needs to change.

When state or props change, React determines the necessary UI updates and updates the browser DOM accordingly.

A simplified flow is:

```text
State / Props Change
        ↓
React checks the UI
        ↓
React determines required changes
        ↓
Browser DOM is updated
```

The important point is that developers do not need to manually update every DOM element when React state changes.

React manages the UI updates based on the component's state and props.

---

# 13. Single Page Application

## What is an SPA?

SPA stands for Single Page Application.

A Single Page Application loads the main application and can update different parts of the interface without requiring a complete browser page reload for every interaction or navigation.

A traditional website may work like:

```text
Home
 ↓
Page Load

About
 ↓
Page Load

Contact
 ↓
Page Load
```

A React application can provide an SPA experience where the interface changes while the application remains loaded.

This can make applications feel faster and more interactive.

---

# 14. Converting the Landing Page into React

The previous HTML/CSS landing page was converted into a React application.

The original landing page was divided into reusable components.

The component structure was planned as:

```text
App
│
├── Navbar
├── Hero
├── About
├── Services
├── Contact
└── Footer
```

Example project structure:

```text
src/
│
├── components/
│   ├── Navbar.jsx
│   ├── Hero.jsx
│   ├── About.jsx
│   ├── Services.jsx
│   ├── Contact.jsx
│   └── Footer.jsx
│
├── App.jsx
├── App.css
├── index.css
└── main.jsx
```

This approach separates different sections of the landing page and makes each section easier to maintain.

---

# 15. App Component

The `App.jsx` file combines the different components.

Example:

```jsx
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import About from "./components/About";
import Services from "./components/Services";
import Contact from "./components/Contact";
import Footer from "./components/Footer";

function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <About />
      <Services />
      <Contact />
      <Footer />
    </>
  );
}

export default App;
```

This creates the application structure.

---

# 16. Python Dictionary vs List

## List

A Python list stores multiple values in an ordered collection.

Example:

```python
numbers = [10, 20, 30, 40]
```

Values are accessed using indexes:

```python
print(numbers[0])
```

Output:

```text
10
```

The index starts from `0`.

---

## Dictionary

A dictionary stores data using key-value pairs.

Example:

```python
student = {
    "name": "Puneet",
    "age": 28
}
```

Values are accessed using keys:

```python
print(student["name"])
```

Output:

```text
Puneet
```

---

## List vs Dictionary

| List                           | Dictionary                    |
| ------------------------------ | ----------------------------- |
| Stores values                  | Stores key-value pairs        |
| Uses indexes                   | Uses keys                     |
| Example: `[10, 20, 30]`        | Example: `{"name": "Puneet"}` |
| Useful for ordered collections | Useful for labelled data      |

Simple way to remember:

```text
List → Index → Value

Dictionary → Key → Value
```

---

# 17. DSA Problem - Missing Number

## Problem

Given numbers from `1` to `n`, one number is missing.

Example:

```python
numbers = [1, 2, 3, 5]
```

The complete sequence should be:

```text
1 2 3 4 5
```

Therefore:

```text
Missing Number = 4
```

---

## Beginner Solution

```python
numbers = [1, 2, 3, 5]

n = 5

for i in range(1, n + 1):
    if i not in numbers:
        print("Missing number:", i)
```

Output:

```text
Missing number: 4
```

## Logic

The program:

1. Starts from `1`.
2. Goes up to `n`.
3. Checks whether each number exists in the list.
4. If a number does not exist, it is the missing number.

---

# 18. DSA Problem - Two Sum

## Problem

Given a list of numbers and a target value, find two numbers whose sum equals the target.

Example:

```python
numbers = [2, 7, 11, 15]
target = 9
```

The answer is:

```text
2 + 7 = 9
```

---

## Beginner Solution

```python
numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])
```

Output:

```text
2 7
```

## Logic

The program:

1. Selects the first number.
2. Selects another number.
3. Adds both numbers.
4. Compares the result with the target.
5. If the result matches the target, the pair is found.

This is a beginner brute-force approach.

---

# 19. Git and GitHub

After completing the React application, the project should be tracked using Git and pushed to GitHub.

The basic workflow is:

```bash
git status
```

Check which files have changed.

Then:

```bash
git add .
```

Stage the changes.

Then:

```bash
git commit -m "Complete Day 3 React fundamentals"
```

Create a commit containing the changes.

Finally:

```bash
git push
```

Push the changes to GitHub.

To verify the final status:

```bash
git status
```

The expected result is:

```text
nothing to commit, working tree clean
```

---

# 20. Task Assigned

The Day 3 task was to:

* Install React.
* Learn React project structure.
* Learn JSX.
* Learn Components.
* Learn Props.
* Learn State.
* Learn Hooks.
* Understand Component-based Architecture.
* Understand Virtual DOM.
* Understand SPA.
* Convert the previous landing page into React.
* Practice Python Dictionary vs List.
* Understand Props vs State.
* Explain JSX.
* Solve Missing Number.
* Solve Two Sum.
* Create a React application.
* Create a proper component structure.
* Update GitHub.

---

# 21. Work Completed

The following concepts and activities were covered:

* React project setup using Vite.
* React folder and file structure.
* JSX syntax.
* JavaScript expressions inside JSX.
* JSX `className`.
* React Components.
* Component-based Architecture.
* Props and data passing.
* Props vs State.
* State management using `useState`.
* Basic understanding of React Hooks.
* Basic understanding of `useEffect`.
* Virtual DOM concept.
* Single Page Application concept.
* Conversion of the landing page into React components.
* Python List vs Dictionary.
* Missing Number DSA problem.
* Two Sum DSA problem.
* Git workflow and GitHub update.

---

# 22. Measurable Impact

The main measurable improvements from this task were:

* Converted a static landing page into a React application.
* Divided the landing page into reusable components.
* Created a structured React project.
* Practiced JSX instead of writing only traditional HTML.
* Learned how data can be passed between components using Props.
* Learned how changing data can be handled using State.
* Practiced React Hooks.
* Solved two beginner-level DSA problems.
* Practiced Git version control and GitHub repository management.

The biggest improvement was moving from a traditional static HTML/CSS page toward a structured, component-based frontend application.

---

# 23. Key Concepts to Explain During the Meeting

## What is React?

React is a JavaScript library for building user interfaces using reusable components.

## What is JSX?

JSX is a syntax that allows us to write HTML-like UI structures inside JavaScript.

## What is a Component?

A component is a reusable part of the user interface.

## What are Props?

Props are values passed from a parent component to a child component.

## What is State?

State is data managed by a component that can change over time and cause the UI to update.

## What are Hooks?

Hooks are special React functions that allow functional components to use features such as state and effects.

## What is Component-Based Architecture?

It means breaking an application into smaller reusable components, with each component handling a specific part of the UI.

## What is the Virtual DOM?

It is React's representation of the UI that React uses to determine the necessary changes to the browser DOM.

## What is an SPA?

SPA means Single Page Application, where the application can update its interface without requiring a complete page reload for every interaction or navigation.

## Props vs State

Props are received from a parent component, while state is managed by the component itself.

---

# 24. Example Meeting Explanation

If I were asked:

**"What did you learn today?"**

I can explain:

> Today I learned the fundamentals of React and created a React project using Vite. I first understood the React project structure and then learned JSX, which allows us to write HTML-like syntax inside JavaScript. After that, I learned how to create reusable components and how to pass data between components using Props.
>
> I also learned State and the `useState` Hook for managing changing data in a component. Along with this, I studied the basic concepts of Component-based Architecture, Virtual DOM, and Single Page Applications.
>
> For the practical part, I converted my previous HTML and CSS landing page into a React application by separating the page into components such as Navbar, Hero, About, Services, Contact, and Footer.
>
> For coding practice, I worked on Python List vs Dictionary and solved the Missing Number and Two Sum problems. Finally, I updated the project using Git and pushed the changes to GitHub.

---

# 25. Final Deliverables

The completed Day 3 work should contain:

```text
React Application
        +
Reusable Component Structure
        +
JSX
        +
Props
        +
State
        +
Hooks
        +
Converted Landing Page
        +
DSA Practice
        +
Updated GitHub Repository
```

---

# 26. Final Checklist

* [ ] React installed
* [ ] React project created using Vite
* [ ] React project structure understood
* [ ] JSX learned
* [ ] Components learned
* [ ] Props learned
* [ ] State learned
* [ ] `useState` practiced
* [ ] Hooks understood
* [ ] `useEffect` basics understood
* [ ] Component-based Architecture understood
* [ ] Virtual DOM understood
* [ ] SPA understood
* [ ] Landing page converted into React
* [ ] Components created
* [ ] Python List vs Dictionary practiced
* [ ] Props vs State understood
* [ ] Missing Number solved
* [ ] Two Sum solved
* [ ] README created
* [ ] Git changes committed
* [ ] GitHub updated
* [ ] Final project checked

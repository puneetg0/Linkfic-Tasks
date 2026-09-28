# Day 7 - Full Stack Mini Project Preparation

## Objective

The main goal of Day 7 was to learn some basic concepts that will be used in my Full Stack Mini Project.

I focused on:

* Python CRUD
* React Component Lifecycle
* Valid Parentheses
* Linear Search
* Binary Search

My Full Stack project will be a **Movie Collection Manager**.

---

# 1. Python - CRUD Using a List

## What is CRUD?

CRUD means four basic operations:

* **Create** - Add something
* **Read** - See something
* **Update** - Change something
* **Delete** - Remove something

For practice, I used a Python list to store movies.

```python
movies = []
```

## Create

I used `append()` to add a movie.

```python
movies.append({
    "id": 1,
    "title": "Inception",
    "genre": "Sci-Fi",
    "year": 2010
})
```

**Simple explanation:**

`append()` adds a new movie to the list.

---

## Read

I used `print()` or a loop to see the movies.

```python
for movie in movies:
    print(movie)
```

**Simple explanation:**

Read means getting or displaying the data.

---

## Update

I can change information about a movie.

```python
movies[0]["genre"] = "Science Fiction"
```

**Simple explanation:**

Here I changed the genre of the first movie.

---

## Delete

I used `pop()` to remove a movie.

```python
movies.pop(0)
```

**Simple explanation:**

`pop()` removes an item from the list.

---

## CRUD Summary

```text
Create → Add movie
Read   → View movie
Update → Change movie
Delete → Remove movie
```

### What I Learned

I learned how basic CRUD operations work using a Python list.

Later, I will use the same CRUD idea in my FastAPI backend.

---

# 2. Frontend - React Component Lifecycle

## What is a Component?

A component is a small part of a React website.

For example, in my Movie Collection Manager I can have:

```text
Movie App
   |
   ├── Movie Form
   ├── Movie List
   └── Movie Card
```

Each part can be a React component.

---

## What is Component Lifecycle?

A component has three basic stages:

```text
Mount
  ↓
Update
  ↓
Unmount
```

### Mount

Mount means the component is created and shown on the screen.

Example:

```text
Movie List opens
       ↓
Component is created
       ↓
Movies are displayed
```

### Update

Update happens when something changes.

For example:

```text
Add a new movie
       ↓
Movie data changes
       ↓
React updates the screen
```

### Unmount

Unmount means the component is removed from the screen.

For example:

```text
Movie Details page
       ↓
User leaves the page
       ↓
Component is removed
```

---

## useEffect

`useEffect()` is commonly used when we need to perform an action after a component loads or when some data changes.

Example:

```jsx
useEffect(() => {
    fetchMovies();
}, []);
```

In my project, I can use this to get movies from the FastAPI backend when the Movie List loads.

### What I Learned

I learned the basic idea of how React components are created, updated, and removed.

---

# 3. DSA - Valid Parentheses

## What is the Problem?

We need to check whether brackets are correctly matched.

Examples of brackets:

```text
()
[]
{}
```

### Valid Examples

```text
()
[]{}
([{}])
```

### Invalid Examples

```text
(]
([)
```

---

## How Do We Solve It?

We use a **stack**.

A stack works like a pile of books.

The last book we put on the pile is the first book we remove.

This is called:

```text
LIFO
Last In, First Out
```

Example:

```text
Input: ([{}])

(
[
{

Then:

}
]
)
```

Every closing bracket should match the last opening bracket.

---

## Simple Python Code

```python
def is_valid(s):
    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:

        if char in "([{":
            stack.append(char)

        else:
            if not stack:
                return False

            if stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0
```

### What I Learned

I learned how to use a stack to check whether brackets are correctly matched.

---

# 4. DSA - Linear Search

## What is Linear Search?

Linear Search checks items one by one.

Example:

```text
10  20  30  40  50
```

If I want to find `40`:

```text
10 → No
20 → No
30 → No
40 → Yes
```

It checks from the beginning until it finds the value.

### Simple Example

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 40:
        print("Found")
```

### What I Learned

Linear Search is simple and works even when the data is not sorted.

---

# 5. DSA - Binary Search

## What is Binary Search?

Binary Search checks the middle value instead of checking every value.

But there is one important condition:

**The data must be sorted.**

Example:

```text
10 20 30 40 50 60 70 80 90
```

I want to find `70`.

First, I check the middle:

```text
10 20 30 40 [50] 60 70 80 90
```

70 is greater than 50, so I ignore the left side.

Then I search:

```text
60 70 80 90
```

This makes the search faster for large sorted data.

---

# 6. Linear Search vs Binary Search

| Linear Search                   | Binary Search           |
| ------------------------------- | ----------------------- |
| Checks one by one               | Checks the middle       |
| Data does not need to be sorted | Data must be sorted     |
| Simple                          | Slightly more difficult |
| O(n)                            | O(log n)                |

### Easy Way to Remember

```text
Linear Search
= Check one by one

Binary Search
= Check middle and remove half
```

---

# 7. Connection With My Project

I will use the CRUD concept in my **Movie Collection Manager**.

The basic flow will be:

```text
React Frontend
      ↓
FastAPI Backend
      ↓
Movie Data
```

For example:

```text
Add Movie
   ↓
React sends request
   ↓
FastAPI receives request
   ↓
Movie is added
```

CRUD will become API operations:

```text
Create → POST
Read   → GET
Update → PUT
Delete → DELETE
```

---

# 8. What I Completed

| Task                              | Status    |
| --------------------------------- | --------- |
| Python CRUD using List            | Completed |
| React Component Lifecycle         | Learned   |
| Valid Parentheses                 | Practiced |
| Linear Search                     | Learned   |
| Binary Search                     | Learned   |
| Movie Collection Manager Planning | Completed |

---

# 9. What I Learned

During Day 7, I learned:

* CRUD means Create, Read, Update, and Delete.
* Python lists can be used to store data.
* React components have a basic lifecycle.
* `useEffect()` can be used for actions such as fetching data.
* A stack follows LIFO.
* Valid Parentheses can be solved using a stack.
* Linear Search checks items one by one.
* Binary Search checks the middle and needs sorted data.
* CRUD concepts can be used to build APIs.

---

# 10. Next Step

The next step is to start building the **Movie Collection Manager** using:

```text
Frontend → React
Backend  → FastAPI
API      → REST API
```

I will first build the backend and then connect it with the React frontend.

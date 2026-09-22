# Day 3 - JavaScript Fundamentals and DOM Manipulation

## Objective

The objective of Day 3 was to learn the fundamentals of JavaScript and use JavaScript to make a landing page interactive.

The main focus areas were:

* JavaScript fundamentals
* Variables and data types
* Operators
* Loops
* Functions
* Arrays
* Objects
* DOM manipulation
* Event handling
* Interactive landing page
* Basic DSA practice using Python

---

## Tasks Assigned

The following tasks were assigned for Day 3:

| Category   | Task                                                        |
| ---------- | ----------------------------------------------------------- |
| JavaScript | Learn variables                                             |
| JavaScript | Learn data types                                            |
| JavaScript | Learn operators                                             |
| JavaScript | Learn loops                                                 |
| JavaScript | Learn functions                                             |
| JavaScript | Learn arrays                                                |
| JavaScript | Learn objects                                               |
| DOM        | Learn DOM manipulation                                      |
| Frontend   | Make the landing page interactive                           |
| DSA        | Write a function to calculate factorial                     |
| DSA        | Practice Fibonacci series                                   |
| DSA        | Find duplicate elements                                     |
| Frontend   | Understand the difference between `let`, `const`, and `var` |
| DOM        | Understand DOM and event handling                           |
| GitHub     | Update the GitHub repository                                |

---

## What I Learned and Completed

### 1. Variables

Learned how to store values using JavaScript variables.

```javascript
let age = 28;
const name = "Puneet";
```

`let` is used when a value may need to be reassigned, while `const` is used when the variable should not be reassigned.

---

### 2. Data Types

Learned the basic JavaScript data types:

* String
* Number
* Boolean
* Array
* Object

Example:

```javascript
let name = "Puneet";
let age = 28;
let isStudent = true;
```

---

### 3. Operators

Practiced arithmetic and comparison operators.

```javascript
let a = 10;
let b = 5;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
```

---

### 4. Loops

Learned how to repeat a block of code using a `for` loop.

```javascript
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
```

Also practiced using loops with arrays.

---

### 5. Functions

Learned how to create reusable blocks of code.

```javascript
function add(x, y) {
    return x + y;
}

let result = add(10, 15);

console.log(result);
```

Learned the difference between parameters, arguments, and `return`.

---

### 6. Arrays

Learned how to store multiple values in an array.

```javascript
let fruits = ["Apple", "Banana", "Mango"];
```

Practiced accessing array elements using indexes.

```javascript
console.log(fruits[0]);
```

Also practiced array methods such as:

```javascript
fruits.push("Orange");
fruits.pop();
```

---

### 7. Objects

Learned how to store related information using key-value pairs.

```javascript
let student = {
    name: "Puneet",
    age: 28,
    course: "JavaScript"
};

console.log(student.name);
console.log(student.course);
```

---

## DOM Manipulation

Learned how JavaScript interacts with HTML through the DOM.

The DOM allows JavaScript to select, modify, and interact with HTML elements.

Practiced:

```javascript
document.getElementById()
```

```javascript
document.querySelector()
```

```javascript
document.querySelectorAll()
```

### Difference between selectors

| Method               | Purpose                            |
| -------------------- | ---------------------------------- |
| `getElementById()`   | Selects an element using its ID    |
| `querySelector()`    | Selects the first matching element |
| `querySelectorAll()` | Selects all matching elements      |

---

## Event Handling

Learned how to respond to user actions.

For example, a button click can trigger JavaScript code:

```javascript
button.addEventListener("click", function() {
    // Code runs when the button is clicked
});
```

This allows a webpage to respond to user interaction.

---

# Interactive Landing Page

The Day 2 landing page was extended using JavaScript to make it interactive.

The page contains:

* A heading
* A description
* A button
* JavaScript event handling
* DOM manipulation

When the user clicks the button, JavaScript changes the heading, description, and button text.

Example:

```javascript
let heading = document.getElementById("heading");
let description = document.getElementById("description");
let button = document.getElementById("startBtn");

button.addEventListener("click", function() {

    heading.textContent = "Let's Start Learning!";

    description.textContent =
        "You are ready to learn JavaScript.";

    button.textContent = "Started";

});
```

## How It Works

```text
User clicks the button
        ↓
JavaScript detects the click
        ↓
Event listener runs
        ↓
JavaScript changes the DOM
        ↓
Heading, description and button are updated
```

This demonstrates how JavaScript adds behavior and interactivity to a webpage.

---

# DSA and Coding Practice

## Factorial

Practiced calculating the factorial of a number using a function and loop.

```python
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

print(factorial(5))
```

Output:

```text
120
```

---

## Fibonacci Series

Practiced generating the Fibonacci series using a loop.

```text
0 1 1 2 3 5 8 13 21
```

---

## Find Duplicate Elements

Practiced finding duplicate values in a list using a `set`.

```python
numbers = [1, 2, 3, 2, 4, 3]

duplicates = []
seen = set()

for number in numbers:
    if number in seen:
        duplicates.append(number)
    else:
        seen.add(number)

print(duplicates)
```

Output:

```text
[2, 3]
```

---

# Folder Structure

```text
Day3/
│
├── index.html
├── style.css
├── script.js
└── README.md
```

---

# Technologies Used

* HTML5
* CSS3
* JavaScript
* Python
* Git
* GitHub

---

# Key Learning

The main learning from Day 3 was understanding how JavaScript adds behavior to a webpage.

HTML provides the structure, CSS provides the design, and JavaScript provides the interaction.

The interactive landing page helped me understand how JavaScript can select HTML elements, listen for user events, and dynamically change webpage content.

---

# Challenge: Understanding Event Handling

"One of the challenges I faced was understanding event handling. Initially, I was confused about how JavaScript detects an action performed by the user, such as clicking a button. After practicing addEventListener(), I understood that we can listen for an event like a click and then execute a function when that event occurs."


Simple example
button.addEventListener("click", function() {
    heading.textContent = "Welcome!";
});

You can explain it as:

User clicks button
       ↓
JavaScript detects "click"
       ↓
Event listener runs
       ↓
Function executes
       ↓
Heading changes
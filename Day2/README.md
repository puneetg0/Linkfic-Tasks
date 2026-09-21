# Day 2 - HTML and CSS Fundamentals

## Objective

The objective of Day 2 was to learn the fundamentals of HTML and CSS and apply them by building a responsive landing page.

The main focus areas were:

- HTML document structure
- Semantic HTML
- CSS selectors
- CSS Box Model
- Flexbox
- CSS Grid
- Responsive Web Design
- Mobile-first design
- Python and DSA practice
- Git and GitHub

---

## Tasks Completed

The following tasks were completed as part of Day 2:

- Learned HTML document structure
- Learned semantic HTML elements
- Practiced CSS selectors
- Learned the CSS Box Model
- Practiced Flexbox
- Practiced CSS Grid
- Learned responsive design concepts
- Learned the difference between Flexbox and Grid
- Built a responsive landing page
- Practiced Python coding problems
- Created a proper project folder structure
- Updated the GitHub repository

---

## Technologies Used

- HTML5
- CSS3
- Python
- Git
- GitHub
- Visual Studio Code

---

## HTML Concepts

### HTML Document Structure

Learned the basic structure of an HTML5 document using:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
Semantic HTML

Learned how to use semantic HTML elements according to their purpose.

Examples:

<header>
<nav>
<main>
<section>
<article>
<footer>

Semantic HTML helps make the structure of a webpage more meaningful, readable, and maintainable.

CSS Concepts
CSS Selectors

Practiced different types of CSS selectors.

Element selector:

p {
    color: black;
}

Class selector:

.card {
    padding: 20px;
}

ID selector:

#header {
    background-color: white;
}
CSS Box Model

Learned that every HTML element can be considered as a box consisting of:

Content
Padding
Border
Margin

Example:

.card {
    padding: 20px;
    border: 1px solid #ddd;
    margin: 20px;
}
Flexbox

Flexbox is used to create and align one-dimensional layouts.

Example:

.container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

Flexbox was used in the project for:

Navigation layout
Horizontal alignment
Spacing between elements
Responsive layout adjustments
CSS Grid

CSS Grid is used for creating two-dimensional layouts using rows and columns.

Example:

.cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

Grid was used for arranging the feature cards in the landing page.

Flexbox vs Grid
Flexbox	CSS Grid
One-dimensional layout	Two-dimensional layout
Works mainly with rows or columns	Works with rows and columns
Useful for navigation and alignment	Useful for card and page layouts
Good for smaller layout components	Good for larger structured layouts

In simple terms:

Flexbox is mainly used for one direction, while Grid is used for rows and columns.

Responsive Web Design

Learned how to make a webpage adapt to different screen sizes such as desktops, tablets, and mobile devices.

CSS media queries were used to change the layout for smaller screens.

Example:

@media (max-width: 768px) {
    .cards {
        grid-template-columns: 1fr;
    }
}

This allows the feature cards to change from multiple columns to a single column on smaller screens.

Project
Responsive Landing Page

As part of the Day 2 task, I created a responsive technology learning landing page using HTML5 and CSS3.

The landing page contains the following sections:

Header
Navigation
Hero Section
Features Section
About Section
Call-to-Action Section
Footer

The project uses semantic HTML, CSS Flexbox, CSS Grid, and media queries.

Project Structure
Day2/
│
├── README.md
├── index.html
│
├── css/
│   └── style.css
│
├── images/
│
└── python_practice.py
Python and DSA Practice
1. Count Vowels

Created a Python program to count the number of vowels in a given string.

Example:

def count_vowels(text):
    count = 0
    vowels = "aeiou"

    for char in text.lower():
        if char in vowels:
            count += 1

    return count
2. Palindrome

Created a Python program to check whether a given string is a palindrome.

A palindrome is a word or string that reads the same forward and backward.

Examples:

madam
level
racecar

Example:

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]
Variable vs Constant
Variable

A variable is a value that can be changed during program execution.

Example:

age = 28
age = 29
Constant

A constant is a value that is intended to remain unchanged.

Python does not have a strict constant keyword. Uppercase naming is commonly used to indicate a constant.

Example:

MAX_USERS = 100
PI = 3.14159
Challenges

The main challenge during Day 2 was understanding the difference between Flexbox and CSS Grid and knowing when to use each one.

I practiced both concepts and used:

Flexbox for navigation and alignment
CSS Grid for the feature card layout
Media queries for responsive design
Learning Outcomes

After completing Day 2, I learned:

How to structure a webpage using HTML5
How to use semantic HTML elements
How CSS selectors work
How the CSS Box Model works
How to use Flexbox
How to use CSS Grid
The difference between Flexbox and Grid
How to create responsive layouts
How to use media queries
How to create a responsive landing page
How to organize a frontend project
How to practice basic Python and DSA problems
How to update a project using Git and GitHub
Git Commands Used

The following Git commands were used to update the repository:

git status
git add Day2
git commit -m "Complete Day 2 HTML CSS fundamentals"
git push

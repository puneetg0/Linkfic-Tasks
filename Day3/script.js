// let name = "punnet";
// let age =25;


// console.log(name);
// console.log(age);

// let a =10;
// let b=20;

// console.log(a + b);
// console.log(a - b);
// console.log(a * b);
// console.log(a / b);


// for (let i=0; i<=5; i++){
//     console.log(i);
// }

// function greet(name){
//     console.log("Hello "+ name);
// }
// greet("Punnet");

// function add(x,y){
//     console.log(x+y);
// }
// add(5,39);

// function multiply(x,y){
//     return x*y;
// }

// let result =multiply(5,6);
// console.log(result);

// let fruits = ["apple", "banana", "mango", "grapes"];
// for (let i=0; i<fruits.length; i++){
//     console.log(fruits[i]);
// }

// fruits.push("orange");
// console.log(fruits);



let heading = document.getElementById("heading");

let description = document.getElementById("description");

let button = document.getElementById("startBtn");


button.addEventListener("click", function() {

    heading.textContent = "Let's Start Learning!";

    description.textContent =
        "You are ready to learn JavaScript.";

    button.textContent = "Started";

});
<!-- supersimple.dev/projects/amazon/checkout -->

<!-- Number and Math -->

- Computer have a problem working with floats.
- Calculations with floats are sometimes inacurate.
- When working with money
- It's best practce to do the calc in cents
- and convert back to dollar from cents

```
20.95+7.99 - give an inaccurate result
to avoid this we can calculate like
(2095+799)/100
```

# What I have learn yet

```
In this lession:
1. Numbers and Math
2. Order of Operations, and Brackets(...)
3. Claculated the number in final project
4. Calculations using floats can be inaccurate
```

```
- How to convert 2.8 to 2
- Math.floor(2.8); // return 2
- Math.ceil(2.8) → rounds up to 3
- Math.round(2.8) → rounds to the nearest integer (3 in this case)
- Math.trunc(2.8) → removes the decimal part, returns 2
```

# Strings

- Checkout String.js for more details

# HTMl and CSS Review , Console.log

- We have added script tag at the bottom of body tag bcuz we want that web page will be created first then we will use JS to make it interactive

- If you want to learn HTMl and CSS then goto the Folder FullstackWebDevByHUXN -> HTML&CSSLearning
- If you want to make project then go to FrontendMentor and HTML&CSSProjects inside FULLStackWebDevbyHuXn

#### Comments

```
- This are the piece of code that JS will going to ignore it
- // :- This is a comment
- /*
  Multi-
  line
  Comment
  */
- Why we use Comments:-
  - Provide more information
  - If we don't want to run some piece of code for debuggin purpose.
```

# Variables

---

```
- What is a Variables ?
    - variable = a container
    - We can save a value like a number of strings inside a variable and then use it later
- Go to 05-Variables-> variables.htm file for more info
- we can save any type of value in a variables including strings

#### Variables name Restrictions:
  1. Can't use special words
    Example: let
  2. Can't start with a number
  3. Can't use special characters except: $ and _

- ; = end of an instruction ( Similar to a. in english)
- we need semi-colon(;) to separate instructions in Javascript
- we can't assing same variable name to let



```

- Goto Projects for exercises :- [Supuer Simple Dev](supersimple.dev/projects/variables)

### Variable re-assignment Shortcuts

- +=2 --> variable = variable + 2
- -=2 --> variable = variable - 2
- _=2 --> variable = variable _ 2
- /=2 --> variable = variable / 2
- ++ --> variable = variable + 1
- -- --> variable = variable - 1

### Naming Conventions

1. camelCase :- In this we combine the words together and capitalize every word except the first word (Standard naming convention in JS)
   eg: camelCase :- cartQuantity
2. PascalCase :- CartQuantity
3. kebab-case : cart-quantity

   - It doesn't work in JS , dash (-) is always a minus symbol
     however we use kebab-case in HTML and CSS and also in our file_name

4. snake_case : cart_quantity
   - It really used in other language but it's not really used in JS

### Ways to create a variables in JS

- There are three ways to create variables in Javascript
  1. let
  2. var
  3. const
  - We can't changes it's value, using const we are sure that it's value remain constant
  - Assignment to const variable is not valid
  - Best practice = use cosnt by default (only use let when we need to change the variable)

#### typeof

- It tells us the what type a value is

---

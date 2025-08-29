<!-- Master Javascript using HuXn youtube course From Zero to Fullstack -->

- 📘 [Javascript Course](https://www.youtube.com/watch?v=H3XIJYEPdus&t=1421s&ab_channel=HuXnWebDev)

# Master Javascript

### (General Guide)

#### 12. Connecting HTML and JavaScript

**Question:** How to connect HTML and JavaScript?

**Solution:**

The most common and recommended way to connect HTML and JavaScript is using the `<script>` tag.

**Methods:**

- **Inline `<script>`:** Embedding JavaScript directly within `<script>` tags in the HTML. (Not recommended for large scripts).

  ```html
  <script>
    // JavaScript code here
  </script>
  ```

- **External JavaScript File (Recommended):** Creating a separate `.js` file and linking it using the `src` attribute of the `<script>` tag.

  ```html
  <script src="path/to/your/script.js"></script>
  ```

**`<script>` Tag Placement:**

- **`<head>`:** Scripts are fetched and executed before the `<body>` is parsed. Use with `defer` or `async` for better performance.
- **`<body>` (before `</body>`):** Ensures HTML is parsed before scripts that manipulate the DOM are executed. Generally preferred.

**Attributes for External Scripts:**

- **`defer`:** Downloads the script in parallel with HTML parsing, but executes it after the HTML is parsed. Maintains script execution order.
- **`async`:** Downloads the script in parallel with HTML parsing and executes it as soon as it's downloaded (potentially interrupting HTML parsing). Execution order is not guaranteed.

**Best Practice:** Use external `.js` files linked with the `<script>` tag, ideally placed at the end of the `<body>` or using `defer` for scripts in the `<head>` that need to interact with the DOM.

- Console: It is an object inside that there are various method like console.table(), console.warn(), console.error()
- Comments:-
  - //
  - clg -> console.log() shortcuts

# Variables

- ** Variables **:- A quantity which value can be changed during the execution of the program is called variable.
  OR
- A variable is just a box where we can store our data and later if we want to reuse that data or maybe change that data so we can totally do that.

- Syntax:- (reserved keyword) (variable name) (type of value)
  - var, let and const
  - We can't use reserved keyword for our variable name
  - it can't be space separated variable name
  - Variable name can't be start with number
  - we can't use dash(-) separated variable name
  - we can use underscore separated \*kbab case0, camelcase , snakecase variable,
  - we use camelcase letter in JS mostly

# 13 Start the Amazon Project and Intro to Git

- Started the Final Amazon Project
- Set up and learned Git
- Learned themain idea of JavaScript
- Created list of products
- Made the "Add to Cart" button interactive

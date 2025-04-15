<!--  I am following Kevinpowell 21 days challenges for making responsive websites -->

# Check out Keving Powell Responsive layout 21 days challenges on [Kevin Powell challenge](https://courses.kevinpowell.co/view/courses/conquering-responsive-layouts/233004-day-1-using-percentages-avoiding-heights/678543-percentages-vs-fixed-widths).

# Day 1:-Using Percentages & avoiding Heights

### Percentages vs Fixed widths

    - If we don't set anything value then html code is responsive although it looks weird
    - Automatically take up 100% of the width of their parent container, unless a specific width is set.
    - More details:
        - Even though they take up the full width, their content doesn’t stretch unless you apply styles (like width, padding, etc.).

        - This default behavior is what makes block elements stack vertically.


    - Fixed Widths (px)
        Sets an exact size (e.g., 400px)

        ✅ Predictable layout across all devices

        ✅ Good for elements that shouldn't resize (e.g., logos, buttons)

        ❌ Not responsive — does not adapt to screen size

        ❌ Can cause overflow issues on smaller screens
    - Percentage Widths (%)
        Sets size relative to the parent container

        ✅ Responsive — adjusts with screen/container size

        ✅ Ideal for fluid layouts and mobile-friendly designs

        ❌ Can be tricky to manage without constraints (like max-width)

        ❌ Layout may break if parent container isn't sized correctly

### Percentages on the child

    - It's always a relationship b/w parent and child element, width % of child is relative to its parent
    - Width (width: %)
        ✅ Relative to the parent’s width

        📦 Common for responsive layouts

        Example: width: 50% → Half the parent’s width

    - Height (height: %)
        ✅ Relative to parent’s height

        ⚠️ Works only if parent has an explicit height

        ❌ Doesn’t work if parent’s height is auto

    - Padding & Margin in %
        ✅ Always based on the parent’s width (even vertical ones)

        🧠 Useful trick for maintaining aspect ratios

        Example: padding-top: 100% → makes a square if width is 100%

    -  Font-size, border-radius, etc.
        ❌ % not commonly used or supported here

        Use em, rem, or absolute units instead

### Why it's a good idea to avoid heights

    - Avoid using heights
    - try to use padding instead that will give us more backgrounds and use 'em or rem' instead of 'px'
    - Websites itself is responsive but using our own css we make it unresponsive

### Challenge#1

    - Go top Day 1 folder to look for my solution and challenge 1 as well

### Day2:- Getting Familiar with Relative heights

# 📐 CSS Relative Units Guide

This guide outlines the most commonly used **relative units in CSS**, explaining when to use each one and why.

---

## 🧰 Relative Units Overview

| Unit            | Based On                        | Use Case                                      | Why Use It                                  |
| --------------- | ------------------------------- | --------------------------------------------- | ------------------------------------------- |
| `em`            | Parent element’s font-size      | Padding, margins, font-size inside components | Scales with parent, flexible for components |
| `rem`           | Root element (`html`) font-size | Global spacing, typography                    | Consistent and predictable scaling          |
| `%`             | Parent container                | Widths, heights, padding                      | Fluid layouts, responsive containers        |
| `vw`            | 1% of viewport width            | Hero sections, responsive headings            | Adapts to screen size                       |
| `vh`            | 1% of viewport height           | Fullscreen layouts, modals                    | Ideal for vertical scaling                  |
| `vmin` / `vmax` | Smaller/larger of `vw`/`vh`     | Responsive typography or layouts              | Auto-scales based on viewport dimension     |
| `ch`            | Width of "0" character          | Controlling text width                        | Great for readable line lengths             |

---

## ✅ Best Practices

### 🔤 Typography & Spacing

Use `rem` for most font sizes, padding, and margins:

````css
body {
  font-size: 1rem; /* base size */
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}


# Day3 : Max-width

    - As we saw, setting a fixed width on an element tends to be a bad idea. Instead we can use percentages, which make our lives easier.

    - The only issue with this is, at large screens, things can get too big. Thankfully, we have max-width that can help us out!
# 📏 Understanding `max-width` in CSS

The `max-width` property is an essential part of creating responsive, readable, and well-structured layouts in CSS. This section explains **why** you should use it and how to apply it effectively.

---

## ❓ What is `max-width`?

`max-width` sets the **maximum width** an element can grow to — but allows it to be smaller if needed.

```css
.container {
  max-width: 1200px;
}

    - Why Use max-width?
    - Benefit	Description
    - 🧠 Readability	Prevents text and content from stretching too wide on large screens
    - 📱 Responsiveness	Works perfectly with fluid layouts (like width: 100%)
    - 💻 Centering Layouts	Commonly used with margin: 0 auto to center content
    - 🔐 Control Layout Flow	Helps keep consistent and clean designs, especially in full-width containers
````

# Challenge 2

- Go to Day3 Folder to look for challenge 2 solution

# Day4

## CSS Viewports

Sure! Here's a detailed `README.md` file explaining the CSS units `vw`, `vh`, `vmin`, and `vmax` in a clean and beginner-friendly way.

---

````markdown
# 📐 CSS Viewport Units: `vw`, `vh`, `vmin`, `vmax`

CSS viewport units are relative units of measurement based on the **size of the browser viewport** (the visible area of a web page). They are incredibly useful for creating **responsive layouts** without relying on media queries.

---

## 🌐 What is the Viewport?

The **viewport** is the visible area of a web page in the browser window. When you resize the window, the viewport size changes. Viewport units let you size elements based on that changing size.

---

## 📏 Units Overview

| Unit   | Description                                         | Example                         |
| ------ | --------------------------------------------------- | ------------------------------- |
| `vw`   | 1% of the viewport **width**                        | `50vw` = 50% width              |
| `vh`   | 1% of the viewport **height**                       | `100vh` = full height           |
| `vmin` | 1% of the **smaller** of viewport's width or height | `50vmin` adapts to smaller side |
| `vmax` | 1% of the **larger** of viewport's width or height  | `80vmax` adapts to larger side  |

---

## 🔍 Detailed Explanation

### 📏 `vw` — Viewport Width

- `1vw` = 1% of the width of the viewport.
- Useful for scaling text or containers relative to screen width.

```css
.container {
  width: 50vw; /* 50% of the viewport width */
}
```
````

---

### 📏 `vh` — Viewport Height

- `1vh` = 1% of the height of the viewport.
- Commonly used for full-page sections or modals.

```css
.hero-section {
  height: 100vh; /* Fills the full visible height */
}
```

---

### 📏 `vmin` — Viewport Minimum

- `1vmin` = 1% of the smaller of viewport width or height.
- Keeps elements proportional regardless of screen orientation.

```css
.box {
  width: 50vmin;
  height: 50vmin; /* Maintains a square shape on any screen */
}
```

---

### 📏 `vmax` — Viewport Maximum

- `1vmax` = 1% of the larger of viewport width or height.
- Useful for large-scale backgrounds or typography.

```css
.heading {
  font-size: 5vmax; /* Scales with the larger side */
}
```

---

## 💡 When to Use Them

| Use Case              | Recommended Unit |
| --------------------- | ---------------- |
| Full screen height    | `100vh`          |
| Responsive width      | `vw`             |
| Maintain aspect ratio | `vmin`           |
| Big text scaling      | `vmax`           |

---

## 🧪 Example

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <style>
      body {
        margin: 0;
      }
      .section {
        width: 100vw;
        height: 100vh;
        background-color: lightblue;
      }
      .text {
        font-size: 5vmin;
        text-align: center;
        padding-top: 40vh;
      }
    </style>
  </head>
  <body>
    <div class="section">
      <div class="text">Responsive Text with vmin</div>
    </div>
  </body>
</html>
```

---

## 📱 Browser Compatibility

✅ Supported in all modern browsers:

- Chrome
- Firefox
- Safari
- Edge

❗️For older mobile browsers, use fallbacks or combine with `media queries`.

---

## 🧠 Tips & Gotchas

- On mobile browsers, `100vh` may include the address bar—be careful with full-screen layouts.
- Combine `vmin`/`vmax` with `em` or `rem` for more predictable typography.
- Always test on multiple screen sizes.

---

## 📚 Resources

- [MDN Web Docs – Viewport Units](https://developer.mozilla.org/en-US/docs/Web/CSS/length)
- [CSS Tricks – Viewport Units](https://css-tricks.com/the-lengths-of-css/)

---

# Day 5

# Challenge 3

- Checkout Solution in Day 5 folder

# Day 6

# Review of the first week

```
Review of the first week
In this first week, we've looked at:
Using percentages for widths
Avoiding to set heights
Using max-width

While there is nothing overly complicated with any of that, being comfortable with these things is the key to mastering responsive layouts.

With a good understanding of the above, all we need is a little flexbox and we're going to start knocking even complex layouts out of the park!

In this section of the course, you can find a few links to some extra reading that you can do if you're looking to continue learning a bit. They'll help supplement what we're covering here, but none of it is required reading 😊.

I'll be sharing my solution to the challenge tomorrow. If you're a little bit behind at this point, you can use today and tomorrow to catch up a little.

Next week, we'll be jumping into flexbox and how we can use it with what we've already learned to make our layouts. We'll be looking at both the macro-scale with a page's layout, as well as the more micro-scale in putting together a common navbar component.

```

# Why you shouldn't use em's for font-size

- It compounds on each other reltive to its parent
- Child's element always get mutiply it's parent's font-size every times as we go down in hierarchy for font-sizes

# A Tale of width and max-width

- [lookout this video for your reference](https://courses.kevinpowell.co/view/courses/conquering-responsive-layouts/257597-day-6-review/740862-a-tale-of-width-and-max-width)
- Look Day 6 folder to understand this point

```Important Notes
An interesting look at the two properties, and how they might not always act the way you think they will.

As it says, the second one is the easier one to understand, just like we looked at, so I plan on sticking with that one
```

# Day 7

# Challenge 3 Solution by Kevin Powell

- Checkout folder Day 7
- [Box-sizing border-box](https://www.youtube.com/watch?v=WlGQdgy-M6w&ab_channel=KevinPowell)
- [BEM naming conventions](https://www.youtube.com/watch?v=SLjHSVwXYq4&ab_channel=KevinPowell)
- We use , box-sizing border-box bcuz by defaults its's a content-box and whaterver we are adding in content-box like broder ord padding it addon to the width of it. and takign extra spaces

### Use BEM naming conventions

- it stands for Block Element modifier
- Like text are part of card block so we can use \_\_ naming conventions for that

---

Absolutely! Here's a `README.md` file explaining the use of the **BEM naming convention** in a project, perfect for documentation or sharing with a team:

---

```markdown
# 🧱 BEM Naming Convention for CSS

This project uses the **BEM (Block-Element-Modifier)** naming convention for writing CSS. BEM is a methodology that helps you create reusable, scalable, and easy-to-maintain front-end code.

---

## 📖 What is BEM?

BEM stands for:

- **Block**: A standalone entity that is meaningful on its own (e.g. `button`, `form`, `nav`)
- **Element**: A part of a block that has no standalone meaning (e.g. `button__icon`, `form__input`)
- **Modifier**: A flag on a block or element that changes its appearance or behavior (e.g. `button--primary`, `form__input--error`)

### 📌 Syntax
```

.block {}
.block**element {}
.block--modifier {}
.block**element--modifier {}

````

---

## ✅ Benefits of Using BEM

- **Clear structure**: You immediately understand what a class is for.
- **Avoids naming conflicts**: Each class is scoped to its component.
- **Component-friendly**: Works great with React, Vue, or any modular architecture.
- **Easy to scale**: BEM scales well for large teams and large codebases.
- **Improved maintainability**: Predictable and readable CSS makes long-term maintenance easier.

---

## 🛠 Example

```html
<!-- HTML -->
<div class="card card--featured">
  <h2 class="card__title">BEM is awesome</h2>
  <p class="card__description">A short intro to the BEM naming convention.</p>
</div>
````

```css
/* CSS */
.card {
  padding: 1rem;
  background-color: white;
}

.card--featured {
  border: 2px solid gold;
}

.card__title {
  font-size: 1.5rem;
  font-weight: bold;
}

.card__description {
  color: #666;
}
```

---

## 🧪 When to Use What

| Type     | Purpose                          | Example            |
| -------- | -------------------------------- | ------------------ |
| Block    | Base component                   | `.button`          |
| Element  | Child of a block                 | `.button__icon`    |
| Modifier | Style variation of block/element | `.button--primary` |

---

## 👎 Things to Avoid

- Don’t nest elements unnecessarily: `block__element__element` is invalid.
- Avoid generic class names like `.red` or `.big`.
- Don’t use tag names in class names (e.g. `.div__title`).

---

## 📂 Recommended Folder Structure

```bash
styles/
├── base/
├── components/
│   ├── _button.scss
│   ├── _card.scss
├── main.scss
```

Each component uses its own BEM-structured styles for modularity.

---

## 🧠 TL;DR

Use BEM for:

- Readable and maintainable CSS
- Preventing class name collisions
- Creating scalable and consistent design systems

---

# Day 8 Flexbox Basics

- Design Specs [link](https://courses.kevinpowell.co/view/courses/conquering-responsive-layouts/260392-day-8-flexbox-basics/750307-flexbox-challenge-1-design-specs)

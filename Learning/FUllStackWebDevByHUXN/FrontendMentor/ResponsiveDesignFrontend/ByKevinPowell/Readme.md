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

    - Go top Day 1 folder to look for my solution and challenge 1

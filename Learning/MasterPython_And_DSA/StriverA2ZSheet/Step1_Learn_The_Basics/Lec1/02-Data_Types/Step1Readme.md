<!--  Primitive Data Types vs Non Primitive Data Types in Python -->

# Primitive Data Types vs Non Primitive Data Types in Python

- Python, known for its versatility and user-friendliness, is a dynamic language that doesn't explicitly categorize data types into primitive and non-primitive as some languages like Java do. However, for clarity and understanding, it's useful to draw parallels and discuss similar concepts.

- Primitive data types in Python are the most basic types of data. They are the building blocks for data manipulation in Python and are typically immutable, meaning their value cannot change after they are created. Here are the main primitive data types in Python:

### Examples of Primitive Data Types

- Integer (int) :
  - Represents whole numbers.
  - Example: x = 10
- Float (float) :
  - Represents floating-point numbers (decimal values).
  - Example: y = 10.5
- Boolean (bool) :
  - Represents True or False values.
  - Example: is_active = True
- String (str) :
  - Represents a sequence of characters.
  - Example: name = "Alice"

```
x = 10              # Integer
y = 10.5            # Float
is_active = True    # Boolean
name = "Alice"      # String

print(type(x))
print(type(y))
print(type(is_active))
print(type(name))

output:-
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'str'>
```

# What are Non-Primitive Data Types in Python?

- Non-primitive data types, also known as complex or composite data types, are data types that are derived from primitive data types. They can store multiple values or more complex structures of data. Unlike primitive types, non-primitive data types are mutable, meaning their contents can be changed.

- Examples of Non-Primitive Data Types
- List (list) :
  - Ordered collection of items, which can be of different types.
  - Example: numbers = [1, 2, 3, 4]
- Tuple (tuple) :
  - Similar to lists, but immutable.
  - Example: coordinates = (10.0, 20.0)
- Dictionary (dict) :
  - Collection of key-value pairs.
  - Example: person = {"name": "Alice", "age": 30}
- Set (set) :
  - Unordered collection of unique items.
  - Example: unique_numbers = {1, 2, 3, 4}
- String (str) :
  - While strings are technically primitive in Python, they can also be considered non-primitive when used to store complex data or collections of characters.

```
numbers = [1, 2, 3, 4]            # List
coordinates = (10.0, 20.0)        # Tuple
person = {"name": "Alice", "age": 30}  # Dictionary
unique_numbers = {1, 2, 3, 4}     # Set

print(type(numbers))
print(type(coordinates))
print(type(person))
print(type(unique_numbers))


output:-
<class 'list'>
<class 'tuple'>
<class 'dict'>
<class 'set'>
```

- Differences Between Primitive and Non-Primitive Data Types in Python
  ![D/B Primitive and Non-Primitive Data Types](/Learning/MasterPython_And_DSA/StriverA2ZSheet/Step1_Learn_The_Basics/image.png)

# When to Use Primitive Data Types in Python ?

- Primitive data types are best used when:

- Simple Data Storage: When you need to store simple, single values such as integers or floats.
- Performance Considerations: They are typically faster and use less memory, making them ideal for high-performance applications.
- Basic Operations: When your operations are limited to basic arithmetic or boolean logic.

# When to Use Non-Primitive Data Types in Python ?

- Non-primitive data types are suitable for:

- Complex Data Storage: When you need to store collections of data, such as lists of items or key-value pairs.
- Flexibility and Mutability: They allow changes to the data without creating new objects, which is useful in scenarios where data needs to be updated frequently.
- Data Relationships: When you need to represent more complex relationships, such as a dictionary mapping keys to values or a set of unique items.

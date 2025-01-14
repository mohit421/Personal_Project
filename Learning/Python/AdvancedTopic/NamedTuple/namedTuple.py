# namedTuple

# We can think of namedtuple a lightweight object works just like a regular tuple its more readble

# Example
# list / tuple
# color = (55,155,255)

# dictionary
# color = {'red': 55, 'green': 155, 'blue': 255}
# print(color['red'])

# namedtuple
# This is good compromise b/w tuple and dictionary , b/w readability and also give functionality of tuple
# from collections import namedtuple
# Color = namedtuple('Color', ['red', 'green', 'blue'])
# color = Color(55,255,255)
# # can be use ad tuple
# print(color[0])
# print(color.red)

# Another exapmle----------------------------

# from collections import namedtuple
# Color = namedtuple('Color', ['red', 'green', 'blue'])
# color = Color(blue=55,green=155,red=255)

# white = Color(255,255,255)
# print(color[0])
# print(white.blue)


# _____________________Example

from collections import namedtuple
# Position = namedtuple('Coordinate', ['x', 'y'])
# p1 = Position(1, 3)
# print(p1)









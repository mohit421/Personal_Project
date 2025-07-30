
# /////////////// Strings - Working with Textual Data            ////////////



# message = "Hellp World"
message = 'Hello World'

print(message)

# we will getting error while running
# message1 = 'bobby's world'

# print(message1)

# to handle above error
message2 = "bobby's world"
print(message2)

# multi line string 
message3 = """Bobby's world was good
cartoon in the 1990s"""
print(message3)


print(len(message))

#  we can access string character individually
#  1st character started with 0
print(message[0])

# access index 11
# print(message[11]) # we give index out  of range

print(message[0:5])

# Slicing video
print(message[:5])

print(message[6:])

# string methods

print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('World')) 
print(message.find('Universe')) # gives -1 i.e., it doesn't exist 

print(message.replace('World', 'Universe'))
print(message)

# We need new variable to get that returned string with those replacements,

new_message = message.replace('World', 'Universe')
print(new_message)

# concatenation

greeting = 'Hello'
name = 'Corey'
message = greeting +" " +  name 
print(message)

message = greeting + ", " + name + '. Welcome!'
print(message)

#  it's better to use format string
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# F-String

message = f'{greeting}, {name}. Welcome!'
print(message)


message = f'{greeting}, {name.upper()}. Welcome!'
print(message)


print(dir(name))

# print(help(str))


print(help(str.lower))


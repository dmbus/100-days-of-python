# Day 001
# Working with variables in python to manage data

# print() function

print("Hello world!")

name = "Lee"
print(f'Hello, {name}!')

# coding exercise
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print(\"what to print\")")

# calculate the length of the username
name = input("Enter your name: ")
print(f'The length of {name} is {len(name)} symbols.')

# same function in one line
print(len(input("Enter your name: ")))

# coding exercise - switching variables
a = input("a: ")
b = input("b: ")
print(f'a: {a}, b: {b}')
a, b = b, a # variables are switched
print(f'a: {a}, b: {b}')

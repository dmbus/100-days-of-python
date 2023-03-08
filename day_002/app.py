# Day 002
# Understanding data types and how to manipulate strings

# strings
greeting = "Hello world!"
print(type(greeting))  # <class 'str'>
print(greeting[0])  # H

# integer
radius = 30
print(type(radius))  # <class 'int'>

# float 
pi = 3.1415
print(type(pi))  # <class 'float'>

# boolean
is_Admin = True
print(type(is_Admin))  # <class 'bool'>

# type conversion
print("Radius is ", str(radius))
print("The length of the road is", float(100.55), "km")

# coding exercise
two_digit = input("Enter two-digit number: ")
sum = int(two_digit[0]) + int(two_digit[1])
print(f'The sum of {two_digit} numbers is {sum}.')

# math operators
print(f'3+3 = {3 + 3}')
print(f'3-3 = {3 - 3}')
print(f'3*3 = {3 * 3}')
print(f'3/3 = {3 / 3}')
print(f'3**3 = {3 ** 3}')
print(f'10//3 = {10 // 3}')
print(f'10%3 = {10 % 3}')

# order of operations
print(3 * 3 + 3 / 3 - 3)

# bmi calculator
print("Welcome to BMI Calculator!")
weight = input("What is your weight (kg)?\n")
height = input("What's your height (cm)?\n")
bmi = int(weight) / (float(height) / 100) ** 2
# print(bmi)
print(f'Your BMI is {"%.2f" % bmi}.')

# coding exercise - life in weeks
print("-" * 20)
print("Welcome to the life in weeks")
age = int(input("Your age in years: "))
left = 90 - age
days = age * 365
weeks = age * 52
months = age * 12

left_days = left * 365
left_weeks = left * 52
left_months = left * 12

print(f'Your age is {days} days, {weeks} in weeks or {months} in months.')
print(f'Your have {left_days} days, {left_weeks} in weeks or {left_months} in months until 90.')

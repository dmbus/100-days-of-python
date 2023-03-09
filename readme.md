# 100 Days of Code
_@ by Angela Yu_

## Day 001

**print()**
```py
print("Hello world!")
```
**using variable**
```pycon
name = "Lee"
print(f'Hello, {name}!')
```

**len()**
```pycon
# calculate the length of the username
name = input("Enter your name: ")
print(f'The length of {name} is {len(name)} symbols.')
```
**input()**
```py
# same function in one line
print(len(input("Enter your name: ")))
```
**change variables' values**
```py
# coding exercise - switching variables
a = input("a: ")
b = input("b: ")
print(f'a: {a}, b: {b}')
a, b = b, a # variables are switched
print(f'a: {a}, b: {b}')
```
**final project**
```py
# band name generator
print("Welcome to the Band Name Generator.")
city_name = input("What's name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
print(f'Your band name is {city_name}\'s {pet_name}.')
```

## Day 002
_Understanding data types and how to manipulate strings_

**strings**
```pycon
greeting = "Hello world!"
print(type(greeting))  # <class 'str'>
print(greeting[0])  # H
```

**integer**
```py
radius = 30
print(type(radius))  # <class 'int'>
```

**float**
```pycon
pi = 3.1415
print(type(pi))  # <class 'float'>
```

**boolean**
```pycon
is_Admin = True
print(type(is_Admin))  # <class 'bool'>
```

**type conversion**
```py
radius = 14
print("Radius is ", str(radius))
print("The length of the road is", float(100.55), "km")
```

**coding exercise**
```py
two_digit = input("Enter two-digit number: ")
sum = int(two_digit[0]) + int(two_digit[1])
print(f'The sum of {two_digit} numbers is {sum}.')
```

**math operators**
```py
print(f'3+3 = {3 + 3}')
print(f'3-3 = {3 - 3}')
print(f'3*3 = {3 * 3}')
print(f'3/3 = {3 / 3}')
print(f'3**3 = {3 ** 3}')
print(f'10//3 = {10 // 3}')
print(f'10%3 = {10 % 3}')
```

**bmi calculator**
```py
print("Welcome to BMI Calculator!")
weight = input("What is your weight (kg)?\n")
height = input("What's your height (cm)?\n")
bmi = int(weight) / (float(height) / 100) ** 2
print(f'Your BMI is {"%.2f" % bmi}.')
```

**coding exercise - life in weeks**
```py
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
```

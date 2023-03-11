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


## Day 004
**List and List's methods**

[List documentation](https://docs.python.org/3/tutorial/datastructures.html)


**list.append(x)**

    Add an item to the end of the list. Equivalent to a[len(a):] = [x].

**list.extend(iterable)**

    Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

**list.insert(i, x)**

    Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

**list.remove(x)**

    Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

**list.pop([i])**

    Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

**list.clear()**

    Remove all items from the list. Equivalent to del a[:].

**list.index(x[, start[, end]])**

    Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

    The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

**list.count(x)**

    Return the number of times x appears in the list.

**list.sort(*, key=None, reverse=False)**

    Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

**list.reverse()**

    Reverse the elements of the list in place.

**list.copy()**

    Return a shallow copy of the list. Equivalent to a[:].



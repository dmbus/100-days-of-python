# Day 003
# Conditional statements,
# Logical operators,
# Code blocks and scopes

# IF / ELIF / ELSE
height = int(input("Enter your height: "))
if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# coding exercise - odd/even
number = int(input("Enter the integer number: "))
if number % 2 == 0:
    print("You entered the integer number.")
else:
    print("You entered the odd number.")

# nested if/elif statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("How old are you? "))
    if age < 12:
        print("The price is $5.")
    elif age <= 18:
        print("The price is $7.")
    else:
        print("The price is $12.")
else:
    print("You are not tall enough. Sorry.")

# coding exercise - BMI with description
height = int(input("What's your height in cm? "))
weight = int(input("What's your weight in kg? "))

bmi = weight / (height/100) ** 2

print(f"Your bmi index is {'%.2f' % bmi}.")


if bmi >= 35:
    feedback = "clinically obese"
elif bmi >= 30:
    feedback = "obese"
elif bmi >= 25:
    feedback = "overweight"
elif bmi >= 18.5:
    feedback = "normal weight"
elif bmi < 18.5:
    feedback = 'underweight'
else:
    feedback = "martian"
print(f"You are {feedback}. Now live with it or change it. Everything in your hands =)")

# coding exercise Leap year
year = int(input("Enter the year: "))
if (year % 4 == 0 or year % 400 == 0) and not year % 100 == 0:
    leap = True
else:
    leap = False
leap_year = "leap" if leap else "not leap"
print(f"{year} is {leap_year}.")
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
        ticket_price = 5
    elif age <= 18:
        ticket_price = 7
    else:
        ticket_price = 12
    photo = input("Do you want to have a photo: Y or N? ")
    if photo.lower() == "y":
        ticket_price += 3
    print(f"The price is ${ticket_price}.")


else:
    print("You are not tall enough. Sorry.")

# coding exercise - BMI with description
height = int(input("What's your height in cm? "))
weight = int(input("What's your weight in kg? "))

bmi = weight / (height / 100) ** 2

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

# coding exercise - pizza order
print("-" * 20)
print("Welcome to martian's pizza club!")
print("What size of pizza do you want?")
pizza_size = input("s - small \n"
                   "m - medium \n"
                   "l - large size")
pepperoni = input("Do you want extra pepperoni Y / N? ")
cheese = input("Do you want extra cheese Y / N? ")
pizza_price = 0
if pizza_size.lower() == "s":
    pizza_price += 15
elif pizza_price.lower() == "m":
    pizza_price += 20
elif pizza_price == "l":
    pizza_price += 25

if pepperoni.lower() == "y" and pizza_size.lower() == "s":
    pizza_price += 2
elif pepperoni.lower() == "y":
    pizza_price += 3

if cheese.lower() == "y":
    pizza_price += 1

print(f"The price of the pizza is {ticket_price}.")

# Logical operators
# A and B
# A or B
# not A

# coding exercise TRUE LOVE
TRUE = "true"
LOVE = "love"

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")


def count(counter, *names):
    sum = 0
    for name in names:
        for letter in name.lower():
            if letter in counter:
                sum += 1
    return sum


true_count = count(TRUE, name1, name2)
love_count = count(LOVE, name1, name2)

result = str(true_count) + str(love_count)
print(f"Your final result is {result}!")


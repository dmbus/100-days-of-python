# Day 002
# Tip calculator

# Task
# If the bill was $150.00, split between 5 people, with 12% tip.
#
# Each person should pay (150.00 / 5) * 1.12 = 33.6
#
# Format the result to 2 decimal places = 33.60
#
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
#
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

print("Welcome to the Tip calculator!")

bill = float(input("How much is the bill? "))
people = int(input("How many people to share? "))
tip = 0.12

total_bill = bill * (1 + tip)
payment = total_bill / people

print(f'The total bill is {"%.2f" % total_bill} and each person should pay {"%.2f" % payment}.')

# another way of format
print("{:.3f}".format(payment))
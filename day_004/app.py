import random
from my_module import pi

# sales = []
#
# for i in range(100):
#     sales.append(random.randint(1, 100))
#
# print(sales)
#
# print(f"This is imported from my module: {pi}")
#
# print(random.random() * 5)
#
# # head or tail ver 1
# options = ['Head', 'Tail']
# print(random.choice(options))
#
# # head or tail ver 2
# head_tail_choice = random.randint(0,1)
# if head_tail_choice == 1:
#     print('Head')
# else:
#     print('Tail')
#
# # python lists
#
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#
# print(states_of_america)
# print(states_of_america[0]) # first item in the list
# print(states_of_america[-1]) # last item in the list
#
# default_list = []
# default_list.append("added item")
# default_list.extend(["first item", "second item", "third item"])

# coding exercise - who pays the bill

members = input("Enter members of the dinner - split them by space:\n")
member_list = members.split(" ")
who_pays = random.choice(member_list)
print(f"{who_pays} pays the bill.")




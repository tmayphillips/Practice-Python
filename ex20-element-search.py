import random

numbers = [2,4,6,8]
number = random.randint(0,9)
print(number)

truth_value = number in numbers
if (truth_value):
    print("The number is included")
else:
    print("The number is not listed")
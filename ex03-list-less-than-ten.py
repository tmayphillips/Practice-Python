a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

for index in a:
    if index < 5:
        print(index)

for index in a:
    if index < 5:
        new_list.append(index)

print(new_list[::])

user_list = []

number = int(input("Enter a number: "))

for index in a:
    if index < number:
        user_list.append(index)

print(user_list[::])
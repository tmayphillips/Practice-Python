a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = []

for value in a:
    if value % 2 == 0:
        new_list.append(value)

print(new_list)
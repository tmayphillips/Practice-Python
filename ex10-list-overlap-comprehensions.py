import random
count_a = random.randint(1,15)
count_b = random.randint(1,15)

a = []
b = []

while len(a) <= count_a:
    a.append(random.randint(0,25))

while len(b) <= count_b:
    b.append(random.randint(0,25))

common = []

for value in a:
    if value in b:
        if value in common:
            next
        else:
            common.append(value)

print(a)
print(b)
print(common)

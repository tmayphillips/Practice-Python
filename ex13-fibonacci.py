count = int(input("Enter the number of fibonacci numbers you desire: "))
fibonacci = [1,1]
i = 1

while i <= (count - 2):
    fibonacci.append(fibonacci[(i-1)] + fibonacci[i])
    i = i + 1

print(fibonacci)
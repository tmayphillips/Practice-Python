number = int(input("Enter a number: "))
div = number
divisors = []

while div > 0:
    if number % div == 0:
        divisors.append(div)
        div = div -1
    else:
        div = div - 1

print(divisors)
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

if number % 4 == 0:
    print("Divisible by 4")

num = int(input("Enter 1st number: "))
check = int(input("Enter 2nd number: "))

if num % check == 0:
    print("Divisible")
else:
    print("Not divisible")
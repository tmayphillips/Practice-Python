name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = 2019 - age + 100

def print_display():
    print(f"{name}, you will turn 100 in {year}.")

print_display()

copies = int(input("Enter the number of copies: "))

while copies > 0:
    print_display()
    if copies > 1:
        print("\n")
    copies = copies - 1
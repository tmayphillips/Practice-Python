import random
a = random.randint(1, 9)

guess =(input("Enter a number between 1 and 9: "))
count = 0
win = False

while win == False:
    if guess == "exit":
        break
    if int(guess) == a:
        count = count + 1
        print(f"You won! It took you {count} guesses")
        break
    if int(guess) < a:
        count = count + 1
        print("Too low")
        guess = (input("Enter another number: "))
    if int(guess) > a:
        count = count + 1
        print("Too high")
        guess = (input("Enter another number: ")) 
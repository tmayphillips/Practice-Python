import random
low = 0
high = 100
count = 0
win = False


while win == False:
    guess = random.randint(low,high)
    print(guess)
    answer = input("Enter higher, lower, or correct: ")
    if answer == "higher":
        count = count + 1
        low = guess + 1
    if answer == "lower":
        count = count + 1
        high = guess - 1
    if answer == "correct":
        count = count + 1
        win = True
        print(f"Correct! It took you {count} guesses.")
import random
number = str(random.randint(0,9999))
user_guess = []
lenghth_of_number = 4

def user_input():
    user_guess = input("Enter a 4 digit number: ")
    if user_guess == "quit":
        exit
    else:
        get_count(number,user_guess)

def get_count(number, user_guess):
    cow = 0
    bull = 0
    i = 0
    while i < lenghth_of_number:
        if number[i] == user_guess[i]:
            cow+=1
            i += 1
        elif number[i] in user_guess:
            bull+=1
            i += 1
        else:
            i += 1
    
    if cow == 4:
        print("You won!")
    else:
        print(cow,bull)
        user_input()
   


user_input()
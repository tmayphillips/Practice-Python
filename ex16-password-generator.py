import secrets
import random

password_stength = input("Do you want your password to be strong or weak: ")
password = ""
choices = ["dog","cat","bird"]

if password_stength == "strong":
    password = secrets.token_urlsafe(16)
elif password_stength == "weak":
    password = random.choice(choices)

print(password)
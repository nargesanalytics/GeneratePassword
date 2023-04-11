import random


#define lenght of password
length= 16


# Ask the user for the types of characters to include in the password

lowercase=input("include lowercase in? (y/n): ").lower() == 'y'
uppercase=input("include uppercase in? (y/n): ").lower() == 'y'
digits=input("include digits in? (y/n): ").lower() == 'y'
punctuation = input("Include punctuation? (y/n): ").lower() == 'y'

#define character of password
characters=""
if lowercase :
    characters += 'abcdefghijklmnopqrstuvwxyz'
if uppercase:
    characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if digits:
    characters += '0123456789'
if punctuation:
    characters += r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


# generate password
while True:
    password = ''.join(random.choice(characters) for i in range(length))
    if (lowercase and any(c.islower() for c in password)
            and uppercase and any(c.isupper() for c in password)
            and digits and sum(c.isdigit() for c in password) >= 3
            and punctuation and any(c in characters for c in password)):
        break
print(password)
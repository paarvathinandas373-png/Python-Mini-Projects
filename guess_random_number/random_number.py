import random
secret_number = random.randint(0,100)
print("Welcome to Number Guessing Game!")
while True:
    number = int(input("Enter a number between 0 and 100: "))
    if secret_number == number:
        print("Congrulation! You have Guessed the number right!")
        break
    elif number <= secret_number:
        print("The number is Too LOW")
    else:
        print("The number is Too HIGH")    
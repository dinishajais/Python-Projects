import random

secret_number=random.randint(1,100)
attempts=0

try:
    while True:
        try:
            user_guess=int(input("Enter a number: "))
        except ValueError:
            print("<Enter a valid number >")
            attempts+=1
            continue
        attempts+=1

        if user_guess==secret_number:
            print(f"Bingo !! Correct guess in {attempts} attempt")
            break
        elif user_guess<secret_number:
            print("Too low !! Try again")
        else:
            print("Too high !! Try again")
except:
    print("An exception has occured")




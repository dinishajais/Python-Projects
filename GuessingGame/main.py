import random

def get_user_guess():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        print("<Enter a valid number >")
        return None

def check_guess(secret_number,user_guess):
    if user_guess==secret_number:
        return "CORRECT"
    elif user_guess<secret_number:
        print("Too low !! Try again")
        return "LOW"
    else:
        print("Too high !! Try again")
        return "HIGH"

        
def play_game():
    attempts=0
    secret_number=random.randint(1,100)

    while True:

        user_guess=get_user_guess()
        if(user_guess is None):
            continue
        attempts+=1
        result=check_guess(secret_number,user_guess)
        if(result=="CORRECT"):
            print(f"Bingo !! Correct guess in {attempts} attempt")
            break

def main():
    play_game()

main()

        

        





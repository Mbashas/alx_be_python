import random

# Initialize to start first game
play_again = "yes"  

while play_again in ["yes", "y"]:
    secret_number = random.randint(1, 3)
    
    guess = int(input("Enter your guess: "))
    n = 0

    while guess != secret_number:
        match guess:
            case _ if guess > secret_number: 
                print("Too high")
            case _ if guess < secret_number:
                print("too low")
            case _:
                print("Not a value, choose between 0-3")

        n+=1
        guess = int(input("Enter your guess: "))

    # When correct guess is made
    n+=1
    print(f"Right\nAttempts {n}")
    
    # Ask if they want to play again
    play_again = input("Do you want to play again (yes/no)? ").lower()

print("See yaa!")
     
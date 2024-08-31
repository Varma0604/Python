import random

def guess_number():
    # Define the range of possible numbers
    lower_bound = 1
    upper_bound = 100
    
    # Initialize variables
    guess = random.randint(lower_bound, upper_bound)
    attempts = 1
    
    print("Let's play a number guessing game!")
    print("You just need to tell me if my guess is correct, too high, or too low.")
    
    # Game loop
    while True:
        print(f"My guess is: {guess}")
        response = input("Is my guess correct (C), too high (H), or too low (L)? ").upper()
        
        if response == 'C':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts!")
            break
        elif response == 'H':
            upper_bound = guess - 1
            guess = random.randint(lower_bound, upper_bound)
        elif response == 'L':
            lower_bound = guess + 1
            guess = random.randint(lower_bound, upper_bound)
        else:
            print("Invalid response. Please enter 'C' for correct, 'H' for too high, or 'L' for too low.")
            continue
        
        attempts += 1

# Call the function to start the game
guess_number()

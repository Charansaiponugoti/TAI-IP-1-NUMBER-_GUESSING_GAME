import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game! Can you guess the number?")
    
    # Ask the user to guess the number
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if guess < 1 or guess > 100:
                raise ValueError("Guess out of range")
            break
        except ValueError as e:
            print(e)
    
    # Check if the guess is correct
    while guess != number_to_guess:
        if guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        while True:
            try:
                guess = int(input("Enter your guess (between 1 and 100): "))
                if guess < 1 or guess > 100:
                    raise ValueError("Guess out of range")
                break
            except ValueError as e:
                print(e)
    
    print("Congratulations! You guessed the correct number.")

number_guessing_game()

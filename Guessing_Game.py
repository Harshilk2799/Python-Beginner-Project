import random 

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Take a guess: ")) 

        # Check if the guess is within the desired range
        if guess <= 0 or guess > 100:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue  # Skip the rest of the loop and ask for a new guess

        print(guess)
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

        elif guess < secret_number:
            print("Too low! Try again.")

        else:
            print("Too high! Try again.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# End of the game
print("Thanks for playing!")
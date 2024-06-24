import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    # Prompt the user to input their guess
    user_guess = int(input("Enter your guess: "))

    # Increment the number of attempts
    attempts += 1

    # Compare the user's guess to the secret number
    if user_guess < secret_number:
        print("Guess higher! Try again.")
    elif user_guess > secret_number:
        print("Guess lower! Try again.")
    else:
        # The user guessed correctly!
        print(f" Congratulations! You guessed the number in {attempts} attempts.")
        break

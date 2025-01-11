import random

# Generate a random jackpot number between 1 and 100
jackpot = random.randint(1, 100)

# Take the first guess from the user
guess = int(input("Chal Guess Kar: "))
counter = 1

# Loop until the correct guess
while guess != jackpot:
    if guess < jackpot:
        print("Guess higher!")
    else:
        print("Guess lower!")
    
    # Take another guess
    guess = int(input("Chal Guess Kar: "))
    counter += 1

# User guessed the correct number
print("Sahi guess jawab!")
print(f"You took {counter} attempts.")

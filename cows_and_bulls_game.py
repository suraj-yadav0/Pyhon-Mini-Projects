import random

def generate_secret_number():
    """Generate a random 4-digit number with unique digits"""
    digits = list(range(10))
    random.shuffle(digits)
    # First digit shouldn't be 0
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    return ''.join(map(str, digits[:4]))

def get_bulls_and_cows(secret, guess):
    """Calculate the number of bulls and cows"""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows

def validate_guess(guess):
    """Validate if the guess is a valid 4-digit number with unique digits"""
    if not guess.isdigit() or len(guess) != 4:
        return False
    if len(set(guess)) != 4:
        return False
    return True

def play_bulls_and_cows():
    """Main game function"""
    print("Welcome to Bulls and Cows!")
    print("Try to guess the 4-digit number. Each digit is unique.")
    print("Bulls = correct digit in correct position")
    print("Cows = correct digit in wrong position")
    
    secret = generate_secret_number()
    attempts = 0
    
    while True:
        guess = input("\nEnter your guess (4 digits): ")
        
        if not validate_guess(guess):
            print("Invalid input! Please enter a 4-digit number with unique digits.")
            continue
        
        attempts += 1
        bulls, cows = get_bulls_and_cows(secret, guess)
        
        print(f"Bulls: {bulls}, Cows: {cows}")
        
        if bulls == 4:
            print(f"\nCongratulations! You won in {attempts} attempts!")
            print(f"The secret number was: {secret}")
            break

if __name__ == "__main__":
    while True:
        play_bulls_and_cows()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
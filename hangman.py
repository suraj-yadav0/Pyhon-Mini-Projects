import random
import string


def load_words(filename='sowpods.txt'):
    """Load words from file."""
    try:
        with open(filename, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        # Fallback word list if file not found
        return ['python', 'programming', 'computer', 'algorithm', 'developer']


def get_hangman_art(lives):
    """Return ASCII art for current game state."""
    stages = [
        # Final state: head, torso, both arms, both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # Head, torso, both arms, one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        # Head, torso, both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        # Head, torso, one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        # Head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        # Head
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        # Initial empty state
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    return stages[lives]


def play_hangman():
    words = load_words()
    word = random.choice(words).upper()
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters already guessed

    lives = 6  # Number of lives

    print("\nWelcome to HANGMAN!")
    print("Try to guess the word one letter at a time.")
    print("You have", lives, "lives.")

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        print("\n" + get_hangman_art(lives))

        # Print current word state
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        # Print used letters
        print('\nYou have used these letters:', ' '.join(sorted(used_letters)))

        # Get player input
        letter = input('Guess a letter: ').upper()

        # Input validation
        if letter not in alphabet:
            print('Please enter a valid letter.')
            continue
        elif letter in used_letters:
            print('You have already used that letter. Try again!')
            continue

        used_letters.add(letter)

        # Check if letter is in word
        if letter in word_letters:
            word_letters.remove(letter)
            print('Good guess!')
        else:
            lives = lives - 1
            print('Wrong guess. You have', lives, 'lives left.')

    # Game end
    print("\n" + get_hangman_art(lives))

    if lives == 0:
        print('Sorry, you died. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!')

    return input('\nWould you like to play again? (Y/N): ').upper().startswith('Y')


def main():
    while True:
        if not play_hangman():
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
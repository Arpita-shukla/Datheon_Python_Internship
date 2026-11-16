import random

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

WORD_LIST = [
    "PYTHON", "DATHEON", "DEVELOPER", "ALGORITHM", "AUTOMATION",
    "INTERFACE", "TERMINAL", "VARIABLE", "FUNCTION", "DATABASE"
]

def play_hangman():
    secret_word = random.choice(WORD_LIST)
    guessed_letters = set()
    mistakes = 0
    max_mistakes = 6

    print("=== WELCOME TO HANGMAN ===")

    while mistakes < max_mistakes:
        print(HANGMAN_STAGES[mistakes])
        masked_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print(f"Word: {masked_word}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining Attempts: {max_mistakes - mistakes}")

        if "_" not in masked_word:
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            return

        guess = input("\nGuess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. No penalty deducted.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    print(HANGMAN_STAGES[max_mistakes])
    print(f"\nGame Over! You ran out of attempts. The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()
  

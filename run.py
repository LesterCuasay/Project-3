"""
Imports
"""
import random
from words import word_list
from graphics import display_hangman


def get_word():
    """
    Gets a word from the words.py file and randomises it for the game.
    """
    word = random.choice(word_list)
    return word.upper()


def run_game(word):
    """
    The player will get 6 tries, and will be able to
    know which letters OR words they have already guessed
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word)
                           if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, You guessed the word! You win")
    else:
        print("No more tries! The  is " + word)


def main():
    """
    Calls to run the game.
    Gives user the option to restart the game once game completion.
    If not, then they can terminate the game.
    """
    word = get_word()
    run_game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        run_game(word)


if __name__ == "__main__":
    main()
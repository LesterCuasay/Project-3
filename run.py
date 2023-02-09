"""
Imports
"""
import random
import os
from words import word_list
from graphics import display_hangman


def player_id():
    """
    Prompts the user to input a player name
    """
    while True:
        global PLAYER_NAME
        PLAYER_NAME = input("What's your name?  \n").upper()
        if len(PLAYER_NAME) < 3:
            clear_screen()
            print("Name has to be more than 3 letters")
        elif PLAYER_NAME.isalpha():
            clear_screen()
            print(f"{PLAYER_NAME} Let's play Hangman!")
            return
        else:
            clear_screen()
            print(f"{PLAYER_NAME} is not valid")


def clear_screen():
    """
    Clear function to clean-up the terminal to reduce clutter.
    """
    os.system("cls" if os.name == "nt" else "clear")


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
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        print(f"The word has {len(word)} letters.")
        print("Letters guessed: " + ', ' .join(guessed_letters))
        guess = input("Please guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                clear_screen()
                print("You already guessed the letter", guess)
            elif guess not in word:
                clear_screen()
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                clear_screen()
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
                clear_screen()
                print("You already guessed the word", guess)
            elif guess != word:
                clear_screen()
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            clear_screen()
            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        clear_screen()
        print("Congrats " + PLAYER_NAME + ", You guessed the word! You win!")
    else:
        clear_screen()
        print("No more tries! " + PLAYER_NAME + ", the word is " + word)


def main():
    """
    Calls to run the game.
    Gives user the option to restart the game once game completion.
    If not, then they can terminate the game.
    """
    word = get_word()
    player_id()
    run_game(word)
    while True:
        restart_game = False
        while not restart_game:
            restart = input("Play Again? (Y/N) ")
            if restart.upper() == "Y":
                clear_screen()
                print("Let's go again!")
                restart_game = True
            elif restart.upper() == "N":
                print("Thanks for playing, " + PLAYER_NAME + "!")
                quit()
            else:
                clear_screen()
                print(f"{restart} not valid")
                print("Type 'Y' or 'N'")
        word = get_word()
        run_game(word)


if __name__ == "__main__":
    main()
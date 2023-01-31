import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def run_game(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6


def display_hangman(tries):
    stages = [
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        """
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        """
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     
            -
        """
        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        """
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        """
        """
            --------
            |      |
            |      O
            |      
            |      
            |     
            -
        """
    ]
    return stages[tries]
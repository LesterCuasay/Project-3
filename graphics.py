def display_hangman(tries):
    """
    Displays the lives remaining depending on incorrect guesses.
    """
    stages = [
                """
                   You're Dead !
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   1 more guess left !
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                """
                   2 more guesses left !
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                """
                   3 more guesses left !
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                """
                   4 more guesses left !
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                """
                   5 more guesses left !
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
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
    return stages[tries]
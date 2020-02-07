import Hangman
import GuessTheNumber


def choose_game():
    print("Choose the game you want to play: ")
    choice = int(input("(1) Hangman (2) Guess the Number"))

    if(choice == 1):
        Hangman.play()
    elif(choice == 2):
        GuessTheNumber.play()


if(__name__ == "__main__"):
    choose_game()
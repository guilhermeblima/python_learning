import random


def play():
    print("*************************************")
    print("Welcome to Guess The Number!")
    print("*************************************")

    secret_number = round(random.randrange(1, 101))
    total_attempts = 0
    points = 1000

    print("Choose the level of difficulty: ")
    level = int(input("(1) Easy - (2) Medium - (3) Hard"))

    if (level == 1):
        total_attempts = 20
    elif (level == 2):
        total_attempts = 10
    else:
        total_attempts = 5

    for rodada in range(1, total_attempts + 1):
        print("Attempts {} of {}".format(rodada, total_attempts))
        guess_str = input("Please enter a number between 1 and 100: ")
        print("You entered ", guess_str)
        guess = int(guess_str)

        if (guess < 1 or guess > 100):
            print("Please enter a number between 1 and 100!")
            continue

        got_it = guess == secret_number
        greater = guess > secret_number
        less = guess < secret_number

        if (got_it):
            print("You got it and scored {} points".format(points))
            break
        else:
            if (greater):
                print("Wrong! Your guess was greater than the secret number.")
            elif (less):
                print("Wrong! Your guess was less than the secret number.")
            lost_points = abs(secret_number - guess)
            points = points - lost_points
            if (rodada == total_attempts):
                print("The secret number was {} and you scored {} points".format(secret_number, points))
    print("Game Over")


if (__name__ == "__main__"):
    play()

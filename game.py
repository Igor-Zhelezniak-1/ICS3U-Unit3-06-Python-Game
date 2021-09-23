#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is game

import random

secret_number = random.randint(0, 9)  # a number between 0 and 9


def main():
    # this function uses a try statement

    # input
    integer = input("Enter the number between 0-9: ")
    print("")

    # process & output
    try:
        number = int(integer)
        if number == secret_number:
            print("You guessed correct!")
        elif number < 0:
            print("You need enter number 0-9")
        elif number > 9:
            print("You need enter number 0-9")
        else:
            print("You guessed wrong! The number was {0}".format(secret_number))

    except Exception:
        print("This was not a number")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()

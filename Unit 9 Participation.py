"""
Program Name: Die simulator
Author: zachary  ostheimer
Purpose: This program creates a Die class and simulates rolling dice with different numbers of sides.
Starter Code: None
Date: 06/28/2026
"""

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = random.randint(1, self.sides)
        print(number)


def main():
    # make a 6 sided die and roll it 10 times
    print("Rolling a 6-sided die 10 times:")
    die6 = Die()
    for i in range(10):
        die6.roll_die()

    print()

    # make a 10 sided die and roll it 10 times
    print("Rolling a 10-sided die 10 times:")
    die10 = Die(10)
    for i in range(10):
        die10.roll_die()

    print()

    # make a 20 sided die and roll it 10 times
    print("Rolling a 20-sided die 10 times:")
    die20 = Die(20)
    for i in range(10):
        die20.roll_die()


main()
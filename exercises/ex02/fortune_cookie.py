"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730381998"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...


print("Your fortune cookie says... ")
number: int = randint(1,4)
if number == 1:
    print("You will have great success soon! ")
else:
    if number == 2:
        print("You will receive an unexpected gift in the coming days! ")
    else:
        if number == 3:
            print("You will find what you are looking for! ")
        else:
            if number == 4:
                print("Your life will be full of happiness and good memories! ")
print("Now, go spread positive vibes!")
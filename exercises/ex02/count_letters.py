"""Counting letters in a string."""

__author__ = "730381998"


# Begin your solution here...
i: int = 0
letter: str = str(input("What letter do you want to search for?: "))
word: str = str(input("Enter a word: "))
count: int = 0 
while i < len(word):
    if (word[i]) == letter:
        count = count + 1
    else:
        count == 0
    i = i + 1

print("Count: " + str(count))

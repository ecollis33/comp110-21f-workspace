"""Repeating a beat in a loop."""

__author__ = "730381998"


# Begin your solution here...
i : int = 0
counter : int = 0
beat: str = input("What beat do you want to repeat? ")
maximum : int = int(input("How many times do you want to repeat it? "))
counter = 0
while counter < maximum:  
    print(beat, end = '')
    counter = counter + 1

if maximum <= 0:
    print("No beat...")

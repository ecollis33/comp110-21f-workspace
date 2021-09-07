"""This is my program for numeric operators in Python."""
__author__ = "730381998"

A: int = int(input("Left-hand side: "))
B: int = int(input("Right-hand side: "))

print(str(A) + " ** " + str(B) + " is " + str(A ** B))
print(str(A) + " / " + str(B) + " is " + str(A / B))
print(str(A) + " // " + str(B) + " is " + str(A // B))
print(str(A) + " % " + str(B) + " is " + str(A % B))
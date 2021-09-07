"""This is my program for relational operators in Python."""
__author__ = "730381998" 

A: int = int(input("Left-hand side: "))
B: int = int(input("Right-hand side: "))

less_than = bool(A < B)
greater_or_equal = bool(A >= B)
equal = bool(A == B)
not_equal = bool(A != B)
print(str(A) + " < " + str(B) + " is " + str(less_than))
print(str(A) + " >= " + str(B) + " is " + str(greater_or_equal))
print(str(A) + " == " + str(B) + " is " + str(equal))
print(str(A) + " != " + str(B) + " is " + str(not_equal))
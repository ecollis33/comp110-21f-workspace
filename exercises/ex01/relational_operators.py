"""This is my program for relational operators in Python."""
__author__= "730381998" 

A: int = int(input("Left-hand side: "))
B: int = int(input("Right-hand side: "))

lessthan = bool (A<B)
greaterorequal= bool (A>=B)
equal= bool (A==B)
notequal= bool(A!=B)
print(str(A) + " < " + str(B) + " is " + str(lessthan))
print(str(A) + " >= " + str (B) + " is " + str(greaterorequal))
print(str(A) + " == " + str(B) + " is " + str(equal))
print(str(A) + " != " + str(B) + " is " + str(notequal))
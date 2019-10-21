# Gretchen Ferland
# trivia game

def printMessage():
    print("Welcome to the school game")
    print("Lets learn some new things!")

def main():
    print("Hello Student")
    printMessage()

main()

print("lets look at some simple math equations first ")

print("a will equal 2")
print("b will equal 5")
a= int(2)
b= int(5)
print("a-b")
print(a-b)
print("b*b")
print(b*b)
print("b/a")
print(b/a)

print("now lets look at a more complicated problem")
import math

def getQuadratic(a,b) :
    square = a**2 + b**2
    squareRoot = math.sqrt(square)
    return squareRoot

def main():
    print("The sqaure of the sum of the squares of 3 and 4 is:", getQuadratic(3,4))

main()

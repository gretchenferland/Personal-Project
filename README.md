
print("What would a - b equal?: ")
x = int(input())
if x == a - b:
    print("Correct!")
else:
    while a - b != x
        x = int(input))
        if x == a - b:
            print("Correct")


        print("Incorrect, try again")

        print("What would b * b equal?: ")
        x = int(input())
        if x == a * b:
            print("Correct!")
        else:
            print("Incorrect, try again")

        print("What would b / a equal?: ")
        x = int(input())
        if x == b / a:
            print("Correct!")
        else:
            print("Incorrect,try again")

        print("now lets look at a more complicated problem")
        import math


def getQuadratic(a, b):
    square = a ** 2 + b ** 2
    squareRoot = math.sqrt(square)
    return squareRoot


def main():
    print(
    "The sqaure of the sum of the squares of 3 and 4 is:", getQuadratic(3, 4))


main()

# Enter a number that is not written but in actual numerical form
print("Now give me all the numbers between 2 and 20 that are divisible by 2: ")
for x in range(2, 20, 2):
    print(x)

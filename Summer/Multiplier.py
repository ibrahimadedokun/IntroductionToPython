import random as _random
import operator as _operator

print("Multiplying application")

scores = 0

while scores > -3 and scores < 3:
    firstNumber = _random.randrange(2, 12)
    secondNumber = _random.randrange(2, 12)

    print(str(firstNumber) + " x " + str(secondNumber))

    while True:
            try:
                response = int(input("The answer is: "))
            except ValueError:
                print("Enter a valid answer...")
                continue
            else:
                break

    if response == _operator.mul(firstNumber, secondNumber):
        scores = scores + 1
        print("Correct!")
        print("Total score now: " + str(scores))
        if scores == 3:
            print("You are a genius")
    else:
        scores = scores - 1
        print("Wrong!")
        print("Total score now: " + str(scores))
        if scores == -3:
            print("Better luck next time")
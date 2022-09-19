import random as _random

print("Subtracting application")

scores = 0

while scores > -3 and scores < 3:
    firstNumber = _random.randrange(1, 100)
    secondNumber = _random.randrange(1, 100)

    if firstNumber > secondNumber:
        print(str(firstNumber) + " - " + str(secondNumber))

        response = input()

        if int(response) == firstNumber - secondNumber:
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
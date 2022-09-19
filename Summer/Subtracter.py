import random as _random
import operator as _operator

print("===SUBTRACTING APPLICATION===")

scores = 0
maxScores = 3
minScores = -3

while scores > minScores and scores < maxScores:
    firstNumber = _random.randrange(1, 100)
    secondNumber = _random.randrange(1, 100)

    if firstNumber > secondNumber:
        print("\n" + str(firstNumber) + " - " + str(secondNumber))

        while True:
            try:
                response = int(input("You've entered: "))
            except ValueError:
                print("Enter a valid answer...")
                continue
            else:
                break        

        answer = _operator.sub(firstNumber, secondNumber)

        if response == answer:
            scores += 1
            print("Correct!")
            print("Total score now: " + str(scores))
            if scores == maxScores:
                print("You are a genius")
        else:
            scores -= 1
            print("Wrong! The correct answer is {}".format(answer))
            print("Total score now: " + str(scores))
            if scores == minScores:
                print("Better luck next time")
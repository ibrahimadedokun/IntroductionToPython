import random as _random
import operator as _operator

print("===MULTIPLYING APPLICATION===")

scores = 0

while scores > -3 and scores < 3:
    firstNumber = _random.randrange(2, 12)
    secondNumber = _random.randrange(2, 12)

    print("\n" + str(firstNumber) + " x " + str(secondNumber))

    while True:
            try:
                response = int(input("You've entered: "))
            except ValueError:
                print("Enter a valid answer...")
                continue
            else:
                break
    
    answer = _operator.mul(firstNumber, secondNumber)

    if response == answer:
        scores = scores + 1
        print("Correct!")
        print("Total score now: " + str(scores))
        if scores == 3:
            print("You are a genius")
    else:
        scores = scores - 1
        print("Wrong! The correct answer is {}".format(answer))
        print("Total score now: " + str(scores))
        if scores == -3:
            print("Better luck next time")
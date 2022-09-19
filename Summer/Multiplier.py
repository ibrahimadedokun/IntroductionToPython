import random as _random
import operator as _operator

class CustomMultiplier:
    def __init__(this, maximumScore = 3, minimumScore = -3, rangeUpperLimit = 12, rangeLowerLimit = 2):
        this.maximumScore = maximumScore
        this.minimumScore = minimumScore
        this.rangeUpperLimit = rangeUpperLimit
        this.rangeLowerLimit = rangeLowerLimit

    def invoke(this):
        print("===MULTIPLYING APPLICATION===")

        score = 0

        while score > this.minimumScore and score < this.maximumScore:
            firstNumber = _random.randrange(this.rangeLowerLimit, this.rangeUpperLimit)
            secondNumber = _random.randrange(this.rangeLowerLimit, this.rangeUpperLimit)

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
                score += 1
                print("Correct!")
                print("Total score now: " + str(score))
                if score == this.maximumScore:
                    print("\nYou are a genius!\n")
            else:
                score -= 1
                print("Wrong! The correct answer is {}".format(answer))
                print("Total score now: " + str(score))
                if score == this.minimumScore:
                    print("\nBetter luck next time.\n")
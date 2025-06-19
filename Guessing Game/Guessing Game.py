import random

def guessing_number():
    print("Thinking of a Number between 1 and 100....")
    number = random.randint(0, 100)

    attempts = 0

    while True:
        try:
            user = int(input("Enter you Guess :"))
            attempts += 1

            if user < number:
                print("Too Low! Try Again.")

            elif user > number:
                print("Too High! Try Again.")

            else:
                print("Great Gob! You Guessed the Number in", attempts, "attempts.")
                break

        except ValueError:
            print("Invalid Input! Try Again.")
            guessing_number()

guessing_number()
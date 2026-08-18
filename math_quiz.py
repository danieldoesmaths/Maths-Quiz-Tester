from random import randint

score = 0

def generate_question():
    number_1 = randint(1, 12)
    number_2 = randint(1, 12)
    return number_1, number_2

def multiplication(number, number_1, number_2):
    value = number_1 * number_2
    answer = int(input(
        f"Question {number}: What is {number_1} x {number_2}? : "
    ))
    if answer == value:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

def addition(number, number_1, number_2):

    value = number_1 + number_2
    answer = int(input(
        f"Question {number}: What is {number_1} + {number_2}? : "
    ))

    if answer == value:
        print("Correct!")
        return True

    else:
        print("Incorrect!")
        return False

while True:

    print("Welcome to the Maths Timetable Quiz!")
    response = input(
        "\nWould you like to start? (Type Yes or No): "
    )

    if response == "Yes":
        print("Alright, let's get started!")
        operation = int(input(
            "Which operation would you like to be tested on?"
            "\n\t1. Addition"
            "\n\t2. Multiplication"
            "\n"
        ))

        if operation == 1:
            for number in range(1, 11):
                number_1, number_2 = generate_question()
                if addition(number, number_1, number_2):
                    score += 1
            print(f"\nYou scored {score}/10")
            break

        elif operation == 2:
            for number in range(1, 11):
                number_1, number_2 = generate_question()
                if multiplication(number, number_1, number_2):
                    score += 1
            print(f"\nYou scored {score}/10")
            break

        else:
            print("Incorrect response. Shutting down quiz...")
            break

    elif response == "No":
        print("No worries, shutting down quiz...")
        break

    else:

        print(
            "That is not a response that I am looking for."
            "\n\nRestarting..."
        )
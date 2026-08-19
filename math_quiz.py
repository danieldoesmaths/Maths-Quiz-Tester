from random import randint

score = 0

def smallest_number():
    smallest = int(input("What is the smallest number you want to be tested on? "))
    return smallest

def largest_number():
    largest = int(input("What is the largest number you want to be tested on? "))
    return largest

def check_range(smallest, largest):
    if largest <= smallest:
        return False
    return True

def generate_question(smallest, largest):
    number_1 = randint(smallest, largest)
    number_2 = randint(smallest, largest)
    return number_1, number_2

def generate_division_question(smallest, largest):
    smaller = randint(smallest, largest)
    # Find possible divisors
    possible_answers = []
    for answer in range(smallest, largest + 1):
        larger = smaller * answer
        if larger <= largest:
            possible_answers.append(answer)

    # Pick an answer that keeps the larger number within the range
    answer = randint(0,len(possible_answers) - 1)
    answer = possible_answers[answer]
    larger = smaller * answer
    return larger, smaller

def number_of_questions():
    questions = int(input("How many questions would you like to be tested on? "))
    return questions

def multiplication(number, number_1, number_2):
    value = number_1 * number_2
    answer = int(input(f"Question {number}: What is {number_1} x {number_2}? : "))
    if answer == value:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

def addition(number, number_1, number_2):
    value = number_1 + number_2
    answer = int(input(f"Question {number}: What is {number_1} + {number_2}? : "))
    if answer == value:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

def subtraction(number, number_1, number_2):
    value = number_1 - number_2
    answer = int(input(f"Question {number}: What is {number_1} - {number_2}? : "))

    if answer == value:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

def division(number, number_1, number_2):
    value = number_1 // number_2
    answer = int(input(f"Question {number}: What is {number_1} ÷ {number_2}? : "))
    if answer == value:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

while True:
    print("\nWelcome to the Maths Timetable Quiz!")
    response = input("\nWould you like to start? (Type Yes or No): ")
    if response == "Yes":
        print("\nAlright, let's get started!")
        operation = int(input(
            "Which operation would you like to be tested on?"
            "\n\t1. Addition"
            "\n\t2. Multiplication"
            "\n\t3. Subtraction"
            "\n\t4. Division"
            "\n"))

        if operation == 1:

            while True:
                smallest = smallest_number()
                largest = largest_number()
                if check_range(smallest, largest):
                    break
                print(
                    "Error: The largest number must be greater "
                    "than the smallest number."
                )

            questions = number_of_questions()
            for number in range(1, questions + 1):
                number_1, number_2 = generate_question(smallest,largest)
                if addition(number, number_1, number_2):
                    score += 1
            print(f"\nYou scored {score}/{questions}")
            break

        elif operation == 2:

            while True:
                smallest = smallest_number()
                largest = largest_number()

                if check_range(smallest, largest):
                    break

                print(
                    "Error: The largest number must be greater "
                    "than the smallest number."
                )

            questions = number_of_questions()

            for number in range(1, questions + 1):

                number_1, number_2 = generate_question(smallest,largest)
                if multiplication(number, number_1, number_2):
                    score += 1
            print(f"\nYou scored {score}/{questions}")
            break

        elif operation == 3:
            while True:
                smallest = smallest_number()
                largest = largest_number()

                if check_range(smallest, largest):
                    break
                print(
                    "Error: The largest number must be greater "
                    "than the smallest number."
                )
            questions = number_of_questions()
            for number in range(1, questions + 1):
                number_1, number_2 = generate_question(smallest,largest)
                if subtraction(number, number_1, number_2):
                    score += 1
            print(f"\nYou scored {score}/{questions}")
            break

        elif operation == 4:

            while True:
                smallest = smallest_number()
                largest = largest_number()
                if check_range(smallest, largest):
                    break
                print(
                    "Error: The largest number must be greater "
                    "than the smallest number.")

            questions = number_of_questions()

            for number in range(1, questions + 1):
                number_1, number_2 = generate_division_question(smallest,largest)
                if division(number, number_1, number_2):
                    score += 1

            print(f"\nYou scored {score}/{questions}")
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
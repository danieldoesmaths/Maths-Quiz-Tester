from random import randint

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
    possible_answers = []
    for answer in range(smallest, largest + 1):
        larger = smaller * answer
        if larger <= largest:
            possible_answers.append(answer)
    answer = randint(0,len(possible_answers) - 1)
    answer = possible_answers[answer]
    larger = smaller * answer
    return larger, smaller

def number_of_questions():
    questions = int(input("How many questions would you like to be tested on? "))
    return questions

def multiplication(number, number_1, number_2):
    value = number_1 * number_2
    answer = int(input(
            f"Question {number}: "
            f"What is {number_1} x {number_2}? : "))

    if answer == value:
        print("Correct!")
        return True

    else:
        print("Incorrect!")
        return False

def addition(number, number_1, number_2):

    value = number_1 + number_2

    answer = int(input(
            f"Question {number}: "
            f"What is {number_1} + {number_2}? : "))

    if answer == value:
        print("Correct!")
        return True

    else:
        print("Incorrect!")
        return False

def subtraction(number, number_1, number_2):
    value = number_1 - number_2
    answer = int(input(
            f"Question {number}: "
            f"What is {number_1} - {number_2}? : "))

    if answer == value:
        print("Correct!")
        return True

    else:
        print("Incorrect!")
        return False

def division(number, number_1, number_2):
    value = number_1 // number_2
    answer = int(input(
            f"Question {number}: "
            f"What is {number_1} ÷ {number_2}? : "))

    if answer == value:
        print("Correct!")
        return True

    else:
        print("Incorrect!")
        return False

def mixed_question(number,smallest,largest):
    operation = randint(1, 4)
    if operation == 1:
        number_1, number_2 = generate_question(smallest,largest)
        return addition(number,number_1,number_2)

    elif operation == 2:
        number_1, number_2 = generate_question(smallest,largest)
        return multiplication(number,number_1,number_2)

    elif operation == 3:
        number_1, number_2 = generate_question(smallest,largest)
        return subtraction(number,number_1,number_2)

    else:
        number_1, number_2 = generate_division_question(smallest,largest)
        return division(number,number_1,number_2)

while True:

    print("\nWelcome to the Maths Timetable Quiz!")

    response = input(
        "\nWould you like to start? "
        "(Type Yes or No): ")

    if response == "Yes":
        print("\nAlright, let's get started!")
        operation = int(input(
                "Which operation would you like "
                "to be tested on?"
                "\n\t1. Addition"
                "\n\t2. Multiplication"
                "\n\t3. Subtraction"
                "\n\t4. Division"
                "\n\t5. Mixed"
                "\n"))

        if operation in (1, 2, 3, 4, 5):
            while True:
                smallest = smallest_number()
                largest = largest_number()

                if check_range(smallest,largest):
                    break

                print("Error: The largest number must be "
                    "greater than the smallest number.")

            questions = number_of_questions()
            score = 0

            for number in range(1,questions + 1):
                if operation == 1:
                    number_1, number_2 = generate_question(smallest,largest)
                    if addition(number,number_1,number_2):
                        score += 1

                elif operation == 2:
                    number_1, number_2 = generate_question(smallest,largest)
                    if multiplication(number,number_1,number_2):
                        score += 1

                elif operation == 3:
                    number_1, number_2 = generate_question(smallest,largest)
                    if subtraction(number,number_1,number_2):
                        score += 1

                elif operation == 4:
                    number_1, number_2 = generate_division_question(smallest,largest)
                    if division(number,number_1,number_2):
                        score += 1

                elif operation == 5:
                    if mixed_question(number,smallest,largest):
                        score += 1

            print(f"\nYou scored {score}/{questions}")
            break

        else:
            print("Incorrect response. "
                "Shutting down quiz...")
            break

    elif response == "No":
        print("No worries, shutting down quiz...")
        break

    else:

        print("That is not a response that I am looking for.\n\nRestarting...")
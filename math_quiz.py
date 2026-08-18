from random import randint

score = 0

while True:

    print("Welcome to the Maths Timetable quiz!")

    response = input("\nWould you like to start? (Type Yes or No): ")
    if response == "Yes":
        print("Alright, let's get started!")
        for number in range(1, 11):
            number_1 = randint(1, 12)
            number_2 = randint(1, 12)
            value = number_1 * number_2
            answer = int(input(f"Question {number}: What is {number_1} x {number_2}? : "))

            if answer == value:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

        print(f"\nYou scored {score}/10")
        break

    elif response == "No":
        print("No worries, shutting down quiz...")
        break

    else:

        print("That is not a response that I am looking for.\n\nRestarting...")
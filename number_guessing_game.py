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

print("Welcome to the number guessing game!")
while True:
    small = smallest_number()
    large = largest_number()
    if check_range(small, large):
        break

    print("Larger number needs to be greater than smaller number.")

random_generated_number = randint(small, large)

print(f"\nAlright! I have now chosen a number between {small} and {large}. Can you guess it?")

number_of_guesses = 0

while True:
    guessed_number = int(input("Your chosen number: "))
    number_of_guesses += 1
    print(f"\nGuess No. {number_of_guesses}:{guessed_number}")

    if guessed_number < random_generated_number:
        print("The number is higher!")
    elif guessed_number > random_generated_number:
        print("The number is lower!")
    else:
        print("Correct!")
        break
print(
    f"\nFinal Stats"
    f"\n\tThe Number: {random_generated_number}"
    f"\n\tTotal Guesses: {number_of_guesses}"
    )

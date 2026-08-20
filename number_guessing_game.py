from random import randint

print("Welcome to the number guessing game ")

smallest_number = int(input("What is the smallest number that you want the range to be ?  :"))
largest_number = int(input("What is the largest number that you want the range to be ?  :"))

random_generated_number = randint(smallest_number,largest_number)

print(f"\nAlright!,I have now chosen a number between {smallest_number} to {largest_number} can you guess it?")

number_of_guesses = 0

while True:
    guessed_number = int(input("Your chosen number  :"))
    number_of_guesses += 1
    if guessed_number < random_generated_number:
        print(f"\nGuess No.{number_of_guesses} : {guessed_number}")
        print("The number is higher!")
        
    elif guessed_number > random_generated_number:
        print(f"\nGuess No.{number_of_guesses} : {guessed_number}")
        print("The number is lower!" )
        
    else:
        break
print(f"\nFinal Stats\n\tThe Number:{random_generated_number}\n\tTotal Guesses:{number_of_guesses}")

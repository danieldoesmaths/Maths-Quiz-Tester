from random import randint
random_generated_number = randint(0,100)
print("Welcome to the number guessing game ")
print("\nI have chosen a number between 0 to 100 can you guess it?")
while True:
    guessed_number = int(input("Your chosen number  :"))
    if guessed_number < random_generated_number:
        print("The number is higher!")
    elif guessed_number > random_generated_number:
        print("The number is lower!" )
    else:
        break
print(f" You have guessed correctly ! , the number that I have is {random_generated_number}")
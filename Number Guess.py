import random

number_to_guess = random.randint(1, 100)

while True:
 try:
   guess = int(input("Guess a number between 1 and 100: "))

   if guess < number_to_guess:
    print("Too low!")
   elif guess > number_to_guess:
    print("Too high!")
   else:
    print("Comnngratulation! You guesses the number.")
    break
 except ValueError:
  print('Please enter a valid number')

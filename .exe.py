import random
secretnumber = random.choice(range(101))
chances = 0
while chances < 7:
  try:
    n = int(input("Guess a number between 1 and 100 "))
  except:
      print("Stupid! Enter a fricking integer!")
      continue
  if n == secretnumber:
    print("Good Job! You guessed it.")
    break
  if n > 100:
    print("Stupid! It says between 1 and 100")
    continue
  if n < 1:
    print("Stupid! It says between 1 and 100")
    continue
  if n > secretnumber:
    print("Too High")
    chances = chances+1
  else:
    print("Too Low")
    chances = chances+1
if chances >= 7:
    print("You couldn't guess it. You're a failure!")
    print(f"The secret number was {secretnumber}.")
import random

print ("You have 5 tries to guess the number")
print(" You have to choose from these" + target)

trys = 1
target = ["blue", "red", "green", "pink", "yellow", "gray"]
rand = random.choice(target)
while trys != 5:
  num = input("Guess >> ")
  trys +=1
  if guess == rand:
    print("You guessed it")
    break

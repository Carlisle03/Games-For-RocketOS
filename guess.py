import random

class Game:
  def __init__(self):
    self.tries = 0
    self.target = random.randint(1, 100)
  def execute(self):
    print("Guess a number from 1 to 100")
    while True:
      guess = input("Guess >> ")
      if guess == self.target:
        break
      
main=Game()
main.execute()

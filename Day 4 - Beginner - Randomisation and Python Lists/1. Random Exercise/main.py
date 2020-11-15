import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

randomSide = random.randint(0, 1)
if randomSide == 1:
  print("Heads")
else:
  print("Tails")
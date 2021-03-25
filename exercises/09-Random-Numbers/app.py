import random
import os

def get_randomInt():
  # CHANGE ONLY THIS LINE BELOW
	random_number = random.randint(1, 10)
	return random_number


os.system("clear")
print(get_randomInt())

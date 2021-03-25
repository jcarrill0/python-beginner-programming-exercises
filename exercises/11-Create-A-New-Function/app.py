import random
import os

# your code here

def generate_random():
    r1 = random.randint(0, 9)
    print("Random number between 0 and 10 is % s" % (r1))

os.system("clear")
generate_random()
import random
import os

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
    position = spin_chamber()
    if position == bullet_position:
        return "You are dead!"
    else : 
        return "Keep playing!"

os.system("clear")
print(fire_gun())
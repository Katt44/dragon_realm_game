import random 
import time

# having the user pick between to caves, that randomly are friendly or dangerous
# printing text out slowly for suspense in  checking the cave
# asking user if they want to play again

def display_intro():
	print ('''Standing at the mouth of a cave you take one long inhale 
and you exhale as you pass through the threshold.
The cave up ahead  forks but both paths are damp, seeming to breathing, and onimnious. ''')

def choose_a_cave():
	cave = ""
	print ("Do you go left or right?(1,2)")

	
#	while cave != '1' and cave  != '2': # what does this mean
#		print ("Do you go left or right?(1,2)")
#		cave = input()

	return cave

def check_cave():
	print (" The once narrow cave expands sharply..")
	time.sleep(2)
	print ("In the pitch black, you feel a rush of hot foul smelling air hit you.. ")
	time.sleep(2)


	friendly_cave = random.randint(1,2)

	if chosen_cave == str(friendly_cave):
		print(" dragon scene1 ")
	else:
		print ("dragon scene2")

#def play_again():



display_intro()
choose_a_cave()
check_cave()
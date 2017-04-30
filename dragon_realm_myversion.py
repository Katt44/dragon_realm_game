import random 
import time

def display_intro():
	print ('''Standing at the mouth of a cave you take one long inhale 
and you exhale as you pass through the threshold.
The cave up ahead  forks but both paths are damp, seeming to breathing, and onimnious. ''')

def choose_a_cave():
	cave = raw_input("What cave will you enter? left or right?")
	cave = cave.lower()
	print "you chose to go " + cave + " good luck."
	return cave 
	

def check_cave(chosen_cave):
	print (" The once narrow cave expands sharply..")
	time.sleep(2)
	print ("In the pitch black, you feel a rush of hot foul smelling air hit you.. ")
	time.sleep(2)

	friendly_cave = random.choice(['right','left'])
	if chosen_cave == friendly_cave:
		print  "The dragon finds you and falls in love with you"
	else:
		print "The starving dragon sees you and drools. It lunges toward you and eats you"


#call functions
def play_dragon_realm():
	display_intro()
	cave = choose_a_cave()
	check_cave(cave)

play_dragon_realm()
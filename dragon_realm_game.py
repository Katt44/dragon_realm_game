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
	while cave != '1' and cave  != '2':
		print ("Do you go left or right?(1,2)")
		cave = input()

	return cave

#def check_cave():

#def play_again():



display_intro()
choose_a_cave()
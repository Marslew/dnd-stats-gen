#This is a DnD Stats Generator. Some lighthearted Python Fun

########################
#Script Name: Dnd Stats Generator
#Date Started: 4/1/2020
#Date Finished: 4/9/2020
#Author: 
########################
# Version History
# 1.0 Script considered finished with functional loops for content

# Possible Improvements in Later versions
# Break choices into functions
# Work on User Interface (state when dice rolls are made, mention stat results, etc)
# Expand for "Class Suggestions" - Ask user for class, and suggest stats alignment. 
# Expand Class Suggestions to incorporate racial stat bonuses. 

from random import randint

def stat_gen_method():
	print("Welcome to the DnD Stats Generator!")
	print("Here are the methods of generating stats in DnD.")
	print("1. Manual Dice Roll")
	print("2. Point Buy")
	print("3. Standard Template")
	method_choice = input("Please select the number to generate Stats.\n")
	return method_choice
	
def dm_comment(choice):

	if choice == "evil":
		print("Ok, we'll have some tough rolls up ahead. Hold on!")
	elif choice == "fair":
		print("Remember that whatever happens...fair is fair.")
	elif choice == "lenient": 
		print("Ok, we'll have some forgiveness baked in.")
		
def stat_roll(type):

	stat_list = []
	
	for j in range(0,6):
			
		four_dice = []
		
		for i in range (1,5):
			if type == "evil":
			
				dice_num = randint(1, 6)
			elif type == "fair":
				dice_num = randint(2, 6)
			elif type == "lenient":
				dice_num = randint(3, 6)
			
			four_dice.append(dice_num)
					
		four_dice.sort()
		four_dice.pop(0)
		value = sum(four_dice)
		stat_list.append(value)
		
	return stat_list
	
def method_output(gen_choice):

	if gen_choice == '1':

		char_stats = ''
		print("You've selected the Manual method for stats.")
		dm_style = input("Is the DM evil, fair, or lenient? Please describe.")
		dm_comment(dm_style)
		char_stats = stat_roll(dm_style)	
		return char_stats
	
	elif gen_choice == '2':
		print("You've selected the Point Buy method for stats.")
		print("You have 27 points to spend on abilities. See chart below.")
		print("Ability Score Point Cost")
		print("Score			Cost")
		print("  8			  0 ")
		print("  9			  1 ")
		print("  10			  2 ")
		print("  11			  3 ")
		print("  12			  4 ")
		print("  13			  5 ")
		print("  14			  7 ")
		print("  15			  9 ")
		print("\n\nWe hope you choose wisely!")
		
	elif gen_choice == '3':
		print("You've selected the Standard Template method for stats.")
		print("Use the numbers 8, 10, 12, 13, 14,15 how you see fit.")
		char_stats = [8, 10, 12, 13, 14,15]
		return char_stats

	else:
		print("Oops! You entered an incorrect choice.")
		stat_choice = input("Please select the number to generate Stats.")
	

stat_choice = ''

stat_choice = stat_gen_method()
stats = method_output(stat_choice)
print(stats)
print("Well...I hope you liked your results. Those are yours for keeps!")


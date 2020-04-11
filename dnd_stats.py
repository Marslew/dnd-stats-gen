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
print("Welcome to the DnD Stats Generator!")

print("Here are the methods of generating stats in DnD.")

print("1. Manual Dice Roll")
print("2. Point Buy")
print("3. Standard Template")

stat_choice = input("Please select the number to generate Stats.\n")
stat_list = []

#print("Ok, we'll have some forgiveness baked in.")
#print("Ok, we'll have some tough rolls up ahead. Hold on!")
#print("Well...I hope you liked your results. Those are yours for keeps!")
#print("Remember that whatever happens...fair is fair.")

while stat_choice == '1' or '2' or '3':
	if stat_choice == '1':
		print("You've selected the Manual method for stats.")
		
		dm_style = input("Is the DM evil, fair, or lenient? Please describe.")
		
		#if dm_style != 'evil' or 'fair' or 'lenient':
		#	print("You need to enter a description. Please state the type of DM")
		#	print(dm_style)
		#	dm_style = input("Is the DM evil, fair, or lenient? Please describe.")

		for j in range(0,6):
			
			four_dice = []
			value = 0
			
			for i in range (1,5):
				if dm_style == "evil":
					dice_num = randint(1, 6)
				elif dm_style == "fair":
					dice_num = randint(2, 6)
				elif dm_style == "lenient":
					dice_num = randint(3, 6)
				four_dice.append(dice_num)
					
			four_dice.sort()
			four_dice.pop(0)
			value = sum(four_dice)
			stat_list.append(value)
				
			
		print(stat_list)	
		
	elif stat_choice == '2':
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
		
	elif stat_choice == '3':
		print("You've selected the Standard Template method for stats.")
		print("Use the numbers 8, 10, 12, 13, 14,15 how you see fit.")


	else:
		print("Oops! You entered an incorrect choice.")
		stat_choice = input(print("Please select the number to generate Stats."))


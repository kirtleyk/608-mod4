""" File 2 - playing-craps.py (Sections 4.4, 4.5)
In this file, we will use random functions to simulate chance events (rolling a pair of six-sided dice). 
Following the example provided in Section 4.4 "Rolling a Six-Sided Die 6,000,000 Times", create a simulation that rolls two dice 6 million times. Hint: On line 15, make face = random.randrange(1,7) + random.randrange(1,7) and expand the the if block to up to 12 (6+6, the maximum value of two dice).  For one possible solution, see Module 3: Project Craps (One possible solution) 
What fraction of the time did you roll "craps"? (add the frequencies for 2, 3, or 12)
What fraction of the time did you "win"? (add the frequencies for 7 or 11)
Confirm you get approximately the same as the example run shown below.
"""

from random import randrange

# create list that will hold totals of the die rolls in each of 12 positions
face_totals = [0,0,0,0,0,0,0,0,0,0,0,0]

def roll():
    # calculate random die roll total
    die_roll_total = randrange(1,7) + randrange(1,7)
    # increment the count value for the face value rolled based on the list position
    face_totals[die_roll_total-1] += 1
    return die_roll_total


roll_total = 6000000   # Set number of dice rolls
for x in range(1, roll_total+1): roll()   #roll the dice
 
print(f'\nSimulating {roll_total} die rolls!', '\n')

# display the die roll totals calculated and stored in each position of the list  
print(f'Face {"Frequency":>13}')  # heading
for index in range(len(face_totals)): 
    # the position in the list (+1, zero-based index) represents the face of the die rolled
    # the total was stored in the index+1 position of the list for corresponding die roll face value
    print(f'{index+1:>4} {face_totals[index]:>13}')  
    
# calucate percentage of times rolled for craps and win to display below
craps_percentage = (face_totals[1] + face_totals[2] + face_totals[11]) / roll_total * 100
win_percentage = (face_totals[6] + face_totals[10]) / roll_total * 100

print(f'\nCraps {craps_percentage:0.2f}% of the time!')
print(f'\n{"Win":>5} {win_percentage:0.2f}% of the time!', '\n')
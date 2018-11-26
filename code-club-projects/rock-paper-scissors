#https://codeclubprojects.org/en-GB/python/rock-paper-scissors/#

from random import randint

#Ask the player to choose rock, paper or scissors
player = input('Do you choose rock (r), paper (p) or scissors (s)?')

#Use this input to print out what the player chose
print(player, 'vs ', end='')


#Use randint to decide whether the computer chooses rock, paper or scissors
chosen = randint(1,3)

#Assign rock, paper or scissors to each integer: 1 = rock (r), 2 = paper (p)
#3 = scissors (s)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's';

#Print the user's input and what they're up against
print(computer)

#Write a function to check player choice and computer choice and print who wins
if player == computer:
    print('Draw!')
elif player == 'r' and computer == 'p':
    print('Computer wins!')
elif player == 'r' and computer == 's':
    print('Player wins!')
elif player == 'p' and computer == 'r':
    print('Player wins!')
elif player == 'p' and computer == 's':
    print('Computer wins!')
elif player == 's' and computer == 'r':
    print('Computer wins!')
elif player == 's' and computer == 'p':
    print('Player wins!')

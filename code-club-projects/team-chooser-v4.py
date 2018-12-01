#https://codeclubprojects.org/en-GB/python/team-chooser/
#What if we had an odd numbers of players?
#The below while loop chooses a random player for team A and then for team B
#However, we get an error if there's an odd number of players because after
#choosing for team A, there's no one left for team B

#Also, add team names

from random import choice

#Create a list of players

players = ['Harry', 'Hermione', 'Neville', 'Ginny', 'Luna']
print(players)

#List of team names
teamNames = ['Alligators', 'Gorilllas', 'Eagles', 'Pythons', 'Wasps', 'Panthers']

#Print the first player in the list using indexing
print(players[0])

#Create empty list to store players
teamA = []
teamB = []

#Create while loop to keep choosing from players until the list = 0

while len(players) > 0:
    #Store the random player choice in new variable playerA
    playerA = choice(players)
    print(playerA)
    #Add randomly chosen playerA to teamA
    teamA.append(playerA)
    #With the player chosen, now remove this player from list of players
    players.remove(playerA)
    #Which players are left?
    print('Players left: ', players)
    
    #If we have an odd number of players, by telling the program to break when
    #the players list is empty we avoid getting an error
    if players == []:
        break

    #Repeat process, but for a new teamB
    playerB = choice(players)
    print(playerB)
    teamB.append(playerB)
    players.remove(playerB)
    print('Players left: ', players)

#Decide what each team is called
teamNameA = choice(teamNames)
#Now remove teamNameA from teamNames
teamNames.remove(teamNameA)

#Repeat for teamB
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

#Print random team names and who is in those teams
print('The players are: ')
print(teamNameA, ': ', teamA)
print(teamNameB, ': ', teamB)

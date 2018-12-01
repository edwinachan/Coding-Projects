#https://codeclubprojects.org/en-GB/python/team-chooser/

from random import choice

#Create a list of players

players = ['Harry', 'Hermione', 'Neville', 'Ginny']
print(players)

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

    #Repeat process, but for a new teamB
    playerB = choice(players)
    print(playerB)
    teamB.append(playerB)
    players.remove(playerB)
    print('Players left: ', players)

print('Team A: ', teamA)
print('Team B: ', teamB)

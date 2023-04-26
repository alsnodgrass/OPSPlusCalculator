"""
Author: Austin Snodgrass
Name: OPS+ Calculator
Purpose: Take user input and use it to calculate players OBP, Slugging and OPS+
Date: 04/24/2023
"""

#Retrieving user input to calculate player statistics
player = input('Player: ')
hits = float(input('Hits: '))
doubles = float(input('Doubles: '))
triples = float(input('Triples: '))
homeRuns = float(input('Home Runs: '))
singles = hits - doubles - triples - homeRuns
walks = float(input('Walks: '))
hbp = float(input('Hit by Pitch: '))
sacFlies = float(input('Sacrifice Flies: '))
atBats = float(input('At Bats: '))

#Setting league statistic variables
leagueOnBase = 0.320
leagueSlugging = 0.402

#Using user input to calculate player statistics and format values to be printed
onBase = round((hits + walks + hbp) / (atBats + walks + hbp + sacFlies), 3)
slugging = round((singles + (doubles * 2) + (triples *3) + (homeRuns * 4)) / atBats, 3)

opsPlus = int(100 * ((onBase / leagueOnBase) + (slugging / leagueSlugging) - 1))

#Printing calculated player statistics
print(player + ' has an OBP of ' + str(onBase) + ' with a slugging of ' + str(slugging) + ' for an OPS+ of ' + str(opsPlus))
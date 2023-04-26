"""
Author:     Austin Snodgrass
Name:       OPS+ Calculator
Date:       04/26/2023
Purpose:    Creates a user interface to input a players statistics and use them to calculate the
    players OBP, Slugging and OPS+. Program should then update interface to display this information
"""

import PySimpleGUI as psg

psg.theme('DarkRed2')

stat_input_left = [
    [
        psg.Text('Player:'),
        psg.In(size = (20, 1), enable_events = True, key = 'PLAYER', justification = 'right')
    ],
    [
        psg.Text('Hits:'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'HITS', justification = 'right')
    ],
    [
        psg.Text('Doubles:'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'DOUBLES', justification = 'right')
    ],
    [
        psg.Text('Triples:'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'TRIPLES', justification = 'right')
    ],
    [
        psg.Text('Home Runs:'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'HOMERUNS', justification = 'right')
    ]
]
stat_input_right = [
    [
        psg.Text('Walks:\t'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'WALKS', justification = 'right')
    ],
    [
        psg.Text('Hit By Pitch:\t'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'HITBYPITCH', justification = 'right')
    ],
    [
        psg.Text('Sac Flies:\t'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'SACFLIES', justification = 'right')
    ],
    [
        psg.Text('At Bats:\t'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'ATBATS', justification = 'right')
    ],
    [
        
        psg.Button('Calculate', size = (25, 1), key = 'CALCULATE')
    ]
]
stat_output = [
    [psg.Text('Please input stats in order to calculate OPS+', key = 'OUTPUT')]
]
layout = [
    [
        psg.Column(stat_input_left),
        psg.VSeperator(),
        psg.Column(stat_input_right)
    ],
    [
        psg.HorizontalSeparator()
    ],
    [
        psg.Column(stat_output)
    ]
]

gui = psg.Window('OPS Plus Calculator', layout)

def calculate():
    player = str(values['PLAYER'])
    hits = float(values['HITS'])
    doubles = float(values['DOUBLES'])
    triples = float(values['TRIPLES'])
    homeRuns = float(values['HOMERUNS'])
    singles = hits - doubles - triples - homeRuns
    walks = float(values['WALKS'])
    hbp = float(values['HITBYPITCH'])
    sacFlies = float(values['SACFLIES'])
    atBats = float(values['ATBATS'])

    leagueOnBase = 0.320
    leagueSlugging = 0.402

    onBase = round((hits + walks + hbp) / (atBats + walks + hbp + sacFlies), 3)
    slugging = round((singles + (doubles * 2) + (triples * 3) + (homeRuns * 4)) / atBats, 3)
    opsPlus = int(100 * ((onBase / leagueOnBase) + (slugging / leagueSlugging) - 1))

    return player, onBase, slugging, opsPlus

while True:
    event, values = gui.read()

    if event == 'CALCULATE':
        statistics = calculate()
        playerPrint = str(statistics[0])
        onBasePrint = str(statistics[1])
        sluggingPrint = str(statistics[2])
        opsPlusPrint = str(statistics[3])
        gui['OUTPUT'].update(playerPrint + ' has an OBP of ' + onBasePrint + ' with a Slugging of ' + sluggingPrint + ' for an OPS Plus of ' + opsPlusPrint)
    if event == psg.WIN_CLOSED:
        break

gui.close()
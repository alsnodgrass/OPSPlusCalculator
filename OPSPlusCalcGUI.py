"""
Author:     Austin Snodgrass
Name:       OPS+ Calculator
Date:       04/27/2023
Purpose:    Creates a user interface to input a players statistics and use them to calculate the
    players OBP, Slugging and OPS+. Program should then update interface to display this information
"""

#Importing packages for UI and setting theme
import PySimpleGUI as psg
psg.theme('DarkRed2')

#Setting message for user to provide data used for calculations
user_message = [
    [psg.Text('Calculations use a league OBP of .320 and a league Slugging of .411.\nAccurate as of 07/17/2023', text_color = 'white')]
]

#Settings up input boxes with references to allow user statistical input
stat_input_left = [
    [
        psg.Text('Player:', text_color = 'white'),
        psg.In(size = (20, 1), enable_events = True, key = 'PLAYER', justification = 'right')
    ],
    [
        psg.Text('Hits:', text_color = 'white'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'HITS', justification = 'right')
    ],
    [
        psg.Text('Doubles:', text_color = 'white'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'DOUBLES', justification = 'right')
    ],
    [
        psg.Text('Triples:', text_color = 'white'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'TRIPLES', justification = 'right')
    ],
    [
        psg.Text('Home Runs:', text_color = 'white'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'HOMERUNS', justification = 'right')
    ]
]
stat_input_right = [
    [
        psg.Text('Walks:\t', text_color = 'white'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'WALKS', justification = 'right')
    ],
    [
        psg.Text('Hit By Pitch:\t', text_color = 'white'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'HITBYPITCH', justification = 'right')
    ],
    [
        psg.Text('Sac Flies:\t', text_color = 'white'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'SACFLIES', justification = 'right')
    ],
    [
        psg.Text('At Bats:\t', text_color = 'white'),
        psg.Push(),
        psg.In(size = (10, 1), enable_events = True, key = 'ATBATS', justification = 'right')
    ],
    [
        
        psg.Button('Calculate', size = (25, 1), key = 'CALCULATE', button_color = ('white', 'dark red'))
    ]
]

#Setting uo output box with directions for user. Message will later change with results from calculations
stat_output = [
    [psg.Text('Please input stats in order to calculate OPS+', key = 'OUTPUT', text_color = 'white')]
]

#Setting the layout for the GUI to include preivously created elements
layout = [
    [
        psg.Column(user_message)
    ],
    [
        psg.HorizontalSeparator()
    ],
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

#Setting up GUI instance and initializing the layout we created
gui = psg.Window('OPS Plus Calculator', layout)

#Defining calculate function to be called later in order to make our statistical calculations based on
#user input. Function returns an index that includes our calculated statistics to be printed to the GUI
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
    leagueSlugging = 0.411

    onBase = round((hits + walks + hbp) / (atBats + walks + hbp + sacFlies), 3)
    slugging = round((singles + (doubles * 2) + (triples * 3) + (homeRuns * 4)) / atBats, 3)
    opsPlus = int(100 * ((onBase / leagueOnBase) + (slugging / leagueSlugging) - 1))

    return player, onBase, slugging, opsPlus

#While loop created to allow user to reuse program until the exit manually. Event reader allows the
#calculate function to be called once the CALCULATE button is pressed. Once the function is called the
#final message is changed to display the players name and statistics
while True:
    event, values = gui.read()

    if event == 'CALCULATE':
        statistics = calculate()
        gui['OUTPUT'].update(str(statistics[0]) + ' has an OBP of ' + str(statistics[1]) + ' with a Slugging of ' + str(statistics[2]) + ' for an OPS Plus of ' + str(statistics[3]))
    if event == psg.WIN_CLOSED:
        break

gui.close()
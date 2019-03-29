from tkinter import *
import os
import csv
import pandas as pd
import analyse_try
import analyse_kicking
import analyse_game
import analyse_substitution
import analyse_scoring
from analyse_penalty import penalty_analysis
from analyse_card import card_analysis

window = Tk()
width = 265
height = 150
window.title("Analysis")
window.minsize(265,150)
window.maxsize(265,150)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

teamList = ["Munster", "Glasgow Warriors", "Ospreys", "Connacht", "Cardiff Blues", "Cheetahs", "Zebre", "Leinster", "Edinburgh", "Benetton", "Scarlets", "Ulster", "Dragons", "Southern Kings"]
team = StringVar(window)
team.set(teamList[0])
menu = OptionMenu(window, team, *teamList)
Label(window, text = "Team to analyse:").place(x = 0, y = 10)
menu.place(x = 0, y = 30)

optionList = ["Scored vs Conceded", "Timing of Tries Scored", "Try Frequency", "First Try", "Total Team Tries", "Penalty", "Card", "Substitution", "Average Sub", "Kick Success", "Conversion", "Form", "Points Spread"]
option = StringVar(window)
option.set(optionList[0])
menu = OptionMenu(window, option, *optionList)
Label(window, text = "What to analyse:").place(x = 135, y = 10)
menu.place(x = 135, y = 30)

def analyse():

    optionChoice = option.get()
    teamChoice = team.get()
    teamChoice = teamChoice.lower()

    info = ["Event", "Card Colour", "Time", "Conversion", "For"]
    time = ['Time']


    if optionChoice == "Total Team Tries" or optionChoice == "First Try":
        with open('tries.csv', 'a+') as tries:
            newRowWriter = csv.writer(tries, lineterminator='\r')
            newRowWriter.writerow(info)
            tries.close()

    if optionChoice == "Average Sub":
        with open('subs.csv', 'a+') as subs:
            newRowWriter = csv.writer(subs, lineterminator='\r')
            newRowWriter.writerow(info)
            subs.close()

    if optionChoice == "Substitution":
        with open('subs.csv', 'a+') as subs:
            newRowWriter = csv.writer(subs, lineterminator='\r')
            newRowWriter.writerow(info)
            subs.close()

    if optionChoice == "Try Frequency":
        with open('tries.csv', 'a+') as tries:
            newRowWriter = csv.writer(tries, lineterminator='\r')
            newRowWriter.writerow(time)
            tries.close()

    file = open("fixtures.txt", "r")
    for line in file:

        filename = line.replace('\n', "").replace('/', "").replace('-', " ")
        filename = filename+".csv"

        if optionChoice == "Card":
            with open(filename) as data:
                with open('cards.csv', 'a+') as cards:
                    for row in data:
                        if optionChoice in row:
                            cards.write(row)

        if optionChoice == "Total Team Tries":
            with open(filename) as data:
                with open('tries.csv', 'a+') as tries:
                    for row in data:
                        if "Try" in row:
                            tries.write(row)

        if optionChoice == "Kick Success":
            with open(filename) as data:
                with open('kicking.csv', 'a+') as kicking:
                    for row in data:
                        if "Try" in row:
                            kicking.write(row)
                        if "Penalty" in row:
                            kicking.write(row)

        if optionChoice == "Average Sub":
            with open(filename) as data:
                with open('subs.csv', 'a+') as subs:
                    for row in data:
                        if "Substitution" in row:
                            subs.write(row)

        elif optionChoice == "First Try":
            with open(filename) as data:
                with open('tries.csv', 'a+') as tries:
                    for row in data:
                        if "Try" in row:
                            tries.write(row)

        if teamChoice in filename and os.path.exists(filename):
            if optionChoice == "Scored vs Conceded" or optionChoice == "Conversion":
                with open(filename) as data:
                    with open('tries.csv', 'a+') as tries:
                        for row in data:
                            if 'Try' in row:
                                tries.write(row)

            elif optionChoice == "Timing of Tries Scored":
                with open(filename) as data:
                    with open('tries.csv', 'a+') as tries:
                        csv_reader = csv.reader(data, delimiter=',')
                        for row in csv_reader:
                            if teamChoice in row:
                                if "Try" in row:
                                    for i, cell in enumerate(row):
                                        if i == 2:
                                            time = ("{cell}".format(**locals()))
                                            tries.write(time + '\n')

            elif optionChoice == "Penalty":
                with open(filename) as data:
                    with open('penalties.csv', 'a+') as penalties:
                        for row in data:
                            if optionChoice in row:
                                penalties.write(row)

            elif optionChoice == "Substitution":
                with open(filename) as data:
                    with open('subs.csv', 'a+') as subs:
                        for row in data:
                            if teamChoice in row:
                                if optionChoice in row:
                                    subs.write(row)

            elif optionChoice == "Form":
                if filename.startswith(teamChoice):
                    with open(filename) as data:
                        with open('home.csv', 'a+') as home:
                            for row in data:
                                if "Home Score" in row:
                                    home.write(row)
                                if "Away Score" in row:
                                    home.write(row)

                else:
                    with open(filename) as data:
                        with open('away.csv', 'a+') as away:
                            for row in data:
                                if "Home Score" in row:
                                    away.write(row)
                                if "Away Score" in row:
                                    away.write(row)

            elif optionChoice == "Try Frequency":
                with open(filename) as data:
                    with open('tries.csv', 'a+') as tries:
                        csv_reader = csv.reader(data, delimiter=',')
                        for row in csv_reader:
                            if teamChoice in row:
                                if "Try" in row:
                                    for i, cell in enumerate(row):
                                        if i == 2:
                                            time = ("{cell}".format(**locals()))
                                            tries.write(time + '\n')

            elif optionChoice == "Points Spread":
                with open(filename) as data:
                    with open('scores.csv', 'a+') as score:
                        for row in data:
                            if "Try" in row:
                                score.write(row)
                            elif "Penalty" in row:
                                score.write(row)
                            elif "Drop Goal" in row:
                                score.write(row)


    window.destroy()

    if optionChoice == "Scored vs Conceded":
        analyse_try.try_analysis(teamChoice)

    elif optionChoice == "Timing of Tries Scored":
        analyse_scoring.timing_of_scores()

    elif optionChoice == "Try Frequency":
        analyse_try.tries_frequency()

    elif optionChoice == "First Try":
        analyse_try.first_try()

    elif optionChoice == "Total Team Tries":
        analyse_try.total_tries()

    elif optionChoice == "Conversion":
        analyse_kicking.conversion_success(teamChoice)

    elif optionChoice == "Kick Success":
        analyse_kicking.total_accuracy()

    elif optionChoice == "Penalty":
        penalty_analysis(teamChoice)

    elif optionChoice == "Card":
        card_analysis()

    elif optionChoice == "Substitution":
        analyse_substitution.substitute_analysis()

    elif optionChoice == "Form":
        analyse_game.match_form(teamChoice)

    elif optionChoice == "Average Sub":
        analyse_substitution.average_sub()

    elif optionChoice == "Points Spread":
        analyse_scoring.total_scores()



button = Button(window, text = "Analyse", command = analyse)
button.place(x = 100, y = 100)
window.mainloop()
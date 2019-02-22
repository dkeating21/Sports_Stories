from tkinter import *
import os
import csv
import pandas as pd
import analyse_try
import analyse_kicking
from analyse_penalty import penalty_analysis
from analyse_card import card_analysis
from analyse_substitution import substitute_analysis

window = Tk()
width = 250
height = 150
window.title("Analysis")
window.minsize(250,150)
window.maxsize(250,150)
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

optionList = ["Try", "Penalty", "Card", "Substitution", "Total Tries", "Kick Success", "Conversion"]
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

    if optionChoice == "Try" or optionChoice == "Total Tries" or optionChoice == "Conversion":
        with open('tries.csv', 'a+') as tries:
            newRowWriter = csv.writer(tries, lineterminator='\r')
            newRowWriter.writerow(info)
            tries.close()


    elif optionChoice == "Penalty":
        with open('penalties.csv', 'a+') as penalties:
            newRowWriter = csv.writer(penalties, lineterminator='\r')
            newRowWriter.writerow(info)
            penalties.close()

    elif optionChoice == "Kicking Accuracy":
        with open('kicking.csv', 'a+') as kicking:
            newRowWriter = csv.writer(kicking, lineterminator='\r')
            newRowWriter.writerow(info)
            kicking.close()

    elif optionChoice == "Card":
        with open('cards.csv', 'a+') as cards:
            newRowWriter = csv.writer(cards, lineterminator='\r')
            newRowWriter.writerow(info)
            cards.close()

    elif optionChoice == "Substitution":
        with open('subs.csv', 'a+') as subs:
            newRowWriter = csv.writer(subs, lineterminator='\r')
            newRowWriter.writerow(info)
            subs.close()

    file = open("fixtures.txt", "r")
    for line in file:

        filename = line.replace('\n', "").replace('/', "").replace('-', " ")
        filename = filename+".csv"

        if optionChoice == "Card":
            with open(filename) as data:
                with open('cards.csv', 'a') as cards:
                    for row in data:
                        if optionChoice in row:
                            cards.write(row)

        if optionChoice == "Total Tries":
            with open(filename) as data:
                with open('tries.csv', 'a') as tries:
                    for row in data:
                        if "Try" in row:
                            tries.write(row)

        if optionChoice == "Kick Success":
            with open(filename) as data:
                with open('kicking.csv', 'a') as kicking:
                    for row in data:
                        if "Try" in row:
                            kicking.write(row)
                        if "Penalty" in row:
                            kicking.write(row)

        if teamChoice in filename and os.path.exists(filename):
            if optionChoice == "Try" or optionChoice == "Conversion":
                with open(filename) as data:
                    with open('tries.csv', 'a+') as tries:
                        for row in data:
                            if 'Try' in row:
                                tries.write(row)

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
                            if optionChoice in row:
                                subs.write(row)

    window.destroy()

    if optionChoice == "Try":
        analyse_try.try_analysis(teamChoice)

    elif optionChoice == "Total Tries":
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
        substitute_analysis(teamChoice)



button = Button(window, text = "Analyse", command = analyse)
button.place(x = 100, y = 100)
window.mainloop()
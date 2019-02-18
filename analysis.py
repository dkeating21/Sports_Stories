from tkinter import *
import os
from analyse_try import try_analysis
from analyse_penalty import penalty_analysis
from analyse_drop_goal import drop_goal_analysis
from analyse_card import card_analysis
from analyse_substitution import substitute_analysis
#from analyse_score import score_analysis

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
Label(window, text = "Team to analyse:").place(x = 5, y = 10)
menu.place(x = 5, y = 30)

optionList = ["Try", "Penalty", "Drop Goal", "Card", "Substitution"]
option = StringVar(window)
option.set(optionList[0])
menu = OptionMenu(window, option, *optionList)
Label(window, text = "What to analyse:").place(x = 140, y = 10)
menu.place(x = 140, y = 30)

def analyse():
    optionChoice = option.get()
    teamChoice = team.get()
    teamChoice = teamChoice.lower()


    file = open("fixtures.txt", "r")
    for line in file:

        filename = line.replace('\n', "").replace('/', "").replace('-', " ")
        filename = filename+".csv"
        if teamChoice in filename and os.path.exists(filename):

            if optionChoice == "Try":
                tries = 'tries.csv'
                if not os.path.exists(tries):
                    triesFile = open(tries, 'a+')
                    with open(filename) as file:
                        for row in file:
                            if optionChoice in row:
                                row = row.replace('\n', "")
                                triesFile.write(row + '\n')
                                triesFile.close()
                try_analysis()


            elif optionChoice == "Penalty":
                penalty_analysis(filename, teamChoice, optionChoice)

            elif optionChoice == "Drop Goal":
                drop_goal_analysis(filename, teamChoice, optionChoice)

            elif optionChoice == "Card":
                card_analysis(filename, teamChoice, optionChoice)

            elif optionChoice == "Substitution":
                substitute_analysis(filename, teamChoice, optionChoice)

            #elif optionChoice == "Score":
            #    score_analysis(filename, teamChoice)

    window.destroy()


button = Button(window, text = "Analyse", command = analyse)
button.place(x = 100, y = 100)
window.mainloop()
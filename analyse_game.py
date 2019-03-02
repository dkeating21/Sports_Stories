import os
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

def match_form(team):

    global awayScore, homeScore
    homeWin = 0
    homeDraw = 0
    homeLoss = 0
    with open('home.csv') as matches:
        csv_reader = csv.reader(matches, delimiter=',')
        for row in csv_reader:
            if "Home Score" in row:
                for i, cell in enumerate(row):
                    if i == 5:
                        homeScore = ("{cell}".format(**locals()))
            if "Away Score" in row:
                for i, cell in enumerate(row):
                    if i == 5:
                        awayScore = ("{cell}".format(**locals()))

                if homeScore > awayScore:
                    homeWin += 1
                elif homeScore < awayScore:
                    homeLoss += 1
                else:
                    homeDraw += 1

        labels = ('Win', 'Loss', 'Draw')
        y_pos = np.arange(len(labels))
        performance = [homeWin, homeLoss, homeDraw]

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, labels)
        plt.ylabel('Total')
        plt.title('Home Form')

        plt.show()

        labels = 'Win', 'Loss', 'Draw'
        sizes = [homeWin, homeLoss, homeDraw]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
        ax1.axis('equal')

        plt.title(team + ' home form')
        plt.show()

    os.remove('home.csv')

    awayWin = 0
    awayDraw = 0
    awayLoss = 0
    with open('away.csv') as data:
        csv_reader = csv.reader(data, delimiter=',')
        for row in csv_reader:
            if "Home Score" in row:
                for i, cell in enumerate(row):
                    if i == 5:
                        homeScore = ("{cell}".format(**locals()))
            if "Away Score" in row:
                for i, cell in enumerate(row):
                    if i == 5:
                        awayScore = ("{cell}".format(**locals()))

                if homeScore < awayScore:
                    awayWin += 1
                elif homeScore > awayScore:
                    awayLoss += 1
                else:
                    awayDraw += 1

        labels = ('Win', 'Loss', 'Draw')
        y_pos = np.arange(len(labels))
        performance = [awayWin, awayLoss, awayDraw]

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, labels)
        plt.ylabel('Total')
        plt.title('Away Form')

        plt.show()

        labels = 'Win', 'Loss', 'Draw'
        sizes = [awayWin, awayLoss, awayDraw]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
        ax1.axis('equal')

        plt.title(team + ' away form')
        plt.show()

    os.remove('away.csv')
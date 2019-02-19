import csv
import os
import glob
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def try_analysis(team):

    converted = 0
    missed = 0
    tries_scored = 0
    tries_conceded = 0
    with open('tries.csv') as file:
        #row_count = sum(1 for row in file)
        for row in file:
            if team in row:
                tries_scored += 1
                if "Converted" in row:
                    converted += 1
                if "Missed" in row:
                    missed += 1
            else:
                tries_conceded += 1


    #print("Total tries scored: ", tries_scored)
    #print("Total tries conceded: ", tries_conceded)

    labels = ('Scored', 'Conceded')
    y_pos = np.arange(len(labels))
    performance = [tries_scored, tries_conceded]

    plt.bar(y_pos, performance, align = 'center', alpha = 0.5)
    plt.xticks(y_pos, labels)
    plt.ylabel('Totals')
    plt.title('Scored vs Conceded')

    plt.show()

    labels = 'Converted', 'Missed'
    sizes = [converted, missed]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
    ax1.axis('equal')

    plt.title('Kicking Accuracy')
    plt.show()


    os.remove('tries.csv')


    """
    data = pd.read_csv(filename)
    grouped = data.groupby(['For', 'Event'])
    for name,group in grouped:
        if name == (teamChoice, eventChoice):
            time = group['Time']
            total_tries = group['Event'].count()
            conversion = group['Conversion'].value_counts(normalize=True)
            conversion = np.round(conversion, decimals=2)

            average = time.mean(axis=0)
            average = np.round(average, decimals=1)
            str1 = filename
            number = str1.find(teamChoice)
            if number == 0:
                home_away = "home"
            else:
                home_away = "away"

            if total_tries != 1:
                print(filename)
                print(teamChoice," were ", home_away)
                #print(group)
                print("Total tries scored: ", total_tries)
                print("First try scored: ", time.min(axis=0))
                print("Last try scored: ", time.max(axis=0))
                print("Average time to score a try: ", average)
                print("Conversion success:\n", conversion, "\n")
            else:
                print(filename)
                print(teamChoice, " were ", home_away)
                #print(group)
                print("Total tries scored: ", total_tries)
                print("Try scored at: ", time.min(axis=0))
                print("Conversion success:\n", conversion, "\n")
    """
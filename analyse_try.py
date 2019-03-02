import csv
import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter

def try_analysis(team):

    tries_scored = 0
    tries_conceded = 0
    with open('tries.csv') as file:
        for row in file:
            if team in row:
                tries_scored += 1
            else:
                tries_conceded += 1

    #print(team + " scored: ", tries_scored)
    #print("Total tries conceded: ", tries_conceded)

    labels = ('Scored', 'Conceded')
    y_pos = np.arange(len(labels))
    performance = [tries_scored, tries_conceded]

    plt.bar(y_pos, performance, align = 'center', alpha = 0.5)
    plt.xticks(y_pos, labels)
    plt.ylabel('Totals')
    plt.title('Scored vs Conceded')

    plt.show()

    os.remove('tries.csv')

def total_tries():

    munster_total = 0
    leinster_total = 0
    ulster_total = 0
    connacht_total = 0
    glasgow_total = 0
    ospreys_total = 0
    cardiff_total = 0
    cheetahs_total = 0
    zebre_total = 0
    edinburgh_total = 0
    benneton_total = 0
    scarlets_total = 0
    dragons_total = 0
    kings_total = 0
    data = pd.read_csv('tries.csv')
    grouped = data.groupby('For')
    for name,group in grouped:
        total = group['Event'].count()
        if name == "munster":
            munster_total = total

        elif name == "leinster":
            leinster_total = total

        elif name == "ulster":
            ulster_total = total

        elif name == "connacht":
            connacht_total = total

        elif name == "glasgow warriors":
            glasgow_total = total

        elif name == "ospreys":
            ospreys_total = total

        elif name == "cardiff blues":
            cardiff_total = total

        elif name == "cheetahs":
            cheetahs_total = total

        elif name == "zebre":
            zebre_total = total

        elif name == "edinburgh":
            edinburgh_total = total

        elif name == "benetton":
            benneton_total = total

        elif name == "scarlets":
            scarlets_total = total

        elif name == "dragons":
            dragons_total = total

        elif name == "southern kings":
            kings_total = total

    labels = ("Munster", "Glasgow", "Ospreys", "Connacht", "Cardiff", "Cheetahs", "Zebre", "Leinster", "Edinburgh", "Benetton", "Scarlets", "Ulster", "Dragons", "Kings")
    y_pos = np.arange(len(labels))
    performance = [munster_total, glasgow_total, ospreys_total, connacht_total, cardiff_total, cheetahs_total, zebre_total, leinster_total, edinburgh_total, benneton_total, scarlets_total, ulster_total, dragons_total, kings_total]
    fig, ax = plt.subplots(figsize=(13.8, 5))

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, labels)
    plt.ylabel('Totals')
    plt.title('Total Tries')

    plt.show()

    os.remove('tries.csv')

def first_try():

    tries = []
    with open('tries.csv') as data:
        for row in data:
            row = row.replace('\n', "")
            tries.append(row)
    print(Counter(tries))

    os.remove('tries.csv')

def tries_frequency():

    with open('tries.csv') as data:
        for row in data:
            row = row.replace('\n', "")
            print(row)

    os.remove('tries.csv')
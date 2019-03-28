import csv
import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

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

    munster_try = 0
    leinster_try = 0
    ulster_try = 0
    connacht_try = 0
    glasgow_try = 0
    ospreys_try = 0
    cardiff_try = 0
    cheetahs_try = 0
    zebre_try = 0
    edinburgh_try = 0
    benneton_try = 0
    scarlets_try = 0
    dragons_try = 0
    kings_try = 0
    data = pd.read_csv('tries.csv')
    grouped = data.groupby(['For', 'Event'])
    for name, group in grouped:
        if name == ("munster", "Try"):
            time = group['Time']
            munster_try = time.mean(axis=0)

        elif name == ("leinster", "Try"):
            time = group['Time']
            leinster_try = time.mean(axis=0)

        elif name == ("ulster", "Try"):
            time = group['Time']
            ulster_try = time.mean(axis=0)

        elif name == ("connacht", "Try"):
            time = group['Time']
            connacht_try = time.mean(axis=0)

        elif name == ("glasgow warriors", "Try"):
            time = group['Time']
            glasgow_try = time.mean(axis=0)

        elif name == ("ospreys", "Try"):
            time = group['Time']
            ospreys_try = time.mean(axis=0)

        elif name == ("cardiff blues", "Try"):
            time = group['Time']
            cardiff_try = time.mean(axis=0)

        elif name == ("cheetahs", "Try"):
            time = group['Time']
            cheetahs_try = time.mean(axis=0)

        elif name == ("zebre", "Try"):
            time = group['Time']
            zebre_try = time.mean(axis=0)

        elif name == ("edinburgh", "Try"):
            time = group['Time']
            edinburgh_try = time.mean(axis=0)

        elif name == ("benetton", "Try"):
            time = group['Time']
            benneton_try = time.mean(axis=0)

        elif name == ("scarlets", "Try"):
            time = group['Time']
            scarlets_try = time.mean(axis=0)

        elif name == ("dragons", "Try"):
            time = group['Time']
            dragons_try = time.mean(axis=0)

        elif name == ("southern kings", "Try"):
            time = group['Time']
            kings_try = time.mean(axis=0)

    labels = ("Munster", "Glasgow", "Ospreys", "Connacht", "Cardiff", "Cheetahs", "Zebre", "Leinster", "Edinburgh", "Benetton", "Scarlets", "Ulster", "Dragons", "Kings")
    y_pos = np.arange(len(labels))
    performance = [munster_try, glasgow_try, ospreys_try, connacht_try, cardiff_try, cheetahs_try, zebre_try, leinster_try, edinburgh_try, benneton_try, scarlets_try, ulster_try, dragons_try, kings_try]
    fig, ax = plt.subplots(figsize=(13.8, 5))

    plt.scatter(y_pos, performance, label='center', color='red')
    plt.xticks(y_pos, labels)
    plt.xlabel('Teams')
    plt.ylabel('Time')
    plt.title('Average Time to Score First Try')

    plt.show()
    """
    data = pd.read_csv('tries.csv')
    tryCount = pd.DataFrame(data['Time'].value_counts())

    y = np.arange(len(tryCount.index.tolist()))

    plt.scatter(y, tryCount['Time'], label = 'center', color = 'red')
    plt.xticks(y, tryCount.index.tolist())
    plt.xlabel('Time')
    plt.ylabel('Total')
    plt.title('First Try Scored')

    plt.show()
    """

    os.remove('tries.csv')

def tries_frequency():

    data = pd.read_csv('tries.csv')
    tryCount = pd.DataFrame(data['Time'].value_counts())

    y = np.arange(len(tryCount.index.tolist()))

    plt.figure(figsize=(13.5, 5))
    plt.bar(y, tryCount['Time'], align='center', alpha = 0.5)
    plt.xticks(y, tryCount.index.tolist())
    plt.xlabel('Time')
    plt.ylabel('Total')
    plt.title('Try Frequency')

    plt.show()

    os.remove('tries.csv')
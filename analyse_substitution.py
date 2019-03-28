import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt

def substitute_analysis():

    data = pd.read_csv('subs.csv')
    subCount = pd.DataFrame(data['Time'].value_counts())

    # print(tryCount)
    y = np.arange(len(subCount.index.tolist()))

    plt.figure(figsize=(13.5, 5))
    plt.bar(y, subCount['Time'], align='center', alpha=0.5)
    plt.xticks(y, subCount.index.tolist())
    plt.xlabel('Time')
    plt.ylabel('Total')
    plt.title('Substitutions')

    plt.show()

    """
    data = pd.read_csv('subs.csv')
    grouped = data.groupby('Event')
    for name, group in grouped:
        if name == "Substitution":
            time = group['Time']
            total_time = time.value_counts()
            average = time.mean(axis=0)
            average = np.round(average, decimals=0)
            print("Total substitutions: ", time.count())
            print("Average substitution time: ", average)
            print(total_time)
    """
    os.remove('subs.csv')


def average_sub():

    munster_subs = 0
    leinster_subs = 0
    ulster_subs = 0
    connacht_subs = 0
    glasgow_subs = 0
    ospreys_subs = 0
    cardiff_subs = 0
    cheetahs_subs = 0
    zebre_subs = 0
    edinburgh_subs = 0
    benneton_subs = 0
    scarlets_subs = 0
    dragons_subs = 0
    kings_subs = 0
    data = pd.read_csv('subs.csv')
    grouped = data.groupby(['For', 'Event'])
    for name, group in grouped:
        if name == ("munster", "Substitution"):
            time = group['Time']
            munster_subs = time.mean(axis=0)

        elif name == ("leinster", "Substitution"):
            time = group['Time']
            leinster_subs = time.mean(axis=0)

        elif name == ("ulster", "Substitution"):
            time = group['Time']
            ulster_subs = time.mean(axis=0)

        elif name == ("connacht", "Substitution"):
            time = group['Time']
            connacht_subs = time.mean(axis=0)

        elif name == ("glasgow warriors", "Substitution"):
            time = group['Time']
            glasgow_subs = time.mean(axis=0)

        elif name == ("ospreys", "Substitution"):
            time = group['Time']
            ospreys_subs = time.mean(axis=0)

        elif name == ("cardiff blues", "Substitution"):
            time = group['Time']
            cardiff_subs = time.mean(axis=0)

        elif name == ("cheetahs", "Substitution"):
            time = group['Time']
            cheetahs_subs = time.mean(axis=0)

        elif name == ("zebre", "Substitution"):
            time = group['Time']
            zebre_subs = time.mean(axis=0)

        elif name == ("edinburgh", "Substitution"):
            time = group['Time']
            edinburgh_subs = time.mean(axis=0)

        elif name == ("benetton", "Substitution"):
            time = group['Time']
            benneton_subs = time.mean(axis=0)

        elif name == ("scarlets", "Substitution"):
            time = group['Time']
            scarlets_subs = time.mean(axis=0)

        elif name == ("dragons", "Substitution"):
            time = group['Time']
            dragons_subs = time.mean(axis=0)

        elif name == ("southern kings", "Substitution"):
            time = group['Time']
            kings_subs = time.mean(axis=0)

    labels = ("Munster", "Glasgow", "Ospreys", "Connacht", "Cardiff", "Cheetahs", "Zebre", "Leinster", "Edinburgh", "Benetton", "Scarlets", "Ulster", "Dragons", "Kings")
    y_pos = np.arange(len(labels))
    performance = [munster_subs, glasgow_subs, ospreys_subs, connacht_subs, cardiff_subs, cheetahs_subs, zebre_subs, leinster_subs, edinburgh_subs, benneton_subs, scarlets_subs, ulster_subs, dragons_subs, kings_subs]
    fig, ax = plt.subplots(figsize=(13.8, 5))

    plt.scatter(y_pos, performance, label='center', color='red')
    plt.xticks(y_pos, labels)
    plt.xlabel('Teams')
    plt.ylabel('Time')
    plt.title('Average Time to Sub')

    plt.show()
    """
    plt.scatter(y, subCount['Time'], label='center', color='red')
    plt.xticks(y, subCount.index.tolist())
    plt.xlabel('Time')
    plt.ylabel('Total')
    plt.title('Substitutions')

    plt.show()
    """

    """
    data = pd.read_csv('subs.csv')
    grouped = data.groupby('Event')
    for name, group in grouped:
        if name == "Substitution":
            time = group['Time']
            total_time = time.value_counts()
            average = time.mean(axis=0)
            average = np.round(average, decimals=0)
            print("Total substitutions: ", time.count())
            print("Average substitution time: ", average)
            print(total_time)
    """
    os.remove('subs.csv')

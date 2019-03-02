import os
from matplotlib import pyplot as plt
import numpy as np

def conversion_success(team):

    converted = 0
    missed = 0

    with open('tries.csv') as file:
        for row in file:
            if team in row:
                if "Converted" in row:
                    converted += 1
                if "Missed" in row:
                    missed += 1

    labels = 'Converted', 'Missed'
    sizes = [converted, missed]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
    ax1.axis('equal')

    plt.title(team + ' conversion accuracy')
    plt.show()

    os.remove('tries.csv')

def total_accuracy():
    munster_converted = 0
    leinster_converted = 0
    ulster_converted = 0
    connacht_converted = 0
    glasgow_converted = 0
    ospreys_converted = 0
    cardiff_converted = 0
    cheetahs_converted = 0
    zebre_converted = 0
    edinburgh_converted = 0
    benneton_converted = 0
    scarlets_converted = 0
    dragons_converted = 0
    kings_converted = 0
    munster_missed = 0
    leinster_missed = 0
    ulster_missed = 0
    connacht_missed = 0
    glasgow_missed = 0
    ospreys_missed = 0
    cardiff_missed = 0
    cheetahs_missed = 0
    zebre_missed = 0
    edinburgh_missed = 0
    benneton_missed = 0
    scarlets_missed = 0
    dragons_missed = 0
    kings_missed = 0
    with open('kicking.csv') as file:
        for row in file:
            if "munster" in row:
                if "Converted" in row:
                    munster_converted += 1
                if "Missed" in row:
                    munster_missed += 1

            elif "leinster" in row:
                if "Converted" in row:
                    leinster_converted += 1
                if "Missed" in row:
                    leinster_missed += 1

            elif "ulster" in row:
                if "Converted" in row:
                    ulster_converted += 1
                if "Missed" in row:
                    ulster_missed += 1

            elif "connacht" in row:
                if "Converted" in row:
                    connacht_converted += 1
                if "Missed" in row:
                    connacht_missed += 1

            elif "glasgow warriors" in row:
                if "Converted" in row:
                    glasgow_converted += 1
                if "Missed" in row:
                    glasgow_missed += 1

            elif "ospreys" in row:
                if "Converted" in row:
                    ospreys_converted += 1
                if "Missed" in row:
                    ospreys_missed += 1

            elif "cardiff blues" in row:
                if "Converted" in row:
                    cardiff_converted += 1
                if "Missed" in row:
                    cardiff_missed += 1

            elif "cheetahs" in row:
                if "Converted" in row:
                    cheetahs_converted += 1
                if "Missed" in row:
                    cheetahs_missed += 1

            elif "zebre" in row:
                if "Converted" in row:
                    zebre_converted += 1
                if "Missed" in row:
                    zebre_missed += 1

            elif "edinburgh" in row:
                if "Converted" in row:
                    edinburgh_converted += 1
                if "Missed" in row:
                    edinburgh_missed += 1

            elif "benetton" in row:
                if "Converted" in row:
                    benneton_converted += 1
                if "Missed" in row:
                    benneton_missed += 1

            elif "scarlets" in row:
                if "Converted" in row:
                    scarlets_converted += 1
                if "Missed" in row:
                    scarlets_missed += 1

            elif "dragons" in row:
                if "Converted" in row:
                    dragons_converted += 1
                if "Missed" in row:
                    dragons_missed += 1

            elif "southern kings" in row:
                if "Converted" in row:
                    kings_converted += 1
                if "Missed" in row:
                    kings_missed += 1

    n_groups = 14
    converted = [munster_converted, glasgow_converted, ospreys_converted, connacht_converted, cardiff_converted, cheetahs_converted, zebre_converted, leinster_converted, edinburgh_converted, benneton_converted, scarlets_converted, ulster_converted, dragons_converted, kings_converted]
    missed = [munster_missed, glasgow_missed, ospreys_missed, connacht_missed, cardiff_missed, cheetahs_missed, zebre_missed, leinster_missed, edinburgh_missed, benneton_missed, scarlets_missed, ulster_missed, dragons_missed, kings_missed]
    fig, ax = plt.subplots(figsize=(13.5, 5))
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, converted, bar_width, alpha=opacity, color='g', label='Converted')

    rects2 = plt.bar(index + bar_width, missed, bar_width, alpha=opacity, color='r', label='Missed')

    plt.xlabel('Team')
    plt.ylabel('Total of kicks')
    plt.title('Kicking Success')
    plt.xticks(index + bar_width, ("Munster", "Glasgow", "Ospreys", "Connacht", "Cardiff", "Cheetahs", "Zebre", "Leinster", "Edinburgh", "Benetton", "Scarlets", "Ulster", "Dragons", "Kings"))
    plt.legend()

    plt.tight_layout()
    plt.show()

    os.remove('kicking.csv')

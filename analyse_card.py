import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

def card_analysis():

    munster_yellow = 0
    munster_red = 0
    leinster_yellow = 0
    leinster_red = 0
    ulster_yellow = 0
    ulster_red = 0
    connacht_yellow = 0
    connacht_red = 0
    glasgow_yellow = 0
    glasgow_red = 0
    ospreys_yellow = 0
    ospreys_red = 0
    cardiff_yellow = 0
    cardiff_red = 0
    cheetahs_yellow = 0
    cheetahs_red = 0
    zebre_yellow = 0
    zebre_red = 0
    edinburgh_yellow = 0
    edinburgh_red = 0
    benneton_yellow = 0
    benneton_red = 0
    scarlets_yellow = 0
    scarlets_red = 0
    dragons_yellow = 0
    dragons_red = 0
    kings_yellow = 0
    kings_red = 0
    with open('cards.csv') as cards:
        for row in cards:
            if "munster" in row:
                if "Yellow" in row:
                    munster_yellow += 1
                if "Red" in row:
                    munster_red += 1

            elif "leinster" in row:
                if "Yellow" in row:
                    leinster_yellow += 1
                if "Red" in row:
                    leinster_red += 1

            elif "ulster" in row:
                if "Yellow" in row:
                    ulster_yellow += 1
                if "Red" in row:
                    ulster_red += 1

            elif "connacht" in row:
                if "Yellow" in row:
                    connacht_yellow += 1
                if "Red" in row:
                    connacht_red += 1

            elif "glasgow warriors" in row:
                if "Yellow" in row:
                    glasgow_yellow += 1
                if "Red" in row:
                    glasgow_red += 1

            elif "ospreys" in row:
                if "Yellow" in row:
                    ospreys_yellow += 1
                if "Red" in row:
                    ospreys_red += 1

            elif "cardiff blues" in row:
                if "Yellow" in row:
                    cardiff_yellow += 1
                if "Red" in row:
                    cardiff_red += 1

            elif "cheetahs" in row:
                if "Yellow" in row:
                    cheetahs_yellow += 1
                if "Red" in row:
                    cheetahs_red += 1

            elif "zebre" in row:
                if "Yellow" in row:
                    zebre_yellow += 1
                if "Red" in row:
                    zebre_red += 1

            elif "edinburgh" in row:
                if "Yellow" in row:
                    edinburgh_yellow += 1
                if "Red" in row:
                    edinburgh_red += 1

            elif "benetton" in row:
                if "Yellow" in row:
                    benneton_yellow += 1
                if "Red" in row:
                    benneton_red += 1

            elif "scarlets" in row:
                if "Yellow" in row:
                    scarlets_yellow += 1
                if "Red" in row:
                    scarlets_red += 1

            elif "dragons" in row:
                if "Yellow" in row:
                    dragons_yellow += 1
                if "Red" in row:
                    dragons_red += 1

            elif "southern kings" in row:
                if "Yellow" in row:
                    kings_yellow += 1
                if "Red" in row:
                    kings_red += 1

    n_groups = 14
    yellow = (munster_yellow, leinster_yellow, ulster_yellow, connacht_yellow, glasgow_yellow, ospreys_yellow, cardiff_yellow, cheetahs_yellow, zebre_yellow, edinburgh_yellow, benneton_yellow, scarlets_yellow, dragons_yellow, kings_yellow)
    red = (munster_red, leinster_red, ulster_red, connacht_red, glasgow_red, ospreys_red, cardiff_red, cheetahs_red, zebre_red, edinburgh_red, benneton_red, scarlets_red, dragons_red, kings_red)
    fig, ax = plt.subplots(figsize=(13.5, 5))
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, yellow, bar_width,alpha=opacity,color='y',label='Yellow')

    rects2 = plt.bar(index + bar_width, red, bar_width,alpha=opacity,color='r',label='Red')

    plt.xlabel('Team')
    plt.ylabel('Total of cards')
    plt.title('Discipline')
    plt.xticks(index + bar_width, ("Munster", "Glasgow", "Ospreys", "Connacht", "Cardiff", "Cheetahs", "Zebre", "Leinster", "Edinburgh", "Benetton", "Scarlets", "Ulster", "Dragons", "Kings"))
    plt.legend()

    plt.tight_layout()
    plt.show()

    os.remove('cards.csv')
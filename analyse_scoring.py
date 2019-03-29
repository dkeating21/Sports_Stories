import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
def total_scores():

    converted_tries = 0
    unconverted_tries = 0
    penalty_goals = 0
    drop_goals = 0

    with open("scores.csv") as scores:
        for row in scores:
            if "Try" in row:
                if "Converted" in row:
                    converted_tries = converted_tries + 1
                elif "Missed" in row:
                    unconverted_tries = unconverted_tries + 1
            elif "Penalty" in row:
                if "Converted" in row:
                    penalty_goals = penalty_goals + 1
            elif "Drop Goal" in row:
                drop_goals = drop_goals + 1

    plt.figure(figsize=(10, 5))
    labels = ('Converted Tries', 'Unconverted Tries', 'Penalties Scored', 'Drop Goal')
    y_pos = np.arange(len(labels))
    performance = [converted_tries * 7, unconverted_tries * 5, penalty_goals * 3, drop_goals * 3]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, labels)
    plt.ylabel('Totals')
    plt.title('Points Scored')

    plt.show()

    labels = ('Converted Tries', 'Unconverted Tries', 'Penalties Scored', 'Drop Goal')
    sizes = [converted_tries, unconverted_tries, penalty_goals, drop_goals]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')

    plt.title('Points Spread')
    plt.show()

    os.remove('scores.csv')

def timing_of_scores():

    first_half = 0
    second_half = 0

    with open("tries.csv") as scores:
        for row in scores:
            row = int(row)
            if row <= 40:
                first_half = first_half + 1
            else:
                second_half = second_half + 1

    labels = ('First Half', 'Second Half')
    y_pos = np.arange(len(labels))
    performance = [first_half, second_half]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, labels)
    plt.ylabel('Totals')
    plt.title('Time of Scoring Tries')

    plt.show()

    labels = ('First Half', 'Second Half')
    sizes = [first_half, second_half]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')

    plt.title('Time of Scoring Tries Breakdown')
    plt.show()

    os.remove('tries.csv')
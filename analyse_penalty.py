import pandas as pd
from matplotlib import pyplot as plt
import os
import numpy as np

def penalty_analysis(team):

    penalties_for = 0
    penalties_against = 0
    scored = 0
    missed = 0
    with open('penalties.csv') as penalties:
        for row in penalties:
            if team in row:
                penalties_for += 1
                if "Converted" in row:
                    scored += 1
                if "Missed" in row:
                    missed += 1
            else:
                penalties_against += 1

    labels = ('For', 'Against')
    y_pos = np.arange(len(labels))
    performance = [penalties_for, penalties_against]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, labels)
    plt.ylabel('Totals')

    plt.title('Penalties')
    plt.show()

    labels = 'Scored', 'Missed'
    sizes = [scored, missed]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')

    plt.title('Penalty Accuracy')
    plt.show()
    """
    data = pd.read_csv('penalties.csv')
    grouped = data.groupby(['For'])
    for name, group in grouped:
        if name == team:
            time = group['Time']
            print(group)
            print("First penalty: ", time.min(axis=0))
            print("Last penalty: ", time.max(axis=0))
            print("Total penalties scored: ", time.count())
            print("Average time to score a penalty: ", time.mean(axis=0))
    """

    os.remove('penalties.csv')
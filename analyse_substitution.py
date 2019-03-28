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
    plt.scatter(y, subCount['Time'], label='center', color='red')
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


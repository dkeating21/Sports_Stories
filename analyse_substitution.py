import pandas as pd
import numpy as np
import os

def substitute_analysis():

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
    os.remove('subs.csv')


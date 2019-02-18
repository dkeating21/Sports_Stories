import pandas as pd
import numpy as np

def substitute_analysis(filename, teamChoice, eventChoice):

    data = pd.read_csv(filename)
    grouped = data.groupby(['For', 'Event'])
    for name, group in grouped:
        if name == (teamChoice, eventChoice):
            time = group['Time']
            print(filename)
            print(group)
            print("First substitute: ", time.min(axis=0))
            print("Last substitute: ", time.max(axis=0))
            print("Average time to make a substitute: ", time.mean(axis=0))
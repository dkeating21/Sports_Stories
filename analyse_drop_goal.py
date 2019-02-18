import pandas as pd
import numpy as np

def drop_goal_analysis(filename, teamChoice, eventChoice):
    data = pd.read_csv(filename)
    grouped = data.groupby(['For', 'Event'])
    for name, group in grouped:
        if name == (teamChoice, eventChoice):
            time = group['Time']
            print(filename)
            print(group)
            print("First drop goal: ", time.min(axis=0))
            print("Last drop goal: ", time.max(axis=0))
            print("Average time to score a drop goal: ", time.mean(axis=0))
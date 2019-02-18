import pandas as pd
import numpy as np

def card_analysis(filename, teamChoice, eventChoice):

    data = pd.read_csv(filename)
    grouped = data.groupby(['For', 'Event'])
    for name, group in grouped:
        if name == (teamChoice, eventChoice):
            time = group['Time']
            card = group['Card Colour']

            print(filename)
            #print(group)
            print("First card: ", time.min(axis=0))
            print("Last card: ", time.max(axis=0))
            print("Average time to get a card: ", time.mean(axis=0))
            print("Card ratio:\n", card, "\n")

import csv
#import os
import glob
import pandas as pd
#from matplotlib import pyplot as plt
import numpy as np

def try_analysis():

    with open('tries.csv') as tries:
        reader = csv.reader(tries, delimiter = '\n')
        for row in reader:
            print(row)









    """
    data = pd.read_csv(filename)
    grouped = data.groupby(['For', 'Event'])
    for name,group in grouped:
        if name == (teamChoice, eventChoice):
            time = group['Time']
            total_tries = group['Event'].count()
            conversion = group['Conversion'].value_counts(normalize=True)
            conversion = np.round(conversion, decimals=2)

            average = time.mean(axis=0)
            average = np.round(average, decimals=1)
            str1 = filename
            number = str1.find(teamChoice)
            if number == 0:
                home_away = "home"
            else:
                home_away = "away"

            if total_tries != 1:
                print(filename)
                print(teamChoice," were ", home_away)
                #print(group)
                print("Total tries scored: ", total_tries)
                print("First try scored: ", time.min(axis=0))
                print("Last try scored: ", time.max(axis=0))
                print("Average time to score a try: ", average)
                print("Conversion success:\n", conversion, "\n")
            else:
                print(filename)
                print(teamChoice, " were ", home_away)
                #print(group)
                print("Total tries scored: ", total_tries)
                print("Try scored at: ", time.min(axis=0))
                print("Conversion success:\n", conversion, "\n")
    """
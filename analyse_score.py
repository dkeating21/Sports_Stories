import pandas as pd
import numpy as np

def score_analysis(filename, teamChoice):

    data = pd.read_csv(filename)
    grouped = data.groupby('For')
    for name,group in grouped:
        if name == teamChoice:
            print(filename)
            print(group)
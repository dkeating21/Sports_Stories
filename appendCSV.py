import csv
import os

def writeToFile(info, file):
    if os.path.exists(file):
        with open(file, "a") as file:
                newRowWriter = csv.writer(file, lineterminator = '\r')
                newRowWriter.writerow(info)
                file.close()

"""
def writeToFile(info):

    if os.path.exists("rugby_data.csv"):
        with open("rugby_data.csv", "a") as file:
            newRowWriter = csv.writer(file, lineterminator = '\r')
            newRowWriter.writerow(info)
            file.close()
    else:
        open("rugby_data.csv", "x")
        with open("rugby_data.csv", "a") as file:
            newRowWriter = csv.writer(file, lineterminator='\r')
            newRowWriter.writerow(info)
            file.close()
"""
import os

def createFile(filename):
    filename = filename.replace('\n', "").replace('/',"").replace('-'," ")
    if not os.path.exists(filename):
        try:
            filename = filename+".csv"
            open(filename, "x")
            with open(filename, "a") as file:
                file.close()
            return filename
        except FileExistsError:
            """print("File " + filename + " exists")"""
            return False
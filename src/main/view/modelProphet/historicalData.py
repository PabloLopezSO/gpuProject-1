import glob
import os
import pandas as pd

dirName:str = os.path.dirname(os.path.abspath(__file__))

def mergeAllCsvInOne():
    csvFilesToBeMerged = os.path.join(dirName, "*.csv")  
    csvFilesToBeMerged = glob.glob(csvFilesToBeMerged)
    df:pd = pd.concat(map(pd.read_csv, csvFilesToBeMerged), ignore_index=True)
    df.to_csv(f'{dirName}{os.sep}historicalData.csv', index=False)


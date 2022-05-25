import os
import time
import luigi
import model.procedure as procedure
from view.modelProphet import historicalData

dirName:str = os.path.dirname(os.path.abspath(__file__))
finalDir:str = os.path.join(dirName, f'data{os.sep}gpuCrawlers{os.sep}tmp')
dbDir:str = os.path.join(dirName, 'model')
viewDir:str = os.path.join(dirName, 'view')
sleepDeleteTempFiles = 5



#Dump dataBase Records to csv
class ExecuteProcedureDumpDataBaseCsv(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'dump.tmp')
    def run(self):
        open('dump.tmp', 'w')
        return procedure.dumpDataToCsv()

#Dump dataBase Records to csv
class MergeCsvHistoricalData(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'dump.tmp')
    def requires(self):
        return ExecuteProcedureDumpDataBaseCsv()
    def run(self):
        return historicalData.mergeAllCsvInOne()

#Execute StreamLit 
class ExecuteStreamLit(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'dump.tmp')
    def requires(self):
        return MergeCsvHistoricalData()
    def run(self):
        time.sleep(sleepDeleteTempFiles)
        filesInDirectory = os.listdir(dirName)
        filteredFiles = [file for file in filesInDirectory if file.endswith(".tmp")]
        for file in filteredFiles:
            pathFile = os.path.join(file)
            print(pathFile)
            os.remove(pathFile)
        return os.system(f"cd {viewDir} && streamlit run streamLit.py")

       
if __name__ == '__main__':
    luigi.run()
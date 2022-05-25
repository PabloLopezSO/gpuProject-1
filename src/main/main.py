import os
import time
import luigi
import model.procedure as procedure
from sentinelBot import gpuProjectBot

dirName:str = os.path.dirname(__file__)
finalDir:str = os.path.join(dirName, f'data{os.sep}gpuCrawlers{os.sep}tmp')
dbDir:str = os.path.join(dirName, 'model')
sleepDeleteTempFiles = 5

class CrawlCoolModLinks(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{finalDir}{os.sep}coolModLinks.json')
    def run(self):
        gpuProjectBot.botTelegramSendMessage('CrawlCoolModLinks Task Starting ..')
        os.system(f"cd {finalDir} && scrapy crawl coolModLinks")
        gpuProjectBot.botTelegramSendMessage('CrawlCoolModLinks Task Finished !')

class CrawlCoolMod(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{finalDir}{os.sep}coolModRTX.json')
    def requires(self):
        return CrawlCoolModLinks()
    def run(self):
        gpuProjectBot.botTelegramSendMessage('CrawlCoolMod Task Starting ..')
        os.system(f"cd {finalDir} && scrapy crawl coolModRTX -O coolModRTX.json")
        gpuProjectBot.botTelegramSendMessage('CrawlCoolMod Task Finished !')

class CrawlAmazon(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{finalDir}{os.sep}amazonRTX.json')
    def requires(self):
        return CrawlCoolMod()
    def run(self):
        gpuProjectBot.botTelegramSendMessage('CrawlAmazon Task Starting ..')
        os.system(f"cd {finalDir} && scrapy crawl amazonRTX -O amazonRTX.json")
        gpuProjectBot.botTelegramSendMessage('CrawlAmazon Task Finished !')

#DumpData mysql DB
class DumpDatabase(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{finalDir}{os.sep}amazonRTX.json')
    def requires(self):
        return CrawlAmazon()
    def run(self):
        gpuProjectBot.botTelegramSendMessage('DumpData Task Starting ..')
        os.system(f"cd {dbDir} && python main.py")
        gpuProjectBot.botTelegramSendMessage('DumpData Task Finished !')

#Execute Procedures --> Clean Data From Crawlers
class ExecuteProcedureDeleteNoRtx3000(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{finalDir}{os.sep}amazonRTX.json')
    def requires(self):
        return DumpDatabase()
    def run(self):
        gpuProjectBot.botTelegramSendMessage('ExecuteProcedureDeleteNoRTX3000 Task Starting ..')
        procedure.deleteNoRtx3000()
        gpuProjectBot.botTelegramSendMessage('ExecuteProcedureDeleteNoRTX3000 Task Finished !')

#Execute Procedures --> Clean Data From Crawlers
class ExecuteProcedureDeleteNoStock(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{finalDir}{os.sep}amazonRTX.json')
    def requires(self):
        return ExecuteProcedureDeleteNoRtx3000()
    def run(self):
        gpuProjectBot.botTelegramSendMessage('ExecuteProcedureDeleteNoStock Task Starting ..')
        procedure.deleteNoStock()
        gpuProjectBot.botTelegramSendMessage('ExecuteProcedureDeleteNoStock Task Finished !')

#Execute Procedures --> Clean Data From Crawlers
class ExecuteProceduresDeleteMisc(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{finalDir}{os.sep}amazonRTX.json')
    def requires(self):
        return ExecuteProcedureDeleteNoStock()
    def run(self):
        gpuProjectBot.botTelegramSendMessage('ExecuteProceduresDeleteMisc Task Starting ..')
        procedure.deleteMisc()
        gpuProjectBot.botTelegramSendMessage('ExecuteProceduresDeleteMisc Task Finished !')

#Execute Procedures --> Clean Data From Crawlers
class ExecuteProceduresDeleteMinusChars(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{finalDir}{os.sep}amazonRTX.json')
    def requires(self):
        return ExecuteProceduresDeleteMisc()
    def run(self):
        gpuProjectBot.botTelegramSendMessage('ExecuteProceduresDeleteMinusChar Task Starting ..')
        procedure.deleteMinusChar()
        gpuProjectBot.botTelegramSendMessage('ExecuteProceduresDeleteMinusChar Task Finished !')

#Execute Procedures --> Clean Data From Crawlers
class ExecuteProceduresUpdateMisc(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{finalDir}{os.sep}amazonRTX.json')
    def requires(self):
        return ExecuteProceduresDeleteMinusChars()
    def run(self):
        gpuProjectBot.botTelegramSendMessage('ExecuteProceduresUpdateMisc Task Starting ..')
        procedure.updateMisc()
        gpuProjectBot.botTelegramSendMessage('ExecuteProceduresUpdateMisc Task Finished !')

#Execute Procedures --> Clean Data From Crawlers
class ExecuteProceduresDeleteComma(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{finalDir}{os.sep}amazonRTX.json')
    def requires(self):
        return ExecuteProceduresUpdateMisc()
    def run(self):
        gpuProjectBot.botTelegramSendMessage('ExecuteProceduresDeleteComma Task Starting ..')
        procedure.deleteComma()
        gpuProjectBot.botTelegramSendMessage('ExecuteProceduresDeleteComma Task Finished !')

#Execute Procedures --> Clean Data From Crawlers
class ExecuteProceduresDeleteParenthesis(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{finalDir}{os.sep}amazonRTX.json')
    def requires(self):
        return ExecuteProceduresDeleteComma()
    def run(self):
        gpuProjectBot.botTelegramSendMessage('ExecuteProceduresDeleteParenthesis Task Starting ..')
        procedure.deleteParenthesis()
        gpuProjectBot.botTelegramSendMessage('ExecuteProceduresDeleteParenthesis Task Finished !')

#Delete Temp files.json
class DeleteTempFiles(luigi.Task):
    def requires(self):
        return ExecuteProceduresDeleteParenthesis()
    def run(self):
        gpuProjectBot.botTelegramSendMessage('DeleteTempFiles Task Starting ..')
        time.sleep(sleepDeleteTempFiles)
        filesInDirectory = os.listdir(finalDir)
        filteredFiles = [file for file in filesInDirectory if file.endswith(".json")]
        for file in filteredFiles:
            pathFile = os.path.join(finalDir, file)
            os.remove(pathFile)
        gpuProjectBot.botTelegramSendMessage('DeleteTempFiles Task Finished !')
        gpuProjectBot.botTelegramSendMessage('All Primordial Tasks Finished (っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ ) ')


if __name__ == '__main__':
    luigi.run()
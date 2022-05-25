import sys
import sqlalchemy
import dataBase
from models import GpuData
from sqlalchemy.exc import OperationalError
import json
import os

def jsonData(fileName:str):
    dirName:str = os.path.dirname(os.path.abspath(__file__).replace(f"{os.sep}model", ""))
    fileName:str = os.path.join(f'{dirName}{os.sep}data{os.sep}gpuCrawlers{os.sep}tmp', fileName)
    jsonFile = open(fileName)
    jsonData = json.load(jsonFile)
    return jsonData


# AMAZON CRAWLER JSON
gpuAmazon_data:list = []
try: 
    for products in jsonData('amazonRTX.json'):
        if 'productPrice' not in products:
            products['productPrice'] = 'No stock'
        gpuAmazon_data.append(GpuData(products['productName'] , products['productPrice'].replace(',', ''), products['productDate']))
except OSError:
    dirName:str = os.path.dirname(os.path.abspath(__file__).replace(f"{os.sep}model", ""))
    finalDir:str = os.path.join(f'{dirName}{os.sep}data{os.sep}gpuCrawlers')
    os.system(f"cd {finalDir} && scrapy crawl amazonRTX -O tmp{os.sep}amazonRTX.json")

# COOLMOD CRAWLER JSON
gpuCoolMod_data:list = []
try:
    for products in jsonData('coolModRTX.json'):
        if 'productPrice' not in products:
            products['productPrice'] = 'No stock'
        gpuCoolMod_data.append(GpuData(products['productName'] , products['productPrice'].replace('.', '').replace(',', '.'), products['productDate']))
except OSError:
    dirName:str = os.path.dirname(os.path.abspath(__file__).replace(f"{os.sep}model", ""))
    finalDir:str = os.path.join(f'{dirName}{os.sep}data{os.sep}gpuCrawlers')
    os.system(f"cd {finalDir} && scrapy crawl coolModRTX -O tmp{os.sep}coolModRTX.json")


def dbCommit():
    dataBase.session.add_all(gpuAmazon_data)
    dataBase.session.add_all(gpuCoolMod_data)
    dataBase.session.commit()

if __name__ == '__main__':
    try:
        dataBase.Base.metadata.create_all(dataBase.engine)
        dbCommit()
    except sqlalchemy.exc.OperationalError:
        print('Connection Timed Out')

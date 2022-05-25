import json
import os
from scrapy import cmdline

def urlExctractor():
    dirName:str = os.path.dirname(os.path.abspath(__file__).replace(f"{os.sep}gpuCrawlers", ""))
    fileName:str = os.path.join(dirName, f'gpuCrawlers{os.sep}tmp{os.sep}coolModLinks.json')
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)

        dataFinal:list = []

        for links in data:
            dataFinal.append(f'https://www.coolmod.com{links["url"][0]}')

        return dataFinal
    except OSError:
        print("coolModLinks.json not found --Initializing")
        cmdline.execute("scrapy crawl coolModLinks -O coolModLinks.json".split())
    except json.decoder.JSONDecodeError:
        print("coolModLinks.json not found --Initializing")
        cmdline.execute("scrapy crawl coolModLinks -O coolModLinks.json".split())
import os
import sys
dirName:str = os.path.dirname(os.path.abspath(__file__).replace(f"{os.sep}view", ""))
finalDir:str = os.path.join(dirName, 'model')
sys.path.append(finalDir)
import sqlalchemy
import dataBase
import re

#USED FOR MULTISELECT ON STREAMLIT IMPORTANT
def listToString(stringList,delimitor):
    stringElements = ""
    for element in stringList:
        stringElements += (element + delimitor)
    return stringElements

def getAllGpuData():
    sqlStatement = sqlalchemy.text("SELECT gpu_name, gpu_price, gpu_date FROM gpu_data ORDER BY gpu_name")
    sqlStatementExecute = dataBase.session.execute(sqlStatement)
    gpuData:list = sqlStatementExecute.fetchall()
    return gpuData

def getNameGpuData():
    sqlStatement = sqlalchemy.text("SELECT gpu_name FROM gpu_data ORDER BY gpu_name")
    sqlStatementExecute = dataBase.session.execute(sqlStatement)
    gpuData:list = sqlStatementExecute.fetchall()
    return gpuData

def getGpuBrand(gpuBrand):
    sqlStatement = sqlalchemy.text(f"SELECT * FROM gpu_data WHERE gpu_name REGEXP '{gpuBrand}' ORDER BY gpu_name")
    sqlStatementExecute = dataBase.session.execute(sqlStatement)
    gpuName:list = sqlStatementExecute.fetchall()
    return gpuName






    
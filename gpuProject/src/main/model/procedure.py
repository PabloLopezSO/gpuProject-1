import os
import sqlalchemy
from model import dataBase
import pandas as pd
dirName:str = os.path.dirname(os.path.abspath(__file__))
finalDir:str = os.path.join(dirName, f'data{os.sep}gpuCrawlers{os.sep}tmp')
viewDir:str = os.path.join(dirName, 'view').replace('model', '')

def dumpDataToCsv():
    sqlStatement = sqlalchemy.text("SELECT gpu_name, gpu_price, gpu_date FROM gpu_data ORDER BY gpu_name")
    sqlStatementExecute = dataBase.session.execute(sqlStatement)
    gpuData:list = sqlStatementExecute.fetchall()
    df = pd.DataFrame(gpuData)
    return df.to_csv(f'{viewDir}{os.sep}modelProphet{os.sep}gpuData.csv', index=False)

def deleteNoRtx3000():
    sqlStatement = sqlalchemy.text("DELETE FROM gpu_data WHERE gpu_name NOT REGEXP '3050|3060|3070|3080|3090'")
    dataBase.session.execute(sqlStatement)
    return dataBase.session.commit()

def deleteNoStock():
    sqlStatement = sqlalchemy.text("DELETE FROM gpu_data WHERE gpu_price LIKE 'No Stock'")
    dataBase.session.execute(sqlStatement)
    return dataBase.session.commit()

def deleteMisc():
    sqlStatement = sqlalchemy.text("DELETE FROM gpu_data WHERE gpu_name REGEXP 'Riser|Cable|Inno3D|KFA2|Gainward'")
    dataBase.session.execute(sqlStatement)
    return dataBase.session.commit()

def deleteMinusChar():
    sqlStatement = sqlalchemy.text("update gpu_data set gpu_name = reverse(concat(left(reverse(gpu_name),instr(reverse(gpu_name),reverse(''))-2),substr(reverse(gpu_name),instr(reverse(gpu_name),reverse('-'))+length('-'))))")
    dataBase.session.execute(sqlStatement)
    return dataBase.session.commit()

def updateMisc():
    sqlStatement = sqlalchemy.text('update gpu_data set gpu_name = "EVGA 08G-P5-3755 3070 Ti" where gpu_name = "EVGA 08G-P5-3755"')
    dataBase.session.execute(sqlStatement)
    return dataBase.session.commit()

def deleteComma():
    sqlStatement = sqlalchemy.text("update gpu_data set gpu_name = SUBSTRING_INDEX(gpu_name, ',', 1)")
    dataBase.session.execute(sqlStatement)
    return dataBase.session.commit()

def deleteParenthesis():
    sqlStatement = sqlalchemy.text("update gpu_data set gpu_name = SUBSTRING_INDEX(gpu_name, '(', 1)")
    dataBase.session.execute(sqlStatement)
    return dataBase.session.commit()

def dumpDataToCsv():
    sqlStatement = sqlalchemy.text("SELECT gpu_name, gpu_price, gpu_date FROM gpu_data ORDER BY gpu_name")
    sqlStatementExecute = dataBase.session.execute(sqlStatement)
    df = pd.DataFrame(sqlStatementExecute)
    df.to_csv(f'{viewDir}{os.sep}modelProphet{os.sep}gpuData.csv', index=False)


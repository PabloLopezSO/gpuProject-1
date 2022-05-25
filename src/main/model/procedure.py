import sqlalchemy
from model import dataBase

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



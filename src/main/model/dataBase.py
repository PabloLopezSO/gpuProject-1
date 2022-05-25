import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#engine = sqlalchemy.create_engine("mysql+pymysql://root:luispablo52@192.168.1.24:33060/gpuData?charset=utf8mb4")
#engine = sqlalchemy.create_engine("mysql+pymysql://root:luispablo52@192.168.1.13:33060/gpuData?charset=utf8mb4")
engine = sqlalchemy.create_engine("mysql+pymysql://pablo:Luispablo52@pgpu-database.cihoiu4bnw7c.eu-west-2.rds.amazonaws.com:3306/gpuProject?charset=utf8mb4")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

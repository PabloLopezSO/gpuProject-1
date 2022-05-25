import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = sqlalchemy.create_engine("superSecret")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

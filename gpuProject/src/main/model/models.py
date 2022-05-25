import dataBase

from sqlalchemy import Column, Integer, String

class GpuData(dataBase.Base):
    __tablename__ = 'gpu_data'
    id_gpu = Column(Integer, primary_key=True)
    gpu_name = Column(String, nullable=True)
    gpu_price = Column(String, nullable=True)
    gpu_date = Column(String, nullable=True)

    def __init__ (self, gpuName, gpuPrice, gpuDate):
        self.gpu_name = gpuName
        self.gpu_price = gpuPrice
        self.gpu_date = gpuDate
    
    def __repr__(self):
        return f'Product({self.gpu_name},{self.gpu_price},{self.gpu_date})'

    def __str__(self):
        return self.gpu_name
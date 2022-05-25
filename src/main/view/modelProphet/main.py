import os
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly as pl
#import yfinance as yf
from pandas import read_csv
import streamlit as st

dirName:str = os.path.dirname(__file__)
finalDir:str = os.path.join(dirName, f'modelProphet{os.sep}gpuData.csv')
dbDir:str = os.path.join(dirName, 'model')
viewDir:str = os.path.join(dirName, 'view')
sleepDeleteTempFiles = 5


def gpuForecastingModel():

    dataPath:str = f'{dirName}{os.sep}historicalData.csv'

    df:pd = read_csv(dataPath, header=0)
    df.gpu_date = pd.to_datetime(df.gpu_date)
    df:pd = df.resample('M', on='gpu_date').mean()
    df:pd = df.dropna()

    df['ds'] = df.index
    df['y']= df.gpu_price
    model = Prophet()
    model.fit(df)

    st.subheader("Prediction Time")
    slideValue = st.slider("Slider", 1, 3)
    st.write("Years:", slideValue)
    future = model.make_future_dataframe(periods=slideValue * 365)
    forecast = model.predict(future)
    fig = plot_plotly(model, forecast)
    st.plotly_chart(fig)

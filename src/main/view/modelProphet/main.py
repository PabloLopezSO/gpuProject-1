import os
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
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

    sliderColumn, blankColumn = st.columns(2)

    with sliderColumn:
        st.subheader("Prediction Time")
        st.write("✨ Here you can choose from the slider itself, the years you want to predict in the future ✨")
        slideValue = st.slider("Slider", 1, 3)
        st.write("Years:", slideValue)
        future = model.make_future_dataframe(periods=slideValue * 365)
        forecast = model.predict(future)

    
    with blankColumn:
        st.subheader("About the prediction")
        dropDownData = st.expander("✨ Click here if you want to know how the prediction its going to be ✨")
        with dropDownData:
            st.write("Well I don't think I have to clarify this, but if you read the title of the project.. You'll see the phrase RTX SERIES 3000 Prediction, Well obviously the prediction is not going to be about each of the graphics card, indeed , it will be about all the graphics cards.")


    fig = plot_plotly(model, forecast)
    fig.update_layout(
        xaxis_title="DATE",
        yaxis_title="3000 SERIES PRICING $"
    )
    fig.update_traces(
        hovertemplate="<br>".join([
            "Price %{y}$"
    ])
    )   

    st.subheader("Here you can see the forecasting model")
    st.write("As you can see, you have two axis date and price. Its operation its pretty simple you have a plot where you can hover with your mouse, so you can see the predicted price, trace one, trace three and actual price.")
    st.write("There you can just play and see the difference on pricing")

    st.plotly_chart(fig)

    st.subheader("Forecasting Model Trained Data")
    st.write("Here you can see the data that We are using to show the predicted price. How prophet manage the cleaned data We gave to him")
    st.write("In a nutshell this data is basically the trained data")
    st.dataframe(forecast)

    


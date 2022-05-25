import os
from turtle import title
from pymysql import OperationalError
import pymysql
import streamlit as st
import pandas as pd
import numpy as np
import getData
import altair as alt
import plotly.figure_factory as ff
import numpy as np
import scipy
from modelProphet import main as gpuModelForecast
from streamlit_option_menu import option_menu




#------------------#
#--    INTRO     --#
#------------------#

st.set_page_config(
     page_title="GpuProject",
     page_icon="✨",
     layout="wide",
     initial_sidebar_state="collapsed"
 )

def homeIntroProject():
    st.title('Welcome to the Gpu Price Prediction Project')
    st.markdown("Hello there! Have you ever spent your time thinking about.. When the graphics cards prices will go down or up? (ง︡'-'︠)ง Well you are in the right place here is a linear regression model to help you find those numbers !")
    st.markdown("If you are interested in how this app was developed check out my GitHub [HattoriHamzo](https://github.com)")
    st.text('')
    st.text('')
    dropDownData = st.expander('✨ You can click here to see the raw data ✨')
    with dropDownData:
        df = pd.DataFrame(getData.getAllGpuData())
        mapping = {df.columns[0]:'Graphic Cards', df.columns[1]: 'Price', df.columns[2]:'Scrape Date'}
        df = df.rename(columns=mapping)
        st.dataframe(data=df.reset_index(drop=True))
    st.text('')



    regeressionModelImageColumn, gpuImageColumn, blankColumn = st.columns(3)

    with regeressionModelImageColumn:
        st.header("Linear Regression Model")
        st.image("https://marvel-b1-cdn.bc0a.com/f00000000206209/www.imsl.com/sites/default/files/image/2021-06/IMSL%20What%20is%20Regression%20Model%20Blog%20Feature.png")
    
    with gpuImageColumn:
        st.header("What is a Linear Regression Model? 👇")
        dropDownData = st.expander('✨ You can click here if you want to know what a Linear Regression Model is ✨')
        with dropDownData:
            st.write('Linear regression is a basic and commonly used type of predictive analysis.  The overall idea of regression is to examine two things: [1] does a set of predictor variables do a good job in predicting an outcome (dependent) variable?  [2] Which variables in particular are significant predictors of the outcome variable, and in what way do they–indicated by the magnitude and sign of the beta estimates–impact the outcome variable?  These regression estimates are used to explain the relationship between one dependent variable and one or more independent variables.')


    regeressionModelImageColumn, gpuImageColumn, blankColumn = st.columns(3)

    with regeressionModelImageColumn:
        st.header("Graphic Cards")
        st.image("https://i.postimg.cc/DwmnmDb6/project-Photo.jpg")
    
    with gpuImageColumn:
        st.header("Graphics Cards Used? 👇")
        dropDownData = st.expander('✨ You can click here if you want to know what graphics cards I used ✨')
        with dropDownData:
            st.write('I used all the RTX 3000 series, from the 3050 to the 3090 passing through the Ti ones, scraped  from different sites like Amazon for example.')
            df = pd.DataFrame(getData.getNameGpuData())
            mapping = {df.columns[0]:'Graphic Cards'}
            df = df.rename(columns=mapping)
            st.dataframe(data=df.reset_index(drop=True))
        


#------------------------------#
#-- PRICE PREDICTION PROJECT --#
#------------------------------#

# Header
def headerFrame():
    st.title("GPU PRICE PREDICTION PROJECT")
    st.header("Data about RTX 3000 SERIES")
    st.write("In this table you can see the prices of the RTX series 3000 from Nvidia and his different brands")
    df = pd.DataFrame(
        getData.getAllGpuData())

    st.dataframe(df)
    st.subheader("Brand Selection")
    st.write("✨ Here you can choose whatever brand you want to see on the graphic below ✨")

# MultiSelect
def multiSelectBased():
    
    gpuBrand = st.multiselect(
    "Select a Brand",
    ("ASUS", "EVGA", "GIGABYTE", "MSI", "MAXSUN", "PNY", "ZOTAC"),
    default='ASUS'
    )
    st.write("Selected:", len(gpuBrand), "Brand")

    #DataFrame
    try:
        df = pd.DataFrame(
        getData.getGpuBrand(getData.listToString(gpuBrand,'|')[:-1]))

        #Chart
        chart = alt.Chart(df.reset_index()).mark_bar().encode(
        x='gpu_name:O',  # specify ordinal data
        y='gpu_price:Q',  # specify quantitative data
        color='gpu_name:N',
        tooltip=[alt.Tooltip('gpu_price:Q', title='GPU PRICE')]
        ).properties(title="Predicted Price", height = 500)
        chart.encoding.x.title = 'GPU NAME'
        chart.encoding.y.title = 'GPU PRICE'
        chart.encoding.color.title = 'GPU BRAND'
        st.altair_chart(chart, use_container_width=True)
    except Exception:
        st.write("Please Select a brand")

def foreCastModel():
    gpuModelForecast.gpuForecastingModel()


#------------------------------#
#----------- MENU ------------ #
#------------------------------#

def sideBarMenu():  
    with st.sidebar:
        selected = option_menu(
            menu_title="Gpu Prediction",
            options=["Home", "Price Prediction Project"],
            icons=["house", "book"],
            menu_icon="cast",
            default_index=0
        )

    if selected == "Home":
        homeIntroProject()
    if selected == "Price Prediction Project":
        st.title(f"WELCOME TO THE PRICE PREDICTION PROJECT")
        headerFrame()
        multiSelectBased()
        foreCastModel()

        
if __name__ == '__main__':
    
    sideBarMenu()

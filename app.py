import streamlit as st
import pandas as pd
import requests
import datetime
from bokeh.plotting import figure
import os

key = os.environ.get('API_Key')

ticker = st.text_input('Please enter your ticker symbol here') 
years = ['Select','2021','2020','2019','2018','2017','2016','2015']
months = ['Select','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug', 'Sep','Oct','Nov','Dec']
YYYY = st.selectbox('Select the year', years)
MONTH = st.selectbox('Select Month', months)
monthdict = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',
              'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
ticker_error = False
date_error = False
if ticker and YYYY!='Select' and MONTH!='Select':
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize={}&apikey={}'.format(ticker, 'full', key)
    response = requests.get(url)
    json_data = response.json()
    if 'Error Message' in list(json_data.keys()):
        ticker_error = True
    else:
        df = pd.DataFrame(json_data['Time Series (Daily)'])
        MM = monthdict[MONTH]
        dates = []
        close_price = []
        for date in df.columns.tolist():
            if (YYYY+'-'+MM) in date:
                dates.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
                close_price.append(float(df.loc['5. adjusted close'][date]))
        if len(dates)==0:
            date_error = True

if ticker and YYYY!='Select' and MONTH!='Select':
    if ticker_error:
        'Sorry but we have no data for',ticker,'. Please choose another ticker symbol.'    
    elif date_error:
        'Sorry but there is no data for ',MONTH,' ',YYYY,' for',ticker,'. Please try a different date range.'    
    else:
        p = figure(x_axis_type="datetime", x_axis_label="Date", 
        y_axis_label="Stock closing price ($)",plot_width=800)
        p.title.text = ticker+' Adjusted Closing Price'
        p.title.align = 'center'
        p.title.text_font_size = "25px"
        p.line(x=dates, y=close_price)
        st.bokeh_chart(p, use_container_width=True)
import requests
import json
import bokeh
import pandas as pd
import datetime
from bokeh.plotting import figure, output_file, show

key = 'ELUKLXU63BR4D6V5'
ticker = 'AAPL'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize={}&apikey={}'.format(ticker, 'full', key)

response = requests.get(url)
json_data = response.json()
df = pd.DataFrame(json_data['Time Series (Daily)'])

YYYY = '2021'
MM = '05'
dates = []
close_price = []
for date in df.columns.tolist():
    if (YYYY+'-'+MM) in date:
        dates.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
        close_price.append(float(df.loc['5. adjusted close'][date]))

p = figure(x_axis_type="datetime", x_axis_label="Date", 
           y_axis_label="Stock price ($)",plot_width=800)
p.title.text = ticker+' Adjusted Price'
p.title.align = 'center'
p.title.text_font_size = "25px"
p.line(x=dates, y=close_price)

show(p)
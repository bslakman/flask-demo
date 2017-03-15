
# coding: utf-8

# In[135]:

import requests
import pandas as pd
import datetime

from bokeh.charts import TimeSeries, show
from bokeh.io import output_notebook
from bokeh.models import HoverTool


# In[141]:

def plot(ticker, list_of_metrics=['close']):
    with open('api.txt', 'r') as f: 
        api_key=f.read()
    
    base = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json'
    today = datetime.date.today()
    date_gte = "".join(str(today - datetime.timedelta(days=30)).split('-'))
    
    response = requests.get(base, params = {'api_key': api_key, 'ticker': ticker, 'date.gte': date_gte})
    table_info = response.json()['datatable']

    df = pd.DataFrame(data = table_info['data'], 
                  columns = [col['name'] for col in table_info['columns']], )
                  #dtype=[col['type'] for col in table_info['columns']])
        
    hover = HoverTool(tooltips=[('Date', '$x')])
    p = TimeSeries(data = df, x = 'date', y = list_of_metrics, tools=[hover], 
               plot_width = 600, plot_height=400, title=ticker)
    show(p)


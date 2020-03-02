import pandas as pd
from datetime import date

def get_latest():
    base = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
    today = date.today()
    today = today.strftime("%m-%d-%Y")
    daily_url = base + today + '.csv'   
    return pd.read_csv(daily_url, index_col=0)

def get_past_data(date_=None):
    base = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
    date_url = str(date_) + '.csv'
    return pd.read_csv(daily_url, index_col=0)

def get_time_series(type_='confirmed'):
    raw_base = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-'
    type_ = type_.capitalize() 
    url = raw_base + type_ + '.csv'
    return pd.read_csv(url, index_col=0)
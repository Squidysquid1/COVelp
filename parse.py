import pandas as pd
import sqlite3
import datetime
import os

def check_covid_data():
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
    df = pd.read_csv(url, error_bad_lines=False)
    info = df[['Admin2', 'Province_State'] + list(df.columns[11:])]

    conn = sqlite3.connect('app.db')
    #conn.execute('DROP TABLE covid_data IF EXISTS')
    info.to_sql('covid_data', conn)
    date_now = datetime.date.today()
    date_recent = datetime.datetime.strptime(df.columns[-1], '%m/%d/%y').date()

    if date_now - datetime.timedelta(days=1) > date_recent:
        df = pd.read_csv(url, error_bad_lines=False)
        info = df[['Admin2', 'Province_State'] + list(df.columns[11:])]

        conn = sqlite3.connect('app.db')
        info.to_sql('covid_data', conn)

check_covid_data()

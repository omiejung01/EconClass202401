import numpy as np
import pandas as pd
from datetime import date

from pandas import json_normalize
import requests

def case11():
    path = 'C:\\data_analysis\\data2\\02-customer_missing.csv'
    df = pd.read_csv(path)
    #print(df)

    df2 = df.replace('-','No data')
    df3 = df2.fillna('No data')
    df4 = df3.replace('--','No data')
    df5 = df4.replace(' ','No data')
    print(df5)

def case12():
    path = 'C:\\data_analysis\\data2\\02-customer_missing.csv'
    df = pd.read_csv(path)

    #'name' column only
    df['name'] = df['name'].fillna('No data')
    df['name'] = df['name'].replace({
        '-': 'No data',
        '--': 'No data',
        ' ': 'No data'
    })
    print(df)

def case13():
    print(calculateAge(date(1997, 2, 3)), "years")

    path = 'C:\\data_analysis\\data2\\02-customer_missing.csv'
    df = pd.read_csv(path)
    #print(df)

    #df['duration'] = calculateAge(date(1997, 2, 3))
    for x in df.index:
        jdate = df.at[x, 'date_join']
        y = int(jdate[0:4])
        m = int(jdate[5:7])
        d = int(jdate[8:10])
        duration_value = calculateAge(date(y, m, d))
        df.at[x, 'duration'] = duration_value
    print(df)


def calculateAge(birthDate):
    days_in_year = 365.2425
    age = int((date.today() - birthDate).days / days_in_year)
    return age

def case14():
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(BASE_URL + "/products")
    data = response.json()
    df = json_normalize(data)
    print(df[['id','title','category']])


if __name__ == '__main__':
    #case11()
    #case12()
    #case13()
    case14()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

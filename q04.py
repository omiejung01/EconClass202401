import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pandas import json_normalize
import requests



def q04():
    # Histogram
    #x = np.random.randn(1000)
    #bins = np.arange(-4, 4, 0.5)
    #plt.hist(x, edgecolor='white', linewidth=1.5, bins=bins)
    # plt.hist(x)
    #plt.show()

    BASE_URL = 'https://fakestoreapi.in/'
    response = requests.get(BASE_URL + "api/products")
    data = response.json()
    df = json_normalize(data)
    df2 = json_normalize(df.products[0])
    df3 = df2.query("price < 4000")

    print(df3[['price']])

    # output
    plt.figure(figsize=(10.4, 6.4))
    plt.hist(df3[['price']], edgecolor='white', linewidth=1.5)
    path = 'C:\\data\\output\\' + 'hist04.png'
    plt.savefig(path)



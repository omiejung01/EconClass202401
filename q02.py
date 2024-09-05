import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def q02():
    # path = 'C:\\data\\transactions2.csv'
    path = 'C:\\data\\transactions.csv'
    df = pd.read_csv(path)
    #filter only US
    df2 = df[df['shippingCountry'].notnull()]
    df3 = df2.query("cardType in ('VISA')")

    country_list = []
    for x in df3.index:
        country_list.append(df3.at[x, 'shippingCountry'])
    # Remove the duplication
    country_list2 = list(dict.fromkeys(country_list))

    amount_transactions_country = []
    for x in country_list2:
        df_country3 = df3[df3['shippingCountry'] == x]
        average_transactions = df_country3[['transactionAmountUSD']].to_numpy().mean()
        #print("Transactions in " + x + " is " + str(amount_transactions) + ".")
        amount_transactions_country.append(average_transactions)

    print(country_list2)
    print(amount_transactions_country)
    #print(df3[['shippingState']])
    #Bar chart

    #output file
    plt.figure(figsize=(6.4, 50.4))
    plt.barh(country_list2, amount_transactions_country)
    #plt.show()
    path = 'C:\\data\\output\\' + 'mybar02.png'
    plt.savefig(path)


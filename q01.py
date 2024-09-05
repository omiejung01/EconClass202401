import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def q01():
    # path = 'C:\\data\\transactions2.csv'
    path = 'C:\\data\\transactions.csv'
    df = pd.read_csv(path)
    #filter only US
    df2 = df[df['shippingCountry'].notnull()]
    df3 = df2.query("shippingCountry in ('US')")
    #print(df3.head())
    #df3['shippingState'] = df3['shippingState'].fillna('No data')
    df3['shippingState'] = df3['shippingState'].fillna('N/A')

    # Change states to uppercase
    df3['shippingState'] = df3['shippingState'].str.upper()


    state_list = []
    for x in df3.index:
        state_list.append(df3.at[x, 'shippingState'])
    # Remove the duplication
    state_list2 = list(dict.fromkeys(state_list))
    #print(state_list2)
    num_transactions_state = []
    for x in state_list2:
        df_state3 = df3[df3['shippingState'] == x]
        num_transactions = len(df_state3)
        #print("Transactions in " + x + " is " + str(num_transactions) + ".")
        num_transactions_state.append(num_transactions)

    print(state_list2)
    print(num_transactions_state)
    #print(df3[['shippingState']])
    #Bar chart

    #output file
    plt.figure(figsize=(20.4, 6.4))
    plt.bar(state_list2, num_transactions_state)
    #plt.show()
    path = 'C:\\data\\output\\' + 'mybar01.png'
    plt.savefig(path)


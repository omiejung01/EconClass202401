import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def q03():
    # path = 'C:\\data\\transactions2.csv'
    path = 'C:\\data\\transactions.csv'
    df = pd.read_csv(path)
    #filter only US
    df2 = df[df['shippingCountry'].notnull()]
    df3 = df2[df2['cardType'].notnull()]

    cardtype_list = []
    for x in df3.index:
        cardtype_list.append(df3.at[x, 'cardType'])
    # Remove the duplication
    cardtype_list2 = list(dict.fromkeys(cardtype_list))

    amount_transactions_cardtype = []
    for x in cardtype_list2:
        df_country3 = df3[df3['cardType'] == x]
        total_amount_transactions = df_country3[['transactionAmountUSD']].to_numpy().sum()
        #print("Transactions in " + x + " is " + str(amount_transactions) + ".")
        amount_transactions_cardtype.append(float(total_amount_transactions))

    print(cardtype_list2)
    print(amount_transactions_cardtype)
    #print(df3[['shippingState']])
    #Bar chart

    #output file
    plt.figure(figsize=(10.4, 6.4))
    #plt.bar(cardtype_list2, amount_transactions_cardtype)

    bar_labels = ['yellow', 'blue', 'green', 'red', 'orange']
    bar_colors = ['yellow', 'blue', 'green', 'red', 'orange']

    fig, ax = plt.subplots()
    bar_container = ax.bar(cardtype_list2, amount_transactions_cardtype, label=bar_labels, color=bar_colors)

    ax.set(ylabel='USD', title='Transaction amount by Card Type', ylim=(0, 400000000))
    ax.bar_label(bar_container, fmt='{:,.0f}')

    #plt.show()
    path = 'C:\\data\\output\\' + 'mybar03.png'
    plt.savefig(path)


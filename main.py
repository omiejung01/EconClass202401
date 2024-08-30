import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def workshop01():
    # path = 'C:\\data\\transactions2.csv'
    path = 'C:\\data\\transactions.csv'
    df = pd.read_csv(path)
    #filter only US
    df2 = df[df['shippingCountry'].notnull()]
    df3 = df2.query("shippingCountry in ('US')")
    #print(df3.head())
    df3['shippingState'] = df3['shippingState'].fillna('No data')

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
    plt.bar(state_list2, num_transactions_state)
    #plt.show()
    path = 'C:\\data\\output\\' + 'mychart.png'
    plt.savefig(path)

if __name__ == '__main__':
    workshop01()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

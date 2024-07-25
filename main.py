import numpy as np
import pandas as pd

def case01():
    mylist = [80, 76, 11.20, 45, 'Amos Bow, Aqua Simulacra', 2.0, 'Elergy for the End', 23.45,
              'A Thousand floating Dreams', 100.0, 56]
    mylist2 = []

    for x in mylist:
        #print(type(x))
        if not isinstance(x, str):
            mylist2.append(x)

    print("Average score is " + str(np.average(mylist2)))
    print('')


def case01_02():
    mylist = [80, 76, 11.20, 45, 'Amos Bow, Aqua Simulacra', 2.0, 'Elergy for the End', 23.45,
              'A Thousand floating Dreams', 100.0, 56]

    mylist2 = []

    for x in mylist:
        #print(type(x))
        if isinstance(x, str):
            mylist2.append(x)

    #print("Average score is " + str(np.average(mylist2)))
    print(mylist2)
    print('')


def case02():
    path = "C:\\Users\\omiem\\Downloads\\01-employee.csv"
    df = pd.read_csv(path)
    # print(df.head())
    print("Average cost is " + str(np.average(df.filter(items=['cost']))))

    df2 = df.filter(items=['cost'])
    # print(np.percentile(df2, 50))
    # print(np.percentile(df2, 25))

    df3 = df2.query("cost <= " + str(np.percentile(df2, 25)))
    print("Number of employee that has cost less than 25 percentile is " + str(len(df3)))

    df4 = df[['project']]
    project_list = []
    for x in df4.index:
        project_list.append(df4.at[x, 'project'])

    project_list2 = list(dict.fromkeys(project_list))

    for x in project_list2:
        #ProjectA
        #x = 'ProjectA'
        df5 = df[df['project'] == x]
        total_cost = df5[['cost']].to_numpy().sum()
        print("Total cost of " + x + " is " + str(total_cost) + ".")

    df6 = df[['project']]
    project_list3 = []
    for x in df6.index:
        project_list3.append(df6.at[x, 'project'])

    project_list4 = list(dict.fromkeys(project_list3))

    for x in project_list4:
        df7 = df[df['project'] == x]
        total_hours = df7[['hours_worked']].to_numpy().sum()
        print("Total hours of " + x + " is " + str(total_hours) + " hours.")

    for x in project_list4:
        df8 = df[df['project'] == x]
        workers = len(df8)
        print("Number of workers of " + x + " is " + str(workers) + ".")

    print('')

def case03():
    path = "C:\\Users\\omiem\\Downloads\\02-customer_missing.csv"
    df = pd.read_csv(path)

    #print(df)
    df2 = df[df['name'].notnull()] #filter null value
    df3 = df2.query("name not in ('-','--') ")
    df4 = df3.query("name.str.strip() not in ('') ")
    print(df4)
    print('')

def case04():
    path = "C:\\Users\\omiem\\Downloads\\05-transactions.csv"
    df = pd.read_csv(path)

    #print(df.columns)
    #print(df[['payment_type','transaction_category']])

    df2 = df.query("payment_type in ('credit_card')")
    #print (df2[['payment_type','account_balance']])

    avg_cc = df2[['transaction_amount']].to_numpy().mean()
    print("Average credit card spending is " + str(avg_cc) + ".")

    df3 = df[['transaction_category']]
    category_list = []
    for x in df3.index:
        category_list.append(df3.at[x, 'transaction_category'])

    category_list2 = list(dict.fromkeys(category_list))
    for x in category_list2:
        df4 = df[df['transaction_category'] == x]
        total = df4[['transaction_amount']].to_numpy().sum()
        print("Total amount of " + x + " category is " + str(total) + ".")

if __name__ == '__main__':
    case01()
    case01_02()
    case02()
    case03()
    case04()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

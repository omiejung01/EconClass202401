import numpy as np
import pandas as pd

def case01():
    mylist = [80, 76, 11.20, 45,
              'Amos Bow, Aqua Simulacra', 2.0,
              'Elergy for the End', 23.45, 'A Thousand floating Dreams', 100.0, 56]

    mylist2 = []
    for x in mylist:
        if not isinstance(x, str):
            mylist2.append(x)
    # to filter text element out

    print("Average score is " + str(np.average(mylist2)))
    print('')


def case01_02():
    mylist = [80, 76, 11.20, 45,
              'Amos Bow, Aqua Simulacra', 2.0,
              'Elergy for the End', 23.45, 'A Thousand floating Dreams', 100.0, 56]

    mylist2 = []
    for x in mylist:
        if isinstance(x, str):
            mylist2.append(x)
    # to filter text element out

    print(mylist2)
    print('')


def case02():
    path = "C:\\Users\\omiem\\Downloads\\01-employee.csv"
    df = pd.read_csv(path)

    #print(df.head())
    #df2 = df[['project', 'cost']]
    #print(df2)
    df2 = df[['cost']]
    print("Average cost is " + str(np.average(df2)))

    df3 = df[['project']]

    project_list = []
    for x in df3.index:
        # print(x)
        # print(df3.at[x, 'project'])
        project_list.append(df3.at[x, 'project'])

    # print(project_list)
    # Remove the duplication
    project_list2 = list(dict.fromkeys(project_list))

    for x in project_list2:
        # print(x)
        df_project = df[df['project'] == x]
        total = df_project[['cost']].to_numpy().sum()
        # print ("The total cost of " + str(x) + " is " + str(total) + ".")

    #print(project_list2) hours_worked
    #print(df.head())

    for x in project_list2:
        df_project2 = df[df['project'] == x]
        total_hours = df_project2[['hours_worked']].to_numpy().sum()
        #print(x)
        #print(total_hours)
        print ("The total working hours of " + x + " is " + str(total_hours) + " hours.")

    for x in project_list2:
        df_project3 = df[df['project'] == x]
        num_people = len(df_project3)
        #print(x)
        #print(num_people)
        print("The number of workers in " + x + " is " + str(num_people) + ".")

    #df2 is cost
    #print(np.percentile(df2, 50))
    #print(np.percentile(df2, 25))

    df4 = df2.query("cost < " + str(np.percentile(df2, 25)))
    #print(len(df4))
    print ("Number of employees that has cost less than 25 percentile is " + str(len(df4)) + ".")
    print('')

def case03():
    path = "C:\\Users\\omiem\\Downloads\\02-customer_missing.csv"
    df = pd.read_csv(path)

    #print(df)

    #filter null value
    df2 = df[df['name'].notnull()]
    df3 = df2.query("name not in ('-','--')")
    df4 = df3.query("name.str.strip() not in '' ")

    print(df4)
    print('')

def case04():
    path = "C:\\Users\\omiem\\Downloads\\05-transactions.csv"
    df = pd.read_csv(path)
    #print(df)
    #transaction_amount , payment_type
    df2 = df[df['payment_type'] == 'credit_card']
    #df2 = df.query("payment_type in ('credit_card')") #same thing
    avg_cc = df2[['transaction_amount']].to_numpy().mean()
    print("Average credit card spending is " + str(avg_cc) + ".")

    df3 = df[['transaction_category']]
    category_list = []
    for x in df3.index:
        category_list.append(df3.at[x,'transaction_category'])

    category_list2 = list(dict.fromkeys(category_list))
    #print(category_list2)

    for x in category_list2:
        df4 = df[df['transaction_category'] == x]
        total_amount = df4[['transaction_amount']].to_numpy().sum()
        #print(x)
        #print(total_amount)
        print("Total amount of " + x + " category is " + str(total_amount) + ".")



if __name__ == '__main__':
    case01() #Average
    case01_02() #Filter number element out
    case02()
    case03()
    case04()

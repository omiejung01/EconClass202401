import pandas as pd
import numpy as np

def ex02():
    path = "C:\\Users\\omiem\\Downloads\\01-employee.csv"
    df = pd.read_csv(path)

    #print(df.to_string())
    #print(df[['employee']])
    #print(df[['cost']])

    average_cost = np.mean(df[['cost']])
    print("Average cost is " + str(average_cost))


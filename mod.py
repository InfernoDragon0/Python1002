import pandas as pd 
import datetime
import sys

def getData():
    covid_df = pd.read_csv("covid19.csv")
    cv_dataset3 = covid_df[["Date","Daily Confirmed"]]
    cv_dataset3["Date"] = cv_dataset3.Date.str[3:]
    c = cv_dataset3.columns.difference(['Daily Confirmed']).tolist()
    df = cv_dataset3.groupby(c, as_index=False).sum()
    print(df)
    sys.stdout.flush()

getData()

import pandas as pd 
import datetime
import sys

def getSum():
    covid_df = pd.read_csv("covid19.csv")
    cv_dataset3 = covid_df[["Daily Confirmed"]]
    df = cv_dataset3.sum()
    #cv_dataset3["Date"] = cv_dataset3.Date.str[3:]
    #c = cv_dataset3.columns.difference(['Daily Confirmed']).tolist()
    #df = cv_dataset3.groupby(c, as_index=False).sum()
    print(df)
    sys.stdout.flush()

getSum()

def getactivecases():
    covid_df = pd.read_csv("covid19.csv")
    cv_getactivecases = covid_df[["Still Hospitalised", "In Isolation MOH report"]]
    sumofstillhospitalised = cv_getactivecases["Still Hospitalised"]
    sumofininsolation = cv_getactivecases["In Isolation MOH report"]
    totalactivecase = sumofstillhospitalised + sumofininsolation # need to remove null value before adding
    print(totalactivecase)

getactivecases()
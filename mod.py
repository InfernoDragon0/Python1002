import pandas as pd 
import datetime
import sys

def getSum():
    covid_df = pd.read_csv("covid19.csv")
    df = covid_df['Cumulative Confirmed'].iloc[[-1]]
    summationoftotaldailycases = int(df)
    return(summationoftotaldailycases)


def getrecovered():
    covid_df = pd.read_csv("covid19.csv")
    df = covid_df['Cumulative Discharged'].iloc[[-1]]
    recoverRate = (int(df)/getSum()*100)
    return(int(recoverRate))


def getactivecases():
    covid_df = pd.read_csv("covid19.csv")
    df = covid_df['Still Hospitalised'].iloc[[-1]]
    df1 = covid_df['In Isolation MOH report'].iloc[[-1]]
    activecase = int(df) + int(df1)
    return(activecase)


def getdailyrecoved(): 
    covid_df = pd.read_csv("covid19.csv")
    df = covid_df['Cumulative Discharged'].iloc[[-1]]
    return(int(df))




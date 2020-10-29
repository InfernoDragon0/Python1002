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
    cv_droprows = covid_df.drop(covid_df.index[ :148])
    cv_getactivecases = cv_droprows[["Still Hospitalised", "In Isolation MOH report"]]
    droppedcv_getactivecases= cv_getactivecases.dropna(axis=0)
    summationofstillhos = droppedcv_getactivecases["Still Hospitalised"].sum()
    summationIsolation = droppedcv_getactivecases["In Isolation MOH report"].sum()
    summationofactivecases = summationofstillhos + summationIsolation
    return(int(summationofactivecases))


def getdailyrecoved(): # since phase 2
    covid_df = pd.read_csv("covid19.csv")
    cv_droprows = covid_df.drop(covid_df.index[ :148])
    cv_getactivecases = cv_droprows[["Daily Discharged", "Daily Deaths"]]
    droppedcv_getactivecases= cv_getactivecases.dropna(axis=0)
    summationofdd = droppedcv_getactivecases["Daily Discharged"].sum()
    summationofddd = droppedcv_getactivecases["Daily Deaths"].sum()
    summationdailyrecovered = summationofdd + summationofddd
    return(int(summationdailyrecovered))





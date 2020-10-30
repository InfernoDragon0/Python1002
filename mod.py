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

def getrecoveredcases():
    covid_df = pd.read_csv("covid19.csv")
    df = covid_df['Cumulative Discharged'].iloc[[-1]] 
    return(int(df))

def getdeath():
    covid_df = pd.read_csv("covid19.csv")
    df = covid_df['Cumulative Deaths'].iloc[[-1]]
    return(int(df))

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

def getfigdesc():
    figure1desc = "This diagram shows the daily cases over a period of time. We can identify the trend of the virus such as a sharp increase, steady decrease or constant. With this, we can predict the future no. of daily cases, taking into the account that Singapore will still remain in Phase 2."
    return figure1desc

def getfig2desc():
    figuer2desc = "The daily active cases constitute those still hospitalised and in isolation. Having a greater number in isolation compared to those still hospitalised is a good sign as it shows that the majority of active cases are in a stable health state which is easier to recover."
    return figuer2desc

def getfig3desc():
    figure3desc = "Daily recovered vs daily active cases. If daily recovered is constantly more than daily cases, and the recovery rate is high, we can infer that Singapore might enter phase 3 soon as the number of active cases would remain in the safe zone."
    return figure3desc


def getall():
    arraysentece = [str(getfigdesc()), str(getfig2desc()), str(getfig3desc())]
    return(arraysentece)




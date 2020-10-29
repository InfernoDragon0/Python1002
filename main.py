import pandas as pd
import sys
import datetime
import mod

def test():
    try:
        covid_df = pd.read_csv("covid19.csv") 
        cv_dataset2 = covid_df[["Date","Daily Confirmed", "Cumulative Confirmed", "Daily Discharged", "Still Hospitalised", "In Isolation MOH report", "Total Completed Isolation MOH report"]] 
        cv_droprows = covid_df.drop(covid_df.index[ :148])

        cv_dataset3 = cv_droprows[["Date","Daily Confirmed"]]
        dfxxx = cv_dataset3.rename(columns={"Date": "x", "Daily Confirmed": "y"})
        dfT = dfxxx.T 
        output = dfT.to_json()

        cv_dataset3["DateN"] = pd.to_datetime(cv_dataset3.Date, format='%d-%b')
        dfxxx = cv_dataset3.rename(columns={"Date": "x", "Daily Confirmed": "y"})
        getrecoverRateinpercent = mod.getrecovered()
        ouputRecoverRatePercent = getrecoverRateinpercent

        getactivecases = mod.getactivecases()
        outputactivecases = getactivecases

        getrecoveredcases = mod.getdailyrecoved()
        outputrecoveredcases = getrecoveredcases
        #Loop for monthly sorting
        output4 = {}
        sumoutput4 = {} 
        for mth in range(6, 11):
            dftx = dfxxx[(dfxxx['DateN'].dt.month == mth)]
            tempout = dftx.T.to_json()
            output4[str(mth)] = tempout

            for index, row in dftx.iterrows():
                if str(mth) in sumoutput4:
                    sumoutput4[str(mth)] = sumoutput4[str(mth)] + int(row['y'])
                else:
                    sumoutput4[str(mth)] = int(row['y'])
        
        activecases_ds = cv_droprows[["Date","Still Hospitalised", "In Isolation MOH report"]]
        dfxx = activecases_ds.rename(columns={"Date": "x", "Still Hospitalised": "y", "In Isolation MOH report": "z"})
        dfA = dfxx.T
        output2 = dfA.to_json()
        
        activecases_ds["DateN"] = pd.to_datetime(activecases_ds.Date, format='%d-%b')
        dfxx = activecases_ds.rename(columns={"Date": "x", "Still Hospitalised": "y", "In Isolation MOH report": "z"})

        #Loop for monthly sorting
        output5 = {}
        sumoutput5 = {}
        for mth in range(6, 11):
            dftx = dfxx[(dfxx['DateN'].dt.month == mth)]
            tempout = dftx.T.to_json()
            output5[str(mth)] = tempout

            for index, row in dftx.iterrows():
                if str(mth) in sumoutput5:
                    sumoutput5[str(mth)] = sumoutput5[str(mth)] + int(row['y'])
                    sumoutput5[str(mth) + "0"] = sumoutput5[str(mth) + "0"] + int(row['z'])
                else:
                    sumoutput5[str(mth)] = int(row['y'])
                    sumoutput5[str(mth) + "0"] = int(row['z'])
        
        drecovered_ds = cv_droprows[["Date", "Daily Discharged"]] 
        dfx = drecovered_ds.rename(columns={"Date": "x", "Daily Discharged": "y"})
        dfB = dfx.T
        output3 = dfB.to_json()
        
        drecovered_ds["DateN"] = pd.to_datetime(drecovered_ds.Date, format='%d-%b')
        dfx = drecovered_ds.rename(columns={"Date": "x", "Daily Discharged": "y"})

        #Loop for monthly sorting
        output6 = {}
        sumoutput6 = {}
        for mth in range(6, 11):
            dftx = dfx[(dfxxx['DateN'].dt.month == mth)]
            tempout = dftx.T.to_json()
            output6[str(mth)] = tempout

            for index, row in dftx.iterrows():
                if str(mth) in sumoutput6:
                    sumoutput6[str(mth)] = sumoutput6[str(mth)] + int(row['y'])
                else:
                    sumoutput6[str(mth)] = int(row['y'])

        output7 = list(covid_df.columns)

        combinedOut = {
            "a": output, 
            "b": output2, 
            "c": output3, 
            "d":ouputRecoverRatePercent,
            "e":outputactivecases,
            "f": outputrecoveredcases,
            "sortmontha": output4, 
            "sortmonthb": output5, 
            "sortmonthc": output6, 
            "searchables": output7,
            "summontha": sumoutput4, 
            "summonthb": sumoutput5, 
            "summonthc": sumoutput6
            }

        print(combinedOut)

        sys.stdout.flush()
    except Exception as e:
        print("an erorr", e.with_traceback)
        sys.stdout.flush()


test()



    






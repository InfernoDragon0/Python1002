import pandas as pd
import sys


def test():
    try:
        covid_df = pd.read_csv("covid19.csv") #reads the csv into python pandas
        cv_dataset2 = cv_droprows[["Date","Daily Confirmed", "Cumulative Confirmed", "Daily Discharged", "Still Hospitalised", "In Isolation MOH report", "Total Completed Isolation MOH report"]] #use only these columns
        cv_droprows = covid_df.drop(covid_df.index[ :148]) #drop rows or [1,2,3,4] 
        #print(covid_df.head(10)) #debug printing first 10 lines
        #print(cv_dataset2.head(5))
        #print(cv_droprows.head(10))

        # Dataset for daily confirmed cases from 18 Jun 2020 onwards by using cv_droprows
        cv_dataset3 = cv_droprows[["Date","Daily Confirmed"]]
        dfT = cv_dataset3.T 
        output = dfT.to_json()
        print(output)

        # Dataset for active cases cases from 18 Jun 2020 onwards by using cv_droprows
        activecases_ds = cv_droprows[["Date","Still Hospitalised", "In Isolation MOH report"]]
        dfA = activecases_ds.T
        output2 = dfA.to_json()
        print(output2)

        # Dataset for daily recovered from 18 Jun 2020 onwards by using cv_droprows
        drecovered_ds = cv.droprows[["Date", "Daily Discharged"]] #Take daily discharged minus daily deaths = actual daily recovered without deaths
        dfB = drecovered_ds.T
        output3 = dfB.to_json()
        print(output3)










        

        sys.stdout.flush()
    except Exception as e:
        print(e.message)
        sys.stdout.flush()


test()



    






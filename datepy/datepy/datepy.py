import numpy as np 
import pandas as pd

def number_of_days(startdate, enddate):
    df = pd.DataFrame({'startdate':[startdate],'enddate':[enddate]})
    df['startdate'] = pd.to_datetime(df['startdate'])
    df['enddate'] = pd.to_datetime(df['enddate'])
    #getting each date from the time range
    dates = [pd.Series(pd.date_range(row[1].startdate, row[1].enddate))
         for row in df[['startdate', 'enddate']].iterrows()]
    deltas = [len(x) for x in dates]
    dates = pd.Series(pd.concat(dates).values, name='date')
    return len(dates)

def days_distribution(startdate, enddate):
    df = pd.DataFrame({'startdate':[startdate],'enddate':[enddate]})
    df['startdate'] = pd.to_datetime(df['startdate'])
    df['enddate'] = pd.to_datetime(df['enddate'])
    #getting each date from the time range
    dates = [pd.Series(pd.date_range(row[1].startdate, row[1].enddate))
         for row in df[['startdate', 'enddate']].iterrows()]
    deltas = [len(x) for x in dates]
    dates = pd.Series(pd.concat(dates).values, name='date')
    #duplicating the dataframe for each date
    df2 = pd.DataFrame(np.repeat(df.values, deltas, axis=0), columns=df.columns)
    df2 = pd.concat([dates, df2], axis=1)
    df2['day_of_week'] = df2['date'].dt.weekday_name
    return dict(df2.day_of_week.value_counts())
    
    
#print(number_of_days('2015-01-01','2015-01-03')) 
#print(days_distribution('2018-12-15','2018-12-17'))
import pandas as pd

# author: Kaiwen Liu

'''
format the date so that can be used in python
'''
def format_date(list_d):
    # to get the values of year, month and day on the date list. 
    year=[int(x[-4:]) for x in list_d]
    month=[int(x[:2]) for x in list_d]
    day=[int(x[3:5]) for x in list_d]
    # format
    date=[pd.datetime(year[i],month[i],day[i]) for i in xrange(len(year))]
    return date
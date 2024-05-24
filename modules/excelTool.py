import pandas as pd 
import matplotlib.pyplot as plt
import os 
import matplotlib.dates as mdates

# currently just reads in excel data, looking to make it graph 
def mod_start():
    fName = input("Enter name of excel file\n\n>")
    graph(fName)
    return 

# currently can plot two axis graphs 
def graph(file_name):
    dp = []

    dataframe1 = pd.read_excel('../rsc/' + file_name + ".xlsx")

    h = dataframe1.to_dict()
    keys = [] 

    # scan for keys 
    for key in h:
        keys.append(key)

    for key in keys: 
        print(key, end ="    ")
    print()

    
    for key in keys:
        temp = [] 
        for i in range(len(h[keys[0]])):
            if key == 'date':
                temp.append(h[key][i].date())
            else:
                temp.append(h[key][i])
        dp.append(temp)

    print(dp)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.plot(dp[0], dp[1])
    plt.gcf().autofmt_xdate()
    plt.show()
    return 

mod_start()                                 
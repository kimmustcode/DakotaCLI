import pandas as pd 
import matplotlib.pyplot as plt
import os 
import matplotlib.dates as mdates

# currently can plot two axis graphs 
def show_graphs():
    
    dls = [
        'steps',
        'pushups',
        'wallsit',
        'water',
        'wr'
    ]
    fig, axs = plt.subplots(len(dls), layout="constrained")
    fig.suptitle('Dailies')
    cnt = 0
    for cat in dls:
        dataframe1 = pd.read_excel('./rsc/Dailies/' + cat + ".xlsx")
        dp = []


        h = dataframe1.to_dict()
        keys = [] 

        # scan for keys 
        for key in h:
            keys.append(key)
    
        for key in keys:
            temp = [] 
            for i in range(len(h[keys[0]])):
                    temp.append(h[key][i])
            dp.append(temp)

        axs[cnt].set_title(cat)
    
        axs[cnt].fill_between(dp[0], dp[1], alpha=0.3)
        axs[cnt].plot(dp[0], dp[1], "--")
        
        cnt += 1 
    plt.show()
    return 
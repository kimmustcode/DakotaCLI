import pandas as pd 
import matplotlib
import os 

# currently just reads in excel data, looking to make it graph 

def mod_start():
    fName = input("Enter name of excel file\n\n>")
    graph(fName)
    return 

def graph(file_name):                                                             
    dataframe1 = pd.read_excel('../rsc/' + file_name + ".xlsx")

    h = dataframe1.to_dict()
    keys = [] 

    # scan for keys 
    for key in h:
        keys.append(key)

    for key in keys: 
        print(key, end ="    ")
    print()

    for i in range(len(h[keys[0]])):
        for key in keys:
            if key == 'date':
                print(h[key][i].date(), end=" ")
            else:
                print(h[key][i], end=" ")
        print("")
    return 

mod_start()                                 
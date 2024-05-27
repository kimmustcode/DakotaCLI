import os
import pandas
from openpyxl import load_workbook 
from modules import excelTool as et

# TODO - Make sure that you cant input twice on same day 

def mod_start():
    os.system('cls')
    userin = input("Stat Tracker\n--daily\n--show\n\n>")
    if userin == 'daily':
        dailies()
    elif userin == 'show':
        et.show_graphs()
    return 


def dailies(): 
    os.system('cls')
    
    date = pandas.to_datetime('today').normalize()

    dls = [
        'steps',
        'pushups',
        'wallsit',
        'water',
        'wr'
    ]

    comments = [
        "\nHow many steps did you do today?\n>",
        "\nHow many Push-Ups did you do today?\n>",
        "\nLongest wall-sit today?\n>",
        "\nHow much water did you drink today?\n>",
        "\nWinrate today?\n>",
    ]
    cnt = 0 

    for task in dls:
        filename = "./rsc/Dailies/" + dls[cnt] + '.xlsx'
        workbook = load_workbook(filename)
        sheet = workbook['Sheet1']

        os.system('cls')
        print("Today's Date: " + date.strftime('%y/%m/%d'))

        amnt = input(comments[cnt])
        dSet = [date.strftime('%y/%m/%d'), amnt]
        sheet.append(dSet)
        workbook.save(filename)
        workbook.close()
        cnt += 1     

    return 
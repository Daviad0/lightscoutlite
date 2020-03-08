'''
SCOUT ADMIN
'''

import json
import csv
import math
import os
import requests
clear = lambda: os.system('clear')
from stringcolor import * 
tabRed1 = []
tabRed2 = []
tabRed3 = []
tabBlue1 = []
tabBlue2 = []
tabBlue3 = []
flagString = ""
helpMenu = True
def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False
matchNum = 1
def TryFile(fileName, station):
    try:
        open(fileName, "r")
        return 1
    except IOError:
        print("[ERROR] " + station + "'s Specified File Doesn't Exist!")
        return 0

if(TryFile("ScoutAdmin.csv", "Scouting Admin") == 1):
    print("Importing previous data...")
    with open("ScoutAdmin.csv") as thistoread:
        dataarray = []
        csv_reader = csv.reader(thistoread, delimiter=",")
        #READABLE FORMAT
        for csvconvert in csv_reader:
            dataarray.append(csvconvert)
        numberofmatches = 0
        for num in dataarray:
            numberofmatches += 1
        print("There are " + str(numberofmatches/6) + " matches loaded in from the previous session...")
        TOTAL_MATCH_NUM = round(numberofmatches/6)
        for x in range(TOTAL_MATCH_NUM):
            tabBlue1.append("U")
            tabBlue2.append("U")
            tabBlue3.append("U")
            tabRed1.append("U")
            tabRed2.append("U")
            tabRed3.append("U")
        loadIndex = 0
        for tabletFlag in dataarray:
            if(dataarray[loadIndex][0].lower() == "blue1"):
                tabBlue1[int(dataarray[loadIndex][1])-1] = (str(dataarray[loadIndex][2].upper()))
            elif(dataarray[loadIndex][0].lower() == "blue2"):
                tabBlue2[int(dataarray[loadIndex][1])-1] = (str(dataarray[loadIndex][2].upper()))
            elif(dataarray[loadIndex][0].lower() == "blue3"):
                tabBlue3[int(dataarray[loadIndex][1])-1] = (str(dataarray[loadIndex][2].upper()))
            elif(dataarray[loadIndex][0].lower() == "red1"):
                tabRed1[int(dataarray[loadIndex][1])-1] = (str(dataarray[loadIndex][2].upper()))
            elif(dataarray[loadIndex][0].lower() == "red2"):
                tabRed2[int(dataarray[loadIndex][1])-1] = (str(dataarray[loadIndex][2].upper()))
            elif(dataarray[loadIndex][0].lower() == "red3"):
                tabRed3[int(dataarray[loadIndex][1])-1] = (str(dataarray[loadIndex][2].upper()))
            loadIndex += 1
        print(tabBlue1)
        input()
        print("Done!")
else:
    TOTAL_MATCH_NUM = int(input("How many matches are there?\n> "))
    for x in range(TOTAL_MATCH_NUM):
        tabBlue1.append("U")
        tabBlue2.append("U")
        tabBlue3.append("U")
        tabRed1.append("U")
        tabRed2.append("U")
        tabRed3.append("U")
    print(tabBlue1)

    



while True:
    clear()
    userChoice = input("""    """ + cs("<N              Match " + str(matchNum) + "              P>", "magenta").bold() +"""

    """ + 
    cs("Red Team          ","white","red")  +    """   """ + cs("Blue Team         ","white","blue") + """
    """ +
    cs("R1    R2    R3    ", "white","red").underline() + """   """  + cs("B1    B2    B3    ","white","blue").underline() + """
    """
     + (cs("\u2713", "green").bold() if tabRed1[matchNum-1] == "U" else cs("\u2691", "orangered").bold()) + """     """  + (cs("\u2713", "green").bold() if tabRed2[matchNum-1] == "U" else cs("\u2691", "orangered").bold()) + """     """ + (cs("\u2713", "green").bold() if tabRed3[matchNum-1] == "U" else cs("\u2691", "orangered").bold()) + """        """ + (cs("\u2713", "green").bold() if tabBlue1[matchNum-1] == "U" else cs("\u2691", "orangered").bold()) + """     """ + (cs("\u2713", "green").bold() if tabBlue2[matchNum-1] == "U" else cs("\u2691", "orangered").bold()) + """     """ + (cs("\u2713", "green").bold() if tabBlue3[matchNum-1] == "U" else cs("\u2691", "orangered").bold())+ """
""" + 
    ("""
    *******************************
    "N" to go to next match (Match """ + str(matchNum+1) + """)
    "P" to go to previous match (Match """ + str(matchNum-1 if matchNum > 1 else 1) + """)
    "SET" to set current match
    "H" to disable help menu
    *******************************
    "E" to exit flag and save
    *******************************
    "F" to flag a tablet match
    "U" to mark a tablet as usable\n> """ if helpMenu == True else """
    [F] Flag
    [U] Unflag
    [H] Help Menu\n> """)).upper()
    if(userChoice == "SET"):
        matchNum = int(input("Which match would you like to switch to?\n> "))
        if(matchNum > len(tabBlue1)):
            matchNum = len(tabBlue1)
        elif(matchNum < 1):
            matchNum = 1
    elif(userChoice == "N"):
        if(matchNum < len(tabBlue1)):
            matchNum += 1
    elif(userChoice == "P"):
        if(matchNum > 1):
            matchNum -= 1
    elif(userChoice == "H"):
        if(helpMenu == True):
            helpMenu = False
        else:
            helpMenu = True
    elif(userChoice == "E"):
        open("ScoutAdmin.csv", "w").close()
        flaggedOutput = open("ScoutAdmin.csv", "w")
        flagString = ""
        index = 0
        print(tabBlue1[3])
        for x in range(len(tabBlue1)):
            flagString = flagString + "Blue1," + str(x+1) + "," + tabBlue1[x] + "\n"
            index += 1
        index = 0
        for x in range(len(tabBlue2)):
            flagString = flagString + "Blue2," + str(x+1) + "," + tabBlue2[x] + "\n"
            index += 1
        index = 0
        for x in range(len(tabBlue3)):
            flagString = flagString + "Blue3," + str(x+1) + "," + tabBlue3[x] + "\n"
            index += 1
        index = 0
        for x in range(len(tabRed1)):
            flagString = flagString + "Red1," + str(x+1) + "," + tabRed1[x] + "\n"
            index += 1
        index = 0
        for x in range(len(tabRed2)):
            flagString = flagString + "Red2," + str(x+1) + "," + tabRed2[x] + "\n"
            index += 1
        index = 0
        for x in range(len(tabRed3)):
            flagString = flagString + "Red3," + str(x+1) + "," + tabRed3[x] + "\n"
            index += 1
        flaggedOutput.write(flagString)
        flaggedOutput.close()
        break
    elif(userChoice == "DA"):
        print("Deteting Flags")
    elif(userChoice == "F"):
        tabletFlagged = input("What color tablet? (Red or Blue)\n> ")
        tabletNumber = int(input("What number tablet? (1, 2, or 3)\n> "))
        if(tabletFlagged.lower() == "blue"):
            if(tabletNumber == 1):
                tabBlue1[matchNum-1] = "F"
            if(tabletNumber == 2):
                tabBlue2[matchNum-1] = "F"
            if(tabletNumber == 3):
                tabBlue3[matchNum-1] = "F"
        elif(tabletFlagged.lower() == "red"):
            if(tabletNumber == 1):
                tabRed1[matchNum-1] = "F"
            if(tabletNumber == 2):
                tabRed2[matchNum-1] = "F"
            if(tabletNumber == 3):
                tabRed3[matchNum-1] = "F"
        else:
            print("Tablet color not valid!")
    elif(userChoice == "U"):
        tabletFlagged = input("What color tablet? (Red or Blue)\n> ")
        tabletNumber = int(input("What number tablet? (1, 2, or 3)\n> "))
        if(tabletFlagged.lower() == "blue"):
            if(tabletNumber == 1):
                tabBlue1[matchNum-1] = "U"
            if(tabletNumber == 2):
                tabBlue2[matchNum-1] = "U"
            if(tabletNumber == 3):
                tabBlue3[matchNum-1] = "U"
        elif(tabletFlagged.lower() == "red"):
            if(tabletNumber == 1):
                tabRed1[matchNum-1] = "U"
            if(tabletNumber == 2):
                tabRed2[matchNum-1] = "U"
            if(tabletNumber == 3):
                tabRed3[matchNum-1] = "U"
        else:
            print("Tablet color not valid!")
    open("ScoutAdmin.csv", "w").close()
    flaggedOutput = open("ScoutAdmin.csv", "w")
    indexauto = 0
    flagString = ""
    print(tabBlue1[3])
    for x in range(len(tabBlue1)):
        flagString = flagString + "Blue1," + str(x+1) + "," + tabBlue1[x] + "\n"
        indexauto += 1
    indexauto = 0
    for x in range(len(tabBlue2)):
        flagString = flagString + "Blue2," + str(x+1) + "," + tabBlue2[x] + "\n"
        indexauto += 1
    indexauto = 0
    for x in range(len(tabBlue3)):
        flagString = flagString + "Blue3," + str(x+1) + "," + tabBlue3[x] + "\n"
        indexauto += 1
    indexauto = 0
    for x in range(len(tabRed1)):
        flagString = flagString + "Red1," + str(x+1) + "," + tabRed1[x] + "\n"
        indexauto += 1
    indexauto = 0
    for x in range(len(tabRed2)):
        flagString = flagString + "Red2," + str(x+1) + "," + tabRed2[x] + "\n"
        indexauto += 1
    indexauto = 0
    for x in range(len(tabRed3)):
        flagString = flagString + "Red3," + str(x+1) + "," + tabRed3[x] + "\n"
        indexauto += 1
    flaggedOutput.write(flagString)
    flaggedOutput.close()
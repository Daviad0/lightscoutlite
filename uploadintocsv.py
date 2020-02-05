import csv
import requests
import json


#STATION TO TRACK
globalstation = "Red2"
headers = {
        'Authorization': 'Basic ZGF2aWFkbzo1OUJBQzZGMi1FMDVFLTQyREUtQkQ1MS1BNjI2MkE5MjkwOUI=',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
response = requests.get("https://frc-api.firstinspires.org/v2.0/2019/schedule/mishe?tournamentlevel=qual", headers=headers)
response = json.loads(response.text)
filewriterr1 = open("IRscout_Red1.csv", "w")
filewriterr2 = open("IRscout_Red2.csv", "w")
filewriterr3 = open("IRscout_Red3.csv", "w")
filewriterb1 = open("IRscout_Blue1.csv", "w")
filewriterb2 = open("IRscout_Blue2.csv", "w")
filewriterb3 = open("IRscout_Blue3.csv", "w")
red1string = ""
red2string = ""
red3string = ""
blue1string = ""
blue2string = ""
blue3string = ""
beforehand = ""
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
for jsonimport in response["Schedule"]:
    for item in jsonimport["teams"]:
        if(item["station"] == "Red1"):
            i1 += 1
            red1string = red1string + "Team Name,Test" + "\n"
            #TEAM NAME
            red1string = red1string + "Team Number,"
            red1string = red1string + str(item["teamNumber"]) + "\n"
            #TEAM NUMBER
            red1string = red1string + "Match Num," + "1\n"
            #MATCH NUMBER
            red1string = red1string + "Alliance,"
            red1string = red1string + str(item["station"]) + "\n"
            #ALLIANCE STATION
            red1string = red1string + "Scout Name,David Reeves\n"
            #SCOUT NAME
            red1string = red1string + "AUTON Initation Line,0\n"
            #AUTON INITATION LINE
            red1string = red1string + "Power Cell Lower,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #LOWER PORT
            red1string = red1string + "Power Cell Outer,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #OUTER PORT
            red1string = red1string + "Power Cell Inner,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #INNER PORT
            red1string = red1string + "Power Cell Miss,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #MISSED PORT
            red1string = red1string + "Control Panel Rotation,0\n"
            #CP ROTATION
            red1string = red1string + "Control Panel Position,0\n"
            #CP POSITION
            red1string = red1string + "Game Park,0\n"
            #ENDGAME PARK
            red1string = red1string + "Climb Attempt,0\n"
            #ENDGAME CLIMB ATTEMPT
            red1string = red1string + "Climb Success,0\n"
            #ENDGAME CLIMB SUCCESS
            red1string = red1string + "Balance Success,0\n"
            #ENDGAME BALANCE SUCCESS
            red1string = red1string + "#" + "\n"
            print("+ Red 1")
        if(item["station"] == "Red2"):
            i2 += 1
            red2string = red2string + "Team Name,Test" + "\n"
            #TEAM NAME
            red2string = red2string + "Team Number,"
            red2string = red2string + str(item["teamNumber"]) + "\n"
            #TEAM NUMBER
            red2string = red2string + "Match Num," + "1\n"
            #MATCH NUMBER
            red2string = red2string + "Alliance,"
            red2string = red2string + str(item["station"]) + "\n"
            #ALLIANCE STATION
            red2string = red2string + "Scout Name,David Reeves\n"
            #SCOUT NAME
            red2string = red2string + "AUTON Initation Line,0\n"
            #AUTON INITATION LINE
            red2string = red2string + "Power Cell Lower,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #LOWER PORT
            red2string = red2string + "Power Cell Outer,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #OUTER PORT
            red2string = red2string + "Power Cell Inner,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #INNER PORT
            red2string = red2string + "Power Cell Miss,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #MISSED PORT
            red2string = red2string + "Control Panel Rotation,0\n"
            #CP ROTATION
            red2string = red2string + "Control Panel Position,0\n"
            #CP POSITION
            red2string = red2string + "Game Park,0\n"
            #ENDGAME PARK
            red2string = red2string + "Climb Attempt,0\n"
            #ENDGAME CLIMB ATTEMPT
            red2string = red2string + "Climb Success,0\n"
            #ENDGAME CLIMB SUCCESS
            red2string = red2string + "Balance Success,0\n"
            #ENDGAME BALANCE SUCCESS
            red2string = red2string + "#" + "\n"
            print("+ Red 2")
        if(item["station"] == "Red3"):
            i3 += 1
            red3string = red3string + "Team Name,Test" + "\n"
            #TEAM NAME
            red3string = red3string + "Team Number,"
            red3string = red3string + str(item["teamNumber"]) + "\n"
            #TEAM NUMBER
            red3string = red3string + "Match Num," + "1\n"
            #MATCH NUMBER
            red3string = red3string + "Alliance,"
            red3string = red3string + str(item["station"]) + "\n"
            #ALLIANCE STATION
            red3string = red3string + "Scout Name,David Reeves\n"
            #SCOUT NAME
            red3string = red3string + "AUTON Initation Line,0\n"
            #AUTON INITATION LINE
            red3string = red3string + "Power Cell Lower,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #LOWER PORT
            red3string = red3string + "Power Cell Outer,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #OUTER PORT
            red3string = red3string + "Power Cell Inner,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #INNER PORT
            red3string = red3string + "Power Cell Miss,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #MISSED PORT
            red3string = red3string + "Control Panel Rotation,0\n"
            #CP ROTATION
            red3string = red3string + "Control Panel Position,0\n"
            #CP POSITION
            red3string = red3string + "Game Park,0\n"
            #ENDGAME PARK
            red3string = red3string + "Climb Attempt,0\n"
            #ENDGAME CLIMB ATTEMPT
            red3string = red3string + "Climb Success,0\n"
            #ENDGAME CLIMB SUCCESS
            red3string = red3string + "Balance Success,0\n"
            #ENDGAME BALANCE SUCCESS
            red3string = red3string + "#" + "\n"
            print("+ Red 3")
        if(item["station"] == "Blue1"):
            i4 += 1
            blue1string = blue1string + "Team Name,Test" + "\n"
            #TEAM NAME
            blue1string = blue1string + "Team Number,"
            blue1string = blue1string + str(item["teamNumber"]) + "\n"
            #TEAM NUMBER
            blue1string = blue1string + "Match Num," + "1\n"
            #MATCH NUMBER
            blue1string = blue1string + "Alliance,"
            blue1string = blue1string + str(item["station"]) + "\n"
            #ALLIANCE STATION
            blue1string = blue1string + "Scout Name,David Reeves\n"
            #SCOUT NAME
            blue1string = blue1string + "AUTON Initation Line,0\n"
            #AUTON INITATION LINE
            blue1string = blue1string + "Power Cell Lower,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #LOWER PORT
            blue1string = blue1string + "Power Cell Outer,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #OUTER PORT
            blue1string = blue1string + "Power Cell Inner,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #INNER PORT
            blue1string = blue1string + "Power Cell Miss,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #MISSED PORT
            blue1string = blue1string + "Control Panel Rotation,0\n"
            #CP ROTATION
            blue1string = blue1string + "Control Panel Position,0\n"
            #CP POSITION
            blue1string = blue1string + "Game Park,0\n"
            #ENDGAME PARK
            blue1string = blue1string + "Climb Attempt,0\n"
            #ENDGAME CLIMB ATTEMPT
            blue1string = blue1string + "Climb Success,0\n"
            #ENDGAME CLIMB SUCCESS
            blue1string = blue1string + "Balance Success,0\n"
            #ENDGAME BALANCE SUCCESS
            blue1string = blue1string + "#" + "\n"
            print("+ Blue 1")
        if(item["station"] == "Blue2"):
            i5 += 1
            blue2string = blue2string + "Team Name,Test" + "\n"
            #TEAM NAME
            blue2string = blue2string + "Team Number,"
            blue2string = blue2string + str(item["teamNumber"]) + "\n"
            #TEAM NUMBER
            blue2string = blue2string + "Match Num," + "1\n"
            #MATCH NUMBER
            blue2string = blue2string + "Alliance,"
            blue2string = blue2string + str(item["station"]) + "\n"
            #ALLIANCE STATION
            blue2string = blue2string + "Scout Name,David Reeves\n"
            #SCOUT NAME
            blue2string = blue2string + "AUTON Initation Line,0\n"
            #AUTON INITATION LINE
            blue2string = blue2string + "Power Cell Lower,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #LOWER PORT
            blue2string = blue2string + "Power Cell Outer,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #OUTER PORT
            blue2string = blue2string + "Power Cell Inner,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #INNER PORT
            blue2string = blue2string + "Power Cell Miss,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #MISSED PORT
            blue2string = blue2string + "Control Panel Rotation,0\n"
            #CP ROTATION
            blue2string = blue2string + "Control Panel Position,0\n"
            #CP POSITION
            blue2string = blue2string + "Game Park,0\n"
            #ENDGAME PARK
            blue2string = blue2string + "Climb Attempt,0\n"
            #ENDGAME CLIMB ATTEMPT
            blue2string = blue2string + "Climb Success,0\n"
            #ENDGAME CLIMB SUCCESS
            blue2string = blue2string + "Balance Success,0\n"
            #ENDGAME BALANCE SUCCESS
            blue2string = blue2string + "#" + "\n"
            print("+ Blue 2")
        if(item["station"] == "Blue3"):
            i6 += 1
            blue3string = blue3string + "Team Name,Test" + "\n"
            #TEAM NAME
            blue3string = blue3string + "Team Number,"
            blue3string = blue3string + str(item["teamNumber"]) + "\n"
            #TEAM NUMBER
            blue3string = blue3string + "Match Num," + "1\n"
            #MATCH NUMBER
            blue3string = blue3string + "Alliance,"
            blue3string = blue3string + str(item["station"]) + "\n"
            #ALLIANCE STATION
            blue3string = blue3string + "Scout Name,David Reeves\n"
            #SCOUT NAME
            blue3string = blue3string + "AUTON Initation Line,0\n"
            #AUTON INITATION LINE
            blue3string = blue3string + "Power Cell Lower,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #LOWER PORT
            blue3string = blue3string + "Power Cell Outer,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #OUTER PORT
            blue3string = blue3string + "Power Cell Inner,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #INNER PORT
            blue3string = blue3string + "Power Cell Miss,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            #MISSED PORT
            blue3string = blue3string + "Control Panel Rotation,0\n"
            #CP ROTATION
            blue3string = blue3string + "Control Panel Position,0\n"
            #CP POSITION
            blue3string = blue3string + "Game Park,0\n"
            #ENDGAME PARK
            blue3string = blue3string + "Climb Attempt,0\n"
            #ENDGAME CLIMB ATTEMPT
            blue3string = blue3string + "Climb Success,0\n"
            #ENDGAME CLIMB SUCCESS
            blue3string = blue3string + "Balance Success,0\n"
            #ENDGAME BALANCE SUCCESS
            blue3string = blue3string + "#" + "\n"
            print("+ Blue 3")
beforehand = "Number of matches," + str(i1) + "\n"
red1string = beforehand + red1string
beforehand = "Number of matches," + str(i2) + "\n"
red2string = beforehand + red2string
beforehand = "Number of matches," + str(i3) + "\n"
red3string = beforehand + red3string
beforehand = "Number of matches," + str(i4) + "\n"
blue1string = beforehand + blue1string
beforehand = "Number of matches," + str(i5) + "\n"
blue2string = beforehand + blue2string
beforehand = "Number of matches," + str(i6) + "\n"
blue3string = beforehand + blue3string
print(str((i1+i2+i3+i4+i5+i6) / 6) + ": all 6 stations divided by 6")
filewriterr1.write(red1string)
filewriterr2.write(red2string)
filewriterr3.write(red3string)
filewriterb1.write(blue1string)
filewriterb2.write(blue2string)
filewriterb3.write(blue3string)



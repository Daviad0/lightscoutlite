import csv
import requests
import json
import os
import time

clear = lambda: os.system('clear')
headers = {
        'Authorization': 'Basic ZGF2aWFkbzo1OUJBQzZGMi1FMDVFLTQyREUtQkQ1MS1BNjI2MkE5MjkwOUI=',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

eventCode = input("Event Code: ").upper()
teamNumber = int(input("Team Number: "))


currentevents = requests.get("https://frc-api.firstinspires.org/v2.0/2020/scores/" + eventCode + "/qual?teamNumber=" + str(teamNumber), headers=headers)
currentevents = json.loads(currentevents.text)
print(currentevents)
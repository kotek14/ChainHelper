#!/usr/bin/env python3

import requests
import os
import time

api_key = "PASTE YOUR API KEY HERE"
#api_key = os.environ['TORN']

# Takes nothing and returns a list of IDs
def readFromFile():
    users = []
    targetsHandle = open("targets.txt", "r")
    for targetLine in targetsHandle.readlines():
        if targetLine[0] == "#" or len(targetLine.split()) < 1:
            pass
        else:
            users.append(targetLine.split()[0])
    targetsHandle.close()
    return(users)

# Takes ID and returns:
# Name, ID, State, Last Action Timestamp, Current timestamp, time until the end of status.
def api_request(user):
    raw = requests.get("https://api.torn.com/user/" + str(user) + "?selections=basic,profile,timestamp&key=" + api_key)
    data = raw.json()
    return(data['name'], data['player_id'], data['status']['state'], data['last_action']['timestamp'], data['timestamp'] - data['last_action']['timestamp'], data['status']['until'] - data['timestamp'])

# Takes seconds and returns a string:
# X days Y hours Z minutes
# or Now if less than 1 minute
def present_time(seconds):
    if seconds < 60:
        return("Now")
    else:
        days = seconds // (24 * 3600)
        seconds = seconds % (24 * 3600) 
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if days:
            return(str(days) + " days " + str(hours) + " hours " + str(minutes) + " minutes")
        elif hours:
            return(str(hours) + " hours " + str(minutes) + " minutes")
        else:
            return(str(minutes) + " minutes")

while True:
    users = readFromFile()
    for user in users:
        data          = api_request(user)
        nameOfUser    = data[0]
        playerID      = data[1]
        playerStatus  = data[2]
        lastAction    = data[4]
        untilDone     = data[5]
        lastActionStr = present_time(data[4])
        untilDoneStr     = present_time(data[5])
        print("%s[%s] Status:%s for %s (Last action: %s ago)" % (nameOfUser, playerID, playerStatus, untilDoneStr, lastActionStr))
        if playerStatus == "Okay": # and lastAction > 3600 * 2:
            print("Found target! Opening browser...")
            #os.system("firefox https://www.torn.com/profiles.php?XID=" + str(playerID))
            attackLink = "https://www.torn.com/loader.php?sid=attack&user2ID=" + str(playerID)
            print("Attack link: " + attackLink)
            input("Press enter when you're done")
            print("Continuing...")
    input("End of the list. Press Enter to start over")

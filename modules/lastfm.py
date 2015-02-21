"""
function np
uses last.fm api to find what a user is currently listening to
uses json dict to find artist, album and track name
todo:
    add validation for username
    """
import requests
import json

def np(user):
    url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=%s&api_key=4a37d68f96770076a9aa3b59f830586c&format=json" % user
    userInfo = requests.get(url)
    userInfo = userInfo.text
    userInfo = json.loads(userInfo)
    try:
        artist = userInfo["recenttracks"]['track'][0]['artist']['#text']
        album = userInfo["recenttracks"]['track'][0]['album']['#text']
        track = userInfo["recenttracks"]['track'][0]['name']
        outt = user + " is now listening to " + track + " - " + artist + " on " + album
        outt = outt[:80]
    except KeyError:
        outt = "no user found"
    return outt

def compare(user1, user2):
    url = "http://ws.audioscrobbler.com/2.0/?method=tasteometer.compare&type1=user&type2=user&value1=%s&value2=%s&api_key=4a37d68f96770076a9aa3b59f830586c&format=json" % (user1, user2)
    userInfo = requests.get(url)
    userInfo = userInfo.text
    userInfo = json.loads(userInfo)
    try:
        percent = userInfo["comparison"]["result"]["score"][2:4]
        similar1 = userInfo["comparison"]["result"]["artists"]["artist"][0]["name"]
        similar2 = userInfo["comparison"]["result"]["artists"]["artist"][1]["name"]
        similar3 = userInfo["comparison"]["result"]["artists"]["artist"][2]["name"]

        outt=("%s and %s are %s%% compatible. Similar artists include %s, %s, and %s" % (user1, user2, percent, similar1, similar2, similar3))
    except KeyError:
        outt="One or both users do not exist"
    return outt

# This file is responsible for searching and getting the results from the Trial and Error forums.
import json
import requests
import urllib3
from utils import hyperlink


ANNOUCNMENTS_URL  = 'https://forum.symnet.moe/api/v1/announcements'
FORUM_PREFIX =  'https://forum.symnet.moe/'
SEARCH_URL = 'https://forum.symnet.moe/api/v1/search'

def search(title):
    query = {'query': title}
    r = requests.post(SEARCH_URL, query)
    jsondata = r.json()
    threadlist = []

    for i in range(len(jsondata)):
        forumdict = jsondata[i]
        title = forumdict.get('Title')
        link = FORUM_PREFIX + forumdict.get('Link')
        threadlink = hyperlink(link, title)
        threadlist.append(threadlink)

    return threadlist


def getAnnouncements():
    r = requests.get(ANNOUCNMENTS_URL)
    jsondata = r.json()
    threadList = []

    for i in range(len(jsondata)):
        forumdict = jsondata[i]
        title = forumdict.get('Title')
        link = FORUM_PREFIX + forumdict.get('Link')
        threadlink = hyperlink(link, title)
        threadList.append(threadlink)

    return threadList

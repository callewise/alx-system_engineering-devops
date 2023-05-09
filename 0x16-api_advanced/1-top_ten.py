#!/usr/bin/python3
""" 
    Queries the Reddit API and prints the titles of the 
    first 10 hot posts listed for a given subreddit 
"""
import requests

def top_ten(subreddit):
    user = {"User-Agent": "Scoot"}
    req = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit), headers=user)
    if req.status_code != requests.codes.OK:
        print('None')
        return 0
    else:
        for child in req.json().get('data').get('children'):
            print(child.get('data').get('title'))

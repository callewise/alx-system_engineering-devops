#!/usr/bin/python3
""" 
    recursive function that queries the Reddit API and returns a list 
    containing the titles of all hot articles for a given subreddit 
"""
import requests


def recurse(subreddit, hot_list=[]):
    """ returns a list containing the titles of all hot 
        articles for a given subreddit.
    """
    user = {"User-Agent": "Scoot"}
    if len(hot_list) is 0:
        req = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit), headers=user)
    else:
        req = requests.get("https://www.reddit.com/r/{}/hot.json?after={}_{}"
                           .format((subreddit),
                                   hot_list[-1].get('kind'),
                                   hot_list[-1].get('data').get('id')),
                           headers=user)
    if req.status_code != requests.codes.OK:
        return None
    if len(req.json().get('data').get('children')) < 1:
        return hot_list
    hot_list.extend(req.json().get('data').get('children'))
    return recurse(subreddit, hot_list)

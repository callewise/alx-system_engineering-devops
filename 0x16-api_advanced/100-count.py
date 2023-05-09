#!/usr/bin/python3
"""
    recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
"""
import requests

def count_words(subreddit, word_list, after=None, counts={}):
    if after == None:
        counts = {word.lower(): 0 for word in word_list}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        json_response = response.json()
        data = json_response['data']
        after = data['after']
        children = data['children']

        for child in children:
            title = child['data']['title'].lower()
            for word in word_list:
                if ' ' + word.lower() + ' ' in ' ' + title + ' ':
                    counts[word.lower()] += 1

        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f'{word}: {count}')
    elif response.status_code == 404:
        print(None)
    else:
        print(f'Error: {response.status_code}')

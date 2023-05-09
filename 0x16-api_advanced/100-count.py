#!/usr/bin/python3
"""
    recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
"""
import requests

def count_words(subreddit, word_list, after=None, word_counter={}):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    headers = {'User-Agent': user_agent}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=100'.format(subreddit)
    if after is not None:
        url += '&after=' + after
    resp = requests.get(url,
                        headers=headers,
                        allow_redirects=False)
    if resp.status_code == 200:
        resp_dict = resp.json()
        data_dict = resp_dict.get('data', {})
        a_list = data_dict.get('children', [])
        for post in a_list:
            post_dict = post.get('data', {})
            title = post_dict.get('title')
            if title is not None:
                for word in title.lower().split():
                    for i in range(len(word_list)):
                        if word_list[i].lower() == word:
                            word_counter[word_list[i]] = \
                                word_counter.get(word_list[i], 0) + 1

        after = data_dict.get('after')
        if after is None:
            if word_counter != {}:
                val_dict = {}
                for key in word_counter:
                    if val_dict.get(word_counter[key]) is None:
                        val_dict[word_counter[key]] = [key]
                    else:
                        val_dict[word_counter[key]].append(key)
                for key in sorted(val_dict.keys(), reverse=True):
                    for word in sorted(val_dict[key]):
                        print('{}: {}'.format(word, key))
        else:
            count_words(subreddit, word_list, after, word_counter)

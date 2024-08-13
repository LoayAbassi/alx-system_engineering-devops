#!/usr/bin/python3
"""
contains recurse
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returns list with all hot articles"""
    global after
    headers = {'User-Agent': 'please'}
    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}
    response = requests.get(endpoint, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        after_portion = response.json().get("data").get("after")
        if after_portion is not None:
            after = after_portion
            recurse(subreddit, hot_list)
        all_titles = response.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")

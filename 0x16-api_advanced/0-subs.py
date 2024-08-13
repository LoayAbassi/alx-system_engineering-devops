#!/usr/bin/python3
"""
script that returns number of subcribers of
a subreddit given in argument.
"""


def number_of_subscribers(subreddit):
    """returns number of subscribers"""
    import requests
    headers = {"User-Agent": "somecustomagent"}
    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(endpoint, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0

if __name__ == "__name__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

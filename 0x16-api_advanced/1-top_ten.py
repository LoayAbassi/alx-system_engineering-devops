#!/usr/bin/python3
"""contains top_ten function"""


def top_ten(subreddit):
    """prints top 10 hot posts of a subreddit"""
    import requests

    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {"User-Agent": "someAgentProb"}
    params = {"limit": 10}
    response = requests.get(endpoint, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for e in data:
            post = e["data"]["title"]
            print(post)

    else:
        print(None)

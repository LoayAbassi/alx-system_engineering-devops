#!/usr/bin/python3
"""contains top_ten function"""


def top_ten(subreddit):
    """prints top 10 hot posts of a subreddit"""
    import requests

    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "someAgentProb"}
    params = {"limit": 10}  # Corrected limit

    response = requests.get(endpoint, headers=headers,
                            allow_redirects=False, params=params)

    try:
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            for e in data:
                post = e.get("data", {}).get("title", "No Title")
                print(post)
        else:
            print(None)
    except ValueError:
        print(None)

#!/usr/bin/python3
"""
returns infos about employee's todo list
"""

if __name__ == "__main__":
    import requests
    import sys
    url = "https://jsonplaceholder.typicode.com/"
    userID = int(sys.argv[1])
    # retreiving employee's name
    user = requests.get(url+"users/"+str(userID))
    user = user.json()["name"]

    completed = 0
    total = 0
    Ncompleted = []
    # retreiving employee's todo list
    tasks = requests.get(url+"todos/")
    for task in tasks.json():
        if task["userId"] == int(userID):
            total += 1
            if task["completed"]:
                completed += 1
                Ncompleted.append(task["title"])
    out = f"Employee {user} is done with tasks({completed}/{total}):"
    print(out)

    for title in Ncompleted:
        print("\t {}".format(title))

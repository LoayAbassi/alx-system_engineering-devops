#!/usr/bin/python3
"""
exports data to json
"""

if __name__ == "__main__":
    import json
    import requests
    import sys
    url = "https://jsonplaceholder.typicode.com/"
    userID = int(sys.argv[1])
    # retreiving employee's name
    user = requests.get(url+"users/"+str(userID))

    user = user.json()["username"]

    # retreiving employee's todo list

    todo = requests.get(url+"todos/", params={"userId": userID})
    todo = todo.json()
    res = {userID: []}
    for task in todo:
        item = {}
        item["task"] = task["title"]
        item["completed"] = task["completed"]
        item["username"] = user
        res[userID].append(item)

    filename = str(userID)+".json"
    with open(filename, "w") as file:
        json.dump(res, file)

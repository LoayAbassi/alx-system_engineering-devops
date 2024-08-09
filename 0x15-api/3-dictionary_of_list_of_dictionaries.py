#!/usr/bin/python3
"""
exports data to json of all employees
"""

if __name__ == "__main__":
    import json
    import requests
    url = "https://jsonplaceholder.typicode.com/"
    # retreiving employee's name
    user = requests.get(url+"users/")

    user = user.json()

    users = {}
    for element in user:
        users[element['id']] = element['username']

    # retreiving employee's todo list

    todo = requests.get(url+"todos/", )
    todo = todo.json()
    result = {}
    for task in todo:

        if (task["userId"] not in result):
            result[task["userId"]] = []
        item = {}
        item["username"] = users[task["userId"]]
        item["task"] = task["title"]
        item["completed"] = task["completed"]
        result[task["userId"]].append(item)

    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(result, file)

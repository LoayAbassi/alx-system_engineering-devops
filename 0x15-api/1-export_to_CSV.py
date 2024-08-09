#!/usr/bin/python3
#!/usr/bin/python3
"""
returns infos about employee's todo list
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys
    url = "https://jsonplaceholder.typicode.com/"
    userID = int(sys.argv[1])
    # retreiving employee's name
    user = requests.get(url+"users/"+str(userID))
    name = user.json()["username"]
    # retreiving employee's todo list
    tasks = requests.get(url+"todos/", params={"userId": userID})
    tasks = tasks.json()
    Data = []

    for task in tasks:
        data = []
        data.append(str(userID))
        data.append(name)
        data.append(str(task["completed"]))
        data.append(task["title"])
        Data.append(data)

    filename = str(userID)+".csv"
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(Data)

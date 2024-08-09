#!/usr/bin/python3
"""returns information about a given employee's TODO list progress"""
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    users = f'users?id={employee_id}'
    todos = f'todos?userId={employee_id}'
    done = f'{todos}&completed=true'
    notDone = f'{todos}&completed=false'
    userData = requests.get(f"{url}{users}").json()
    Name = userData[0].get("name")
    todosData = requests.get(f'{url}{todos}').json()
    todosDone = requests.get(f'{url}{done}').json()
    doneN = len(todosDone)
    totalN = len(todosData)
    print(f'Employee {Name} is done with tasks({doneN}/{totalN}):')
    for task in todosDone:
        print(f"\t {task.get('title')}")
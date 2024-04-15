#!usr/bin/python3

""" Python script that using the rest api, for a given empliyéé, returns info about his her todo list progress"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    response = requests.get(url)
    user = response.json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(sys.argv[1])
    response = requests.get(url)
    todos = response.json()
    done = 0
    total = 0
    tasks = []
    for todo in todos:
        total += 1
        if todo.get('completed'):
            done += 1
            tasks.append(todo.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'), done, total))
    for task in tasks:
        print("\t {}".format(task))
        
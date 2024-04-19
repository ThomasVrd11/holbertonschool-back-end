#!/usr/bin/python3
"""Script to retrieve data from a REST API
and export it in JSON format."""
import json
import requests


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"

    USERS = requests.get(f"{URL}/users").json()

    USER_TASK = {}
    for user in USERS:
        tasks = requests.get(f"{URL}/users/{user['id']}/todos").json()

        USER_TASK[user["id"]] = []
        for task in tasks:
            task_dict = {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            USER_TASK[user["id"]].append(task_dict)

    with open("todo_all_employees.json", "w") as file:
        json.dump(USER_TASK, file)

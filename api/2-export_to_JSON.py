#!/usr/bin/python3
"""Script to fetch and export employee TODO list
progress from a REST API to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employeeId(int)")
        sys.exit(1)

    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    RESPONSE = requests.get(
        f"{URL}/users/{EMPLOYEE_ID}/todos",
        params={"_expand": "user"}
    )
    data = RESPONSE.json()

    if not len(data):
        print("RequestError:", 404)
        sys.exit(1)

    USER_TASK = {EMPLOYEE_ID: []}
    for task in data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": task["user"]["username"]
        }
        USER_TASK[EMPLOYEE_ID].append(task_dict)

    with open(f"{EMPLOYEE_ID}.json", "w") as file:
        json.dump(USER_TASK, file)

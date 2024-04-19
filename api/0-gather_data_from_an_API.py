#!/usr/bin/python3
"""Python script to fetch and display TODO list
progress for a given employee ID using a REST API"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__} employee_id(int)")
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

    TASK_TITLE = [task["title"] for task in data if task["completed"]]
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = len(TASK_TITLE)
    EMPLOYEE_NAME = data[0]["user"]["name"]

    print(f"Employee {EMPLOYEE_NAME} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for title in TASK_TITLE:
        print("\t ", title)

#!/usr/bin/python3
"""Script to fetch and export employee TODO list
progress from a REST API to CSV"""
import csv
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

    USERNAME = data[0]["user"]["username"]

    with open(f"{EMPLOYEE_ID}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for task in data:
            writer.writerow(
                [EMPLOYEE_ID, USERNAME, str(task["completed"]), task["title"]]
            )

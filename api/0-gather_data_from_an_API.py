#!usr/bin/python3

""" Python script that using the rest api, for a given empliyéé, returns info about his her todo list progress"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        """ If the number of arguments is different from 2, print the error message"""
        print("Usage: {} <employee_id>".format(sys.argv[1]))
        sys.exit(1)

    URL = "https://jsonplaceholder.typicode.com"

    EMPLOYEE_ID = sys.argv[1]
    """ Get the user info, the user name, and the number of tasks"""

    RESPONSE = requests.get(
        f"{URL}/users/{EMPLOYEE_ID}/todos",
        params={"_expand": "user"}
    )
    data = RESPONSE.json()
    """ It returns a list of dictionaries, where each dictionary represents a task"""

    """ error handling, if the response is empty, print the error message and exit the program"""
    if not len(data):
        print("Resource not found")
        sys.exit(1)

    """ This is the data that we need to extract from the response"""
    TASK_TITLE = [task["title"] for task in data if task["completed"]]
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = len(TASK_TITLE)
    EMPLOYEE_NAME = data[0]["user"]["name"]

    """ Print the data in the format specified in the task description
    The format is as follows:
    Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        TASK_TITLE
        TASK_TITLE
        ..."""
    print(f"Employee {EMPLOYEE_NAME} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for i in TASK_TITLE:
        print("\t ", i)

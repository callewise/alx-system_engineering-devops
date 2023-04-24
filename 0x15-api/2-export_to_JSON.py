#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import json

def export_employee_todo_list(employee_id):
    # make GET request to retrieve employee info
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = response.json()

    # make GET request to retrieve employee's tasks
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    tasks_data = response.json()

    # create dictionary to store tasks
    tasks_dict = {"USER_ID": []}

    # populate dictionary with task data
    for task in tasks_data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_data["username"]
        }
        tasks_dict["USER_ID"].append(task_dict)

    # write dictionary to JSON file
    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump(tasks_dict, jsonfile)
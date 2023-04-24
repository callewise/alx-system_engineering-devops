#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import json

def export_all_employees_todo_list():
    # make GET request to retrieve all employees
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    employees_data = response.json()

    # create dictionary to store tasks for all employees
    tasks_dict = {}

    # iterate over each employee and retrieve their tasks
    for employee in employees_data:
        employee_id = employee["id"]
        employee_username = employee["username"]
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
        tasks_data = response.json()

        # populate dictionary with task data for this employee
        tasks_dict[employee_id] = []
        for task in tasks_data:
            task_dict = {
                "username": employee_username,
                "task": task["title"],
                "completed": task["completed"]
            }
            tasks_dict[employee_id].append(task_dict)

    # write dictionary to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(tasks_dict, jsonfile)
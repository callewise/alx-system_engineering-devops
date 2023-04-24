#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import csv

def export_employee_todo_list(employee_id):
    # make GET request to retrieve employee info
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = response.json()

    # make GET request to retrieve employee's tasks
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    tasks_data = response.json()

    # create CSV file and write header row
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # write each task as a row in the CSV file
        for task in tasks_data:
            writer.writerow([employee_data["id"], employee_data["username"], task["completed"], task["title"]])
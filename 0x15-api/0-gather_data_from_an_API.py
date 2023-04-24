#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests

def get_employee_todo_list(employee_id):
    # make GET request to retrieve employee info
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = response.json()

    # make GET request to retrieve employee's tasks
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    tasks_data = response.json()

    # calculate number of completed tasks
    completed_tasks = [task for task in tasks_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(tasks_data)

    # display employee's progress
    print(f"Employee {employee_data['name']} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")

    # display completed task titles
    for task in completed_tasks:
        print(f"\t {task['title']}")
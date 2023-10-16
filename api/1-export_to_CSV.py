#!/usr/bin/python3
"""Exports data in the CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    # Create a list to store tasks for CSV export
    tasks_for_csv = []

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

            # Add the task to the list for CSV export
            tasks_for_csv.append({
                "USER_ID": userId,
                "USERNAME": name,
                "TASK_COMPLETED_STATUS": task.get('completed'),
                "TASK_TITLE": task.get('title')
            })

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))

    # Export data to CSV
    with open(f'{userId}.csv', 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(tasks_for_csv)

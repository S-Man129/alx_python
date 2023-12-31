#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""

import csv
import requests
import sys


def export_to_CSV(user_id):
    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(user_id)
    ).json()[0]["username"]
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    ).json()

    tasks_data = []

    for task in tasks:
        tasks_data.append(
            [
                user_id,
                employee_name,
                task["completed"],
                task["title"],
            ]
        )

    with open(str(user_id) + ".csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks_data)


if __name__ == "__main__":
    export_to_CSV(sys.argv[1])

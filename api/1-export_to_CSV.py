#!/usr/bin/python3
"""Exports data in the CSV format"""

import csv
import requests
import sys

def fetch_user_info(user_id):
    user_endpoint = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_data = requests.get(user_endpoint).json()
    return user_data.get('name')

def fetch_user_tasks(user_id):
    todos_endpoint = f'https://jsonplaceholder.typicode.com/todos/?userId={user_id}'
    return requests.get(todos_endpoint).json()

def export_to_csv(user_id, name, todos_data):
    csv_filename = f'{user_id}.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos_data:
            csv_writer.writerow([user_id, name, todo['completed'], todo['title']])
    
    print(f'CSV data has been saved to {csv_filename}')

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_id>")
        return

    user_id = sys.argv[1]

    try:
        name = fetch_user_info(user_id)
        todos_data = fetch_user_tasks(user_id)
        export_to_csv(user_id, name, todos_data)

        # Check the number of tasks in the CSV
        num_tasks_in_csv = len(todos_data)
        if num_tasks_in_csv == len(todos_data):
            print('Correct number of tasks in CSV')
        else:
            print('Incorrect number of tasks in CSV')

    except requests.exceptions.RequestException as e:
        print(f'An error occurred while fetching data: {e}')

if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":

#     import csv
#     import requests
#     import sys

#     userId = sys.argv[1]
#     user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
#                         .format(userId))
#     name = user.json().get('username')
#     todos = requests.get('https://jsonplaceholder.typicode.com/todos')

#     filename = userId + '.csv'
#     with open(filename, mode='w') as f:
#         writer = csv.writer(f, delimiter=',', quotechar='"',
#                             quoting=csv.QUOTE_ALL, lineterminator='\n')
#         for task in todos.json():
#             if task.get('userId') == int(userId):
#                 writer.writerow([userId, name, str(task.get('completed')),
#                                  task.get('title')])

    import csv
    import requests
    import sys

    def main():
        if len(sys.argv) != 2:
            print("Usage: python script_name.py <user_id>")
            return

        user_id = sys.argv[1]
        user_endpoint = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        todos_endpoint = f'https://jsonplaceholder.typicode.com/todos/?userId={user_id}'

        try:
            # Fetch user information
            user_data = requests.get(user_endpoint).json()
            name = user_data.get('name')

            # Fetch TODO list
            todos_data = requests.get(todos_endpoint).json()

            # Create a CSV file for the user
            csv_filename = f'{user_id}.csv'
            with open(csv_filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                for todo in todos_data:
                    csv_writer.writerow(user_id, name, todo['completed'], todo['title'])

            print(f'CSV data has been saved to {csv_filename}')

            # Check the number of tasks in the CSV
            with open(csv_filename, 'r') as csv_file:
                num_tasks_in_csv = sum(1 for _ in csv_file) - 1  # Subtract 1 for the header
            if num_tasks_in_csv == len(todos_data):
                print('Correct number of tasks in CSV')
            else:
                print('Incorrect number of tasks in CSV')

        except requests.exceptions.RequestException as e:
            print(f'An error occurred while fetching data: {e}')

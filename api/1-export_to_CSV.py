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

            for task in todos_data:
                task_id = task['id']
                task_title = task['title']
                task_completed = task['completed']
                csv_writer.writerow([user_id, name, task_completed, task_title])

        print(f'CSV data has been saved to {csv_filename}')

    except requests.exceptions.RequestException as e:
        print(f'An error occurred while fetching data: {e}')

if __name__ == "__main__":
    main()

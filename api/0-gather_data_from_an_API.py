import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    
    # Fetch TODO list for the employee
    todo_url = f"{base_url}/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()
    
    # Count the number of completed and total tasks
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    # Print employee TODO list progress
    print(f"Employee {employee_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")

    # Print titles of completed tasks
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

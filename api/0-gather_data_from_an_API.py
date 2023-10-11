import requests

def get_employee_todo_list_progress(employee_id):
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    employee_endpoint = f"{base_url}/users/{employee_id}"
    todo_endpoint = f"{base_url}/users/{employee_id}/todos"

    try:
        # Fetch employee information
        employee_response = requests.get(employee_endpoint)
        employee_data = employee_response.json()
        employee_name = employee_data.get("name")

        # Fetch TODO list
        todo_response = requests.get(todo_endpoint)
        todo_data = todo_response.json()

        # Count the number of completed and total tasks
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task["completed"])

        # Print employee TODO list progress
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

        # Print the titles of completed tasks
        for task in todo_data:
            if task["completed"]:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_todo_list_progress(employee_id)

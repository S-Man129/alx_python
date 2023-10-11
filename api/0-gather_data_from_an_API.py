import requests

def get_employee_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_endpoint = f"{base_url}/users/{employee_id}"
    todo_endpoint = f"{base_url}/users/{employee_id}/todos"

    try:
        employee_response = requests.get(employee_endpoint)
        employee_data = employee_response.json()
        employee_name = employee_data.get("name")

        todo_response = requests.get(todo_endpoint)
        todo_data = todo_response.json()

        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task["completed"])

        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

        for idx, task in enumerate(todo_data, start=1):
            if task["completed"]:
                print(f"Task {idx} Formatting: OK")
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_todo_list_progress(employee_id)

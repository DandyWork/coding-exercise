import requests  # Import the requests library to make HTTP requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
# This sends a GET request to fetch all todo items.

todos = response.json()
# Parse the JSON response into a Python list of dictionaries.

total_todos = len(todos)
print("Total number of todos:", total_todos)

# Count completed todos in a simple way
completed = 0  
for todo in todos:  
    if todo["completed"] == True:  
        completed = completed + 1  

not_completed = total_todos - completed 

print("Number of completed todos:", completed)
print("Number of not completed todos:", not_completed)


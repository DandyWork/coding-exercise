import requests  # Import request library biar bisa pake http

response = requests.get("https://jsonplaceholder.typicode.com/todos") # request GET dari http

todos = response.json() # masukin JSON response dari request biar bisa dipake 

total_todos = len(todos) #nyari totalnya
print("Total number of todos:", total_todos)

# Itung satu2 mana yang completed
completed = 0  
for todo in todos:  
    if todo["completed"] == True:  
        completed = completed + 1  

not_completed = total_todos - completed #sisa total sama completed jadi not completed

print("Number of completed todos:", completed)
print("Number of not completed todos:", not_completed)


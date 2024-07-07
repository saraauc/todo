
ToDo_items = []
ToDo_complete=[]
def things_todo(items):
    for item in items.split():
        ToDo_items.append(item)
    return ToDo_items
def delete_todo(Todo_delete):
    for item in ToDo_items:
        if item == Todo_delete:
            ToDo_items.remove(item)
    return ToDo_items
def complete_todo(complete):
    if complete in ToDo_items:
        ToDo_complete.append(complete)
        ToDo_items.remove(complete)
    print(ToDo_items)
    return ToDo_complete

user_list = input("Enter all the things you have to do this week: ")
print(things_todo(user_list))
user_pactv = input("Do you have anything to add (if no please enter No/no): ")

if (user_pactv == "No" or user_pactv == "no"):
    pass
else:
    print(things_todo(user_pactv))
user_delete = input("Do you want to delete anything (if no please enter No/no): ")

if (user_delete == "No" or user_delete == "no"):
    pass
else:
    print(delete_todo(user_delete))

user_complete=input("Have you completed any task if yes please enter the task else enter No/no: ")
if(user_complete == "No" or user_delete == "no"):
    pass
else:
     print(complete_todo(user_complete))

ToDo_list = []
ToDo_complete = []
def user_interactive():
    while True:
        user_input = input("Please enter: \n - new_list: to create your new list\n" + \
                           " - add: to add anything to your list\n" + \
                           " - delete: to delete anything from your list\n" + \
                           " - completed: if you want to mark a task as complete \n" + \
                           " - E: if you want to Exit: \n")
        if user_input == "E":
            print ("Exiting the application")
            break

        match user_input:
            case "new_list":
                user_list = input("Enter all the things you have to do this week: ")
                print(things_todo(user_list))
            case "add":
                user_pactv = input("Do you have anything to add (if no please enter No/no): ")
                if (user_pactv == "No" or user_pactv == "no"):
                    pass
                else:
                    print(things_todo(user_pactv))
            case "delete":
                user_delete = input("Do you want to delete anything (if no please enter No/no): ")
                if (user_delete == "No" or user_delete == "no"):
                    pass
                else:
                    print(delete_todo(user_delete))

            case "completed":
                user_complete = input("Have you completed any task if yes please enter the task else enter No/no: ")
                if (user_complete == "No" or user_delete == "no"):
                    pass
                else:
                    print(complete_todo(user_complete))

def things_todo(items):
    for item in items.split():
        ToDo_list.append(item)
    return ToDo_list

def delete_todo(Todo_delete):
    for item in ToDo_list:
        if item == Todo_delete:
            ToDo_list.remove(item)
    return ToDo_list

def complete_todo(complete):
    if complete in ToDo_list:
        ToDo_complete.append(complete)
        ToDo_list.remove(complete)
    print(ToDo_list)
    return ToDo_complete


user_interactive()
with open("todolist.txt", "wt") as f:
    f.write("ToDo List: \n")
    f.write("\n".join(ToDo_list) + '\n')
    f.write("Completed Tasks:\n")
    f.write('\n'.join(ToDo_complete)+'\n')



ToDo_list = []
ToDo_complete = []

def load_data():
    ToDo_complete=[]
    with open("todolist.txt","rt") as file:
        lines = file.readlines()
        choice = None
        for line in lines:
            line = line.strip()
            if line == "ToDo List:":
                choice = "todo"
            elif line == "Completed Tasks:":
                choice = "completed"
            elif line and choice == "todo":
                ToDo_list.append(line)
            elif line and choice == "completed" :
                ToDo_complete.append(line)
        return ToDo_list, ToDo_complete
def save_data():
    with open("todolist.txt", "wt") as f:
        f.write("ToDo List: \n")
        f.write("\n".join(ToDo_list) + '\n')
        f.write("Completed Tasks:\n")
        f.write('\n'.join(ToDo_complete) + '\n')
def user_interactive():
    user_new = input("Do you want to see your tasks that needs to be accomplished\n" + \
                     "Enter yes or no:\n")
    if (user_new.lower() == "yes"):
        print(load_data()[0])
    elif (user_new.lower() == "no"):
        pass
    while True:
        user_input = input("Please enter: \n - new_list: to create your new list\n" + \
                           " - add: to add anything to your list\n" + \
                           " - delete: to delete anything from your list\n" + \
                           " - complete: if you want to mark a task as complete \n" + \
                           " - showc: if you want to see the completed tasks \n" +\
                            " - showtask: if you want to see all the tasks \n" +\
                            " - delete_tasks: delete all taskss \n" +\
                            " - deletecomplete: detete completed tasks\n "+\
                           " - E: if you want to Exit: \n" )
        if user_input == "E":
            print ("Exiting the application")
            save_data()
            break

        match user_input:
            case "new_list":
                user_list = input("Enter all the things you have to do this week: ")
                print(things_todo(user_list))
                save_data()
            case "add":
                user_pactv = input("Do you have anything to add (if no please enter No/no): ")
                if (user_pactv == "No" or user_pactv == "no"):
                    pass
                else:
                    print(things_todo(user_pactv))
                    save_data()
            case "delete":
                user_delete = input("Do you want to delete anything (if no please enter No/no): ")
                if (user_delete == "No" or user_delete == "no"):
                    pass
                else:
                    print(delete_todo(user_delete))
                    save_data()

            case "complete":
                user_complete = input("Have you completed any task if yes please enter the task else enter No/no: ")
                if (user_complete == "No" or user_complete == "no"):
                    pass
                else:
                    print(complete_todo(user_complete))
                    save_data()
            case "showc":
                print(load_data()[1])
                save_data()
            case "delete_tasks":
                print(delete_tasks())
                save_data()
            case "showtask":
                print(load_data()[0])
                save_data()
            case "deletecomplete":
                print(delete_complete())
                save_data()
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
def delete_tasks():
    ToDo_list.clear()
    return ToDo_list
def delete_complete():
    ToDo_complete.clear()
    return ToDo_complete
user_interactive()





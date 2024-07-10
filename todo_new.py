import os
import getpass

ToDo_list = []
ToDo_complete = []

def load_data(filename):
    global ToDo_complete, ToDo_list
    ToDo_complete = []
    ToDo_list = []
    if not os.path.exists(filename):
        with open(filename, "w") as file:
           file.write("Username,Task,Status\n")
    with open("task.csv", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            username,task, status= line.strip().split(',')
            if status == "incomplete":
                ToDo_list.append((username,task))
            elif status == "complete":
                ToDo_complete.append((username,task))




'''    with open("tasks.csv","r") as file:
        lines = file.readlines
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
def save_data(filename):
    with open("tasks.csv", "wt") as f:
        f.write("ToDo List: \n")
        f.write("\n".join(ToDo_list) + '\n')
        f.write("Completed Tasks:\n")
        f.write('\n'.join(ToDo_complete) + '\n') '''

def save_data(filename):
    with open(filename,"w") as file:
        file.write("Username,Task,Status\n")
        for username, task in ToDo_list:
            file.write(f"{username},{task},incomplete\n")
        for username, task in ToDo_complete:
            file.write(f"{username},{task},complete\n")
def user_interactive():
    username= input("Please enter your username: ")
    #username=getpass.getuser()
    #print("Current user:", username)
    #password = input("Please enter your password: ")
    file_name = "task.csv"
    load_data(file_name)
    print (file_name)
    load_data(file_name)
    user_new = input("Do you want to see your tasks that needs to be accomplished\n" + \
                     "Enter yes or no:\n")
    if (user_new.lower() == "yes"):
        print([task for user, task in ToDo_list if user == username])
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
                           "- E: if you want to Exit: \n" )
        if user_input == "E":
            print ("Exiting the application")
            save_data(file_name)
            break

        match user_input:
            case "new_list":
                user_list = input("Enter all the things you have to do this week: ")
                print(things_todo(username, user_list))
                save_data(file_name)
            case "add":
                user_pactv = input("Do you have anything to add (if no please enter No/no): ")
                if (user_pactv == "No" or user_pactv == "no"):
                    pass
                else:
                    print(things_todo(username, user_pactv))
                    save_data(file_name)
            case "delete":
                user_delete = input("Do you want to delete anything (if no please enter No/no): ")
                if (user_delete == "No" or user_delete == "no"):
                    pass
                else:
                    print(delete_todo(username, user_delete))
                    save_data(file_name)

            case "complete":
                user_complete = input("Have you completed any task if yes please enter the task else enter No/no: ")
                if (user_complete == "No" or user_complete == "no"):
                    pass
                else:
                    print(complete_todo(username, user_complete))
                    save_data(file_name)
            case "showc":
                print([task for user, task in ToDo_complete if user == username])
                save_data(file_name)
            case "delete_tasks":
                print(delete_tasks(username))
                save_data(file_name)
            case "showtask":
                print([task for user, task in ToDo_list if user == username])
                save_data(file_name)
            case "deletecomplete":
                print(delete_complete(username))
                save_data(file_name)
def things_todo(username, items):
    global ToDo_list
    for item in items.split(","):
        ToDo_list.append((username, item.strip()))
    return ToDo_list

def delete_todo(username, Todo_delete):
    global ToDo_list
    ToDo_list = [task for task in ToDo_list if not (task[0] == username and task[1] == Todo_delete)]
    return ToDo_list


def complete_todo(username, complete):
    global ToDo_list, ToDo_complete
    ToDo_list = [(user, task) for user, task in ToDo_list if not (user == username and task == complete)]
    ToDo_complete.append((username, complete))
    return ToDo_complete
def delete_tasks(username):
    global ToDo_list
    ToDo_list = [task for task in ToDo_list if task[0] != username]
    return ToDo_list
def delete_complete(username):
    global ToDo_complete
    ToDo_complete = [task for task in ToDo_complete if task[0] != username]
    return ToDo_complete


user_interactive()

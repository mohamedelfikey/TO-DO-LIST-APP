# Build TO DO LIST APPLICATIONS

# APP features:
# 1- add tasks
# 2- mark tasks as complete
# 3- veiw tasks
# 4- quit


def add_task ():
    # get task from user
    task = input("Enter task: ")

    # define task info
    task_info = {"task": task, "completed": False}

    # add task to the list of tasks
    tasks.append(task_info)
    print ("Task added to the list successufly.")

    # print message to the user
    print (f"Tasks: \n {tasks}")
    print ("-"*30)



def mark_task_complete():
    # get list of incomplete tasks
    incomplete_tasks = [task for task in tasks if task["completed"] == False] # aliasing
    
    # handle if empty incomplete tasks
    if not incomplete_tasks:
        print ("NO tasks to mark as completed.")
        return
    
    # show incomplete tasks to the user
    print ("Incomplete tasks: ")
    for i, task in enumerate(incomplete_tasks):
        print (f'{i+1}- {task["task"]}')
        print("-"*30)

    try:
        # get task number from the user
        task_number = int(input("Choose the task number to complete: "))

        if task_number < 1 or task_number > len(task_number):
            print ("Invalid task number")
            return
        
        # mark task as completed
        incomplete_tasks[task_number-1]["completed"] = True
        # print message to the user
        print ("Task marked completed.")

    except ValueError:
        print ("Invalid input, Please enter a number.")


    
        

def view_tasks():
    # handle if empty tasks
    if not tasks:
        print ("No tasks to view.")
        return
    
    print ("Tasks: ")
    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "❌" 
        print (f"{i+1} - {task["task"]} {status}")
        print ("-"*30)



def main():
    message = """1- add tasks
2- mark tasks as complete
3- veiw tasks
4- quit """

    global tasks
    tasks = []
    # complete_tasks = []

    while True:
        print (message)
        choice = input("Enter your choice: ")

        if choice == "1":
            # add taksk to tasks list
            add_task()
        elif choice == "2":
            # mark task as complete
            mark_task_complete()
        elif choice == "3":
            # view tasks
            view_tasks()
        elif choice == "4":
            # quit
            break
        else:
            print ("Invalid choice, please enter a number between 1 to 4.")



if __name__ == "__main__":
    main()



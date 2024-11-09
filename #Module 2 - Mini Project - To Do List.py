#Module 2 - Mini Project - To Do List



def to_do_list():
    tasks = []
    while True:
        print("\n ******** TO_DO_LIST ********")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Mark a Task as Complete")
        print("4. Delete a Task")
        print("5. Exit")
        choice = input("Enter your choice:  ")
        try:
                       
            if choice == "1":
                print()
                n_tasks = int(input("How many tasks would you like to add: "))
                for i in range(n_tasks):
                    task = input("Enter the task: ").upper()
                    tasks.append({"task": task, "complete":False})
                    print("Task Added")
            
            elif choice == "2":
                print("\n Tasks")
                for index, task in enumerate (tasks):
                    status = "Complete" if task ["complete"] else "Not Complete"
                    print(f"{index + 1} - {task ['task']} - {status}")
                    
            elif choice == "3":
                task_index = int(input("Enter the task number to mark as complete: ")) - 1
                if 0<= task_index < len(tasks):
                    tasks[task_index]["complete"] = True
                    print("Task marked as complete.")
                else:
                    print("Invalid task number")
                    
            elif choice == "4":
                print()
                tasks_remove = int(input("How many tasks would you like to remove: "))
                for r in range(tasks_remove):
                    task = int(input("Enter the task to remove: ")) -1
                    tasks.pop(tasks_remove)
                    print("Task Removed")
                                
            elif choice == "5":
                print("Exiting the To-Do-List")
                break
        except ValueError:
            print("Please enter a number")
        # else:
        #     print("Invalid Entry. Try Again!")

to_do_list()
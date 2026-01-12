def show_interface():
    print("TODO LISTTTT")
    print("Press 1 to insert task")
    print("Press 2 to delete task")
    print("Press 3 to edit task")
    print("Press 4 to view task")

show_interface()

try:
    ans = int(input("Click any option:\n"))

    if ans == 1:
        # Insert tasks
        while True:
            no_of_task = int(input("How many tasks do you want to print today? "))
            if no_of_task < 1:
                print("Please enter at least 1 task.")
            else:
                break

        for i in range(no_of_task):
            with open("TODOLIST.txt", "a") as f:
                task = input(f"Enter your task {i+1}: ")
                f.write(task + '\n')
                print("Successfully Added :)")

    elif ans == 2:
        # Delete tasks
        ask = input("Enter what kind of task to delete.\n a. Entire tasks \n b. Specific task: ")
        ask = ask.lower()
        if ask == 'a':
            with open("TODOLIST.txt", "w") as f:
                pass  # clears the file
            print("ALL ITEMS ARE CLEARED")
        elif ask == 'b':
            with open('TODOLIST.txt', 'r') as f2:
                tasks = f2.readlines()

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

            tasksdel = int(input("Tell me which task number you want to delete: "))

            if 0 < tasksdel <= len(tasks):
                del tasks[tasksdel - 1]
                with open('TODOLIST.txt', 'w') as f3:
                    f3.writelines(tasks)
                print(f"Task {tasksdel} deleted.")
            else:
                print("Invalid task number.")
        else:
            print("Invalid option.")

    elif ans == 3:
        # Edit task
        with open("TODOLIST.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to edit.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

            task_num = int(input("Which task number do you want to edit? "))
            new_task = input("Enter the new task: ")

            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1] = new_task + '\n'
                with open("TODOLIST.txt", "w") as file:
                    file.writelines(tasks)
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif ans == 4:
        # View all tasks
        try:
            with open("TODOLIST.txt", "r") as f:
                tasks = f.readlines()
                if not tasks:
                    print("No tasks found.")
                else:
                    print("Your tasks:")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task.strip()}")
        except FileNotFoundError:
            print("No task file found. Create some tasks first.")

    else:
        print("Invalid choice. Please choose from 1 to 4.")

except ValueError:
    print("Enter only valid numbers please.")

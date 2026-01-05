import os

print("=" * 40)
print("TODO LIST")
print("=" * 40)

# Load existing tasks from file
tasks = []
if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as f:
        tasks = [line.strip() for line in f.readlines()]

while True:
    print("\nEnter your choices:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    
    ask = input("\nChoose an option (1/2/3/4): ").strip()
    
    if ask == '1':
        task = input("Enter your task: ")
        tasks.append(task)
        print("✓ Task added.")
        
        # Save to file
        with open("tasks.txt", "a") as f:
            f.write(task + "\n")
        print("✓ Task saved to file.")
    
    elif ask == "2":
        print("\n--- Your Tasks ---")
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet. Add some!")
    
    elif ask == "3":
        if not tasks:
            print("No tasks to remove!")
            continue
            
        print("\nCurrent tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        
        task_to_remove = input("\nEnter the task number or name to remove: ")
        
        # Try removing by number first
        try:
            index = int(task_to_remove) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"✓ Removed: {removed}")
            else:
                print(" Invalid task number.")
                continue
        except ValueError:
            # Remove by name
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                print(f"✓ Removed: {task_to_remove}")
            else:
                print(" Task not found.")
                continue
        
        # Rewrite file
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
        print("✓ File updated.")
    
    elif ask == "4":
        print("\nGoodbye! Stay productive! 👋")
        break
    
    else:
        print(" Invalid option. Please choose 1, 2, 3, or 4.")
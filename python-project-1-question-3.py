# 3rd Description:
# To-Do List App (Text-Based) 3rd question
# Skills practiced: lists, string parsing, loops, input, CRUD basics (CRUD = Create, Read, Update, Delete)

tasks = []  # list to store all tasks
completed_tasks = []  # list to store completed tasks

print("Welcome to Your To-Do List App")
print("Type: add / view / done / delete / exit\n")

while True:
    action = input("Enter action: ").strip().lower()  # strip() removes extra spaces; lower() standardizes input

    # Add a new task
    if action == "add":
        task_input = input("Enter task: ")
        tasks.append(task_input)
        print(f"Task added: {task_input}\n")

    # View all tasks
    elif action == "view":
        if not tasks:
            print("No tasks in your list.\n")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            print()

    # Mark a task as completed
    elif action == "done":
        if not tasks:
            print("No tasks to mark as done.\n")
        else:
            num = int(input("Enter task number to mark complete: ")) - 1
            if 0 <= num < len(tasks):
                completed_tasks.append(tasks[num])
                print(f"Marked as done: {tasks[num]}\n")
                tasks.pop(num)
            else:
                print("Invalid task number.\n")

    # Delete a task
    elif action == "delete":
        if not tasks:
            print("No tasks to delete.\n")
        else:
            num = int(input("Enter task number to delete: ")) - 1
            if 0 <= num < len(tasks):
                print(f"Deleted: {tasks[num]}\n")
                tasks.pop(num)
            else:
                print("Invalid task number.\n")

    # Exit the program
    elif action == "exit":
        break

    else:
        print("Invalid command! Try again.\n")

# Summary at the end
print("\n To-Do List Summary")
print(f"Completed tasks: {len(completed_tasks)}")
print(f"Pending tasks: {len(tasks)}")
print("Goodbye!")

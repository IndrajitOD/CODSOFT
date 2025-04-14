def display_choice():
    print("--------------------------------------------------------")
    print("Enter the operation you want to perform\n")
    print("1. Add a task to the list")
    print("2. Remove a task from the list")
    print("3. View the list")
    print("4. Update a task in the list")
    print("5. Mark task as done or not done")
    print("6. Exit the list.")

def add_task(task_list):
    task_name = input("Enter the task to add to the list: ")
    task = {"name": task_name, "done": False}
    task_list.append(task)
    print("Task", task_name, "added successfully in the list!")

def delete_task(task_list):
    task_name = input("Enter the task to delete from the list: ")
    for task in task_list:
        if task["name"] == task_name:
            task_list.remove(task)
            print("Task", task_name, "deleted successfully!")
            return
    print("Error! Your task was not found in the list")

def view_tasks(task_list):
    if task_list:
        print("\nYour tasks:")
        i = 1
        for task in task_list:
            if task["done"]:
                status = "Done"
            else:
                status = "Not Done"
            print(i, ":", task["name"], "[", status, "]")
            i += 1
    else:
        print("\nList is empty!")

def update_task(task_list):
    task_name = input("Enter the task to update in the list: ")
    for task in task_list:
        if task["name"] == task_name:
            new_name = input("Enter the new task: ")
            task["name"] = new_name
            print("Task", task_name, "updated to", new_name, "successfully!")
            return
    print("This task was not found in the list")

def mark_done(task_list):
    task_name = input("Enter the task to mark done or not done: ")
    for task in task_list:
        if task["name"] == task_name:
            task["done"] = not task["done"]
            status = "Done" if task["done"] else "Not Done"
            print("Task", task_name, "marked as", status)
            return
    print("This task was not found in the list")

def main():
    print("Welcome to my simple to-do list")
    print("This can add tasks, delete, view, update, and mark tasks as done")
    task_list = []
    while True:
        display_choice()
        operation = input("\nEnter your choice (1-6): ")
        if operation.isdigit():
            operation = int(operation)
            if operation == 1:
                add_task(task_list)
            elif operation == 2:
                delete_task(task_list)
            elif operation == 3:
                view_tasks(task_list)
            elif operation == 4:
                update_task(task_list)
            elif operation == 5:
                mark_done(task_list)
            elif operation == 6:
                print("Exiting the to-do list. Thank you for using my To-Do-List!")
                print("All the tasks are deleted from the list!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.\n")
        else:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
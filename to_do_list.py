def display_choice():
    print("--------------------------------------------------------")
    print("Enter the operation you want to perform\n")
    print("1. Add a task to the list")
    print("2. Delete a task from the list")
    print("3. View the list")
    print("4. Update a task in the list")
    print("5. Exit the list.")

def add_task(task_list):
    task = input("Enter the task to add to the list: ")
    task_list.append(task)
    print("Task ",task," added successfully in the list!")

def delete_task(task_list):
    task = input("Enter the task to delete from the list: ")
    if task in task_list:
        task_list.remove(task)
        print("Task ",task," deleted successfully!")
    else:
        print("Error! Your task was not found in the list")
        print("Enter a valid task to delete from the list")

def view_tasks(task_list):
    if task_list:
        print("\nYour tasks:")
        i = 1
        for task in task_list:
            print(i," : ",task)
            i =i+1
    else:
        print("\List is empty!")

def update_task(task_list):
    task = input("Enter the task to update in the list: ")
    if task in task_list:
        index = task_list.index(task)
        new_task = input("Enter the new task: ")
        task_list[index] = new_task
        print("Task ",task," updated to ",new_task," successfully!")
    else:
        print("This task was not found in the list")

def main():
    print("Welcome to my simple to-do list")
    print("This can add a tasks, delete a task, view, and update your tasks in the list")
    task_list = []
    while True:
        display_choice()
        operation =int(input("\nEnter your choice (1-5): "))
        if operation == 1:
            add_task(task_list)
        elif operation == 2:
            delete_task(task_list)
        elif operation == 3:
            view_tasks(task_list)
        elif operation == 4:
            update_task(task_list)
        elif operation == 5:
            print("Exiting the to-do list. Thank you for using the To-Do-List!")
            print("All the tasks are deleted from the list!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
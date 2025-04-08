print ("Welcome to my simple to do list")
print ("I have creater this list where you can add tasks, delete a task, view and update your tasks in the list")
choice ="c"
list = []
while choice == "c":
    print("--------------------------------------------------------")
    print("Enter the operation you want to perform\n")
    operation = (input("1. Enter a to add a task to the list\n2. Enter d to delete a task from the list\n3. Enter v to view the list\n4. Enter u to update task in the list\n"))
    if operation =="a":
        task = input("Enter the task to add to the list : ")
        list.append(task)
    elif operation == "d":
        task=input("Enter the task to delete from the list : ")
        if task in list:
            list.remove(task)
        else:
            print("Your task was not found in the list")
    elif operation == "v":
        print(list)
    elif operation =="u":
        task=input("Enter the task to update in the list : ")
        if task in list:
            index = list.index(task)
            new = input("Enter the new task : ")
            list[index]=new
        else:
            print("this Task was not found in the list")
    else:
        print("\nInvalid operation\n")
    choice=input("\nEnter c to continue or any other key to quit\n")
print("Thank you for using my to do list")

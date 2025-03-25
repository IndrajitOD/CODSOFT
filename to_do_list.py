#aim to create a simple to do list 
print ("Welcome to my simple to do list")
print ("I have creater this list where you can add tasks, delete a task, view and update your tasks in the list")
choice ="c" #here i am initializing the choice variable to c so that the loop can run, until it is changed to any other key
list = [] #here i am creating an empty list
while choice == "c": #to run the instructions multiple times, until the user wants to quit
    print("Enter the operation you want to perform\n")
    operation = (input("1. Enter a to add a task to the list\n2. Enter d to delete a task from the list\n3. Enter v to view the list\n4. Enter u to update task in the list\n"))
    if operation =="a":
        task = input("Enter the task to add to the list : ")
        list.append(task) #here i am using the append function to add a task to the list
    elif operation == "d":
        task=input("Enter the task to delete from the list : ")
        if task in list:
            list.remove(task) #here i am using the remove function to delete a task from the list
        else:
            print("Your task was not found in the list") #if the task entered is not found in the list
    elif operation == "v":
        print(list) #here i am just printing the list, for viewing the list
    elif operation =="u":
        task=input("Enter the task to update in the list : ")
        if task in list:
            index = list.index(task) #to select the index of the task to be updated
            new = input("Enter the new task : ")
            list[index]=new #storing the new task in the old task
        else:
            print("this Task was not found in the list")
    else:
        print("\nInvalid operation\n") #if entered any other key then this shown
    choice=input("\nEnter c to continue or any other key to quit\n") #if any other key is given, the while loop will break
print("Thank you for using my to do list")
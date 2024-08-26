from tabulate import tabulate
import pickle
import atexit
import sys
import os
import time

def saveList():
    with open("todolists.pkl", "wb") as file:
        pickle.dump(todolist, file)




class Task():
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.status = "Not Started"
      
    def changeName(self, newName):
        self.name = newName
    
    def setDescription(self, description):
        self.description = description

    def changeStatus(self, newStatus):
        self.status = newStatus


class ToDoList():
    def __init__(self, name = "My To-Do List"):
        self.name = name
        self.taskList = []

    def addTask(self, taskName = ""):
        newTask = Task(taskName)
        self.taskList.append(newTask)
        print("\nTask added successfully!")
        saveList()

    def removeTask(self, taskName):
        for task in self.taskList:
            if task.name == taskName:
                self.taskList.remove(task)
                print("\nTask removed successfully!")
                saveList()
                break
        else:
            print("\nError: Task not found.")

    def modifyTask(self, taskName, operation, change):
        for task in self.taskList:
            if task.name == taskName:
                if operation == "name":
                    task.changeName(change)
                    print("\nTask edited successfully!")
                elif operation == "description":
                    task.setDescription(change)
                    print("\nTask edited successfully!")
                elif operation == "status":
                    task.changeStatus(change)
                    print("\nTask edited successfully!")
                else:
                    print("\nError: Invalid Operation")
                break
            saveList()
        else:
            print("\nError: Task not found.")

    def printList(self):
        if self.isEmpty():
            print("\nYou do not have any tasks in your To-Do\n")
            return
        tasks = [[task.name, task.description, task.status] for task in self.taskList]
        headers = ["Name", "Description", "Status"]
        print()
        print()
        print(self.name)
        print()
        print(tabulate(tasks, headers = headers, tablefmt = "grid"))
        print()
        print()

    def isEmpty(self):
        return not self.taskList


os.system("cls" if os.name == "nt" else "clear")

try:
    with open("todolists.pkl", "rb") as file:
        todolist = pickle.load(file)
except (FileNotFoundError, EOFError):
    todolist = ToDoList()

atexit.register(saveList)

ok = True
while ok:
    if not todolist.isEmpty(): 
        todolist.printList() 
    else: 
        print("\nYou do not have any tasks in your To-Do\n")

    print("\n(1) Add a new task\n(2) Delete a task\n(3) Update a task\n(4) Exit Program\n")

    choice = input("\nSelect an action by entering the corresponding number: ")
    while not choice.isdigit() or int(choice) not in range(1,5):
        choice = input("\nInvalid option. Please enter a number from 1 to 4: ")

    choice = int(choice)

    cancel = False

    if todolist.isEmpty() and (choice == 2 or choice == 3):
        continue

    if choice == 1:
        newTask = input("\nTitle of new task: ")
        todolist.addTask(newTask)

    elif choice == 2:
        toDelete = input("\nTitle of task to be deleted: ")
        todolist.removeTask(toDelete)

    elif choice == 3:
        cancel = False
        taskName = input("\nTitle of task to be updated: ")
        opInt = input("\n(1) Change task name\n(2) Set task description\n(3) Update task status\n(4) Cancel\nSelect an action by entering the corresponding number: ")
        while not opInt.isdigit() or int(opInt) not in range(1,5):
            opInt = input("\nInvalid option. Please enter a number from 1 to 4: ")
        opInt = int(opInt)
        operation = ""
        change = ""
        if opInt == 1:
            operation = "name"
            change = input("\nNew title of task: ")

        elif opInt == 2:
            operation = "description"
            change = input("\nNew description: ")

        elif opInt == 3:
            operation = "status"
            chInt = input("\n(1) Not Started\n(2) In Progress\n(3) Completed\nSelect new status: ")
            while not chInt.isdigit() or int(chInt) not in range(1,4):
                chInt = input("\nInvalid option. Please enter a number from 1 to 3: ")
            chInt = int(chInt)
            if chInt == 1:
                change = "Not Started"
            elif chInt == 2:
                change = "In Progress"
            elif chInt == 3:
                change = "Completed"

        elif opInt == 4:
            cancel = True

        if not cancel:
            todolist.modifyTask(taskName, operation, change)

    elif choice == 4:
        ok = False
        print("\nSaving . . .")
        time.sleep(3)
        sys.exit()









       




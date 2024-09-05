from tabulate import tabulate
from datetime import datetime
import pickle
import atexit
import sys
import os
import time
import textwrap

def saveList():
    with open("todolists.pkl", "wb") as file:
        pickle.dump(todolist, file)


def textWrap(text, width = 30):
    return "\n".join(textwrap.wrap(text, width))

class Task():
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.status = "Not Started"
        # self.deadline = ""
      
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

    def removeTask(self, taskNum):
        self.taskList.pop(taskNum-1)
        print("\nTask removed successfully!")
        saveList()

    def modifyTask(self, taskNum, operation, change):
        task = self.taskList[taskNum-1]
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
        saveList()

    def printList(self):
        if self.isEmpty():
            print("\nYou do not have any tasks in your To-Do\n")
            return
        tasks = [[index + 1, textWrap(task.name), textWrap(task.description), task.status] for index, task in enumerate(self.taskList)]
        headers = ["", "Name", "Description", "Status"]
        print()
        print()
        print(self.name)
        print()
        print(tabulate(tasks, headers = headers, tablefmt = "grid"))
        print()
        print()

    def isEmpty(self):
        return not self.taskList

    def getSize(self):
        return len(self.taskList)

    def clearList(self):
        self.taskList.clear()
        print("\nList cleared successfully!")

try:
    with open("todolists.pkl", "rb") as file:
        todolist = pickle.load(file)
except (FileNotFoundError, EOFError):
    todolist = ToDoList()

atexit.register(saveList)

ok = True
while ok:
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
    if not todolist.isEmpty(): 
        todolist.printList() 
    else: 
        print("\nYou do not have any tasks in your To-Do\n")

    print("\n(1) Add a new task\n(2) Delete a task\n(3) Update a task\n(4) Clear list\n(5) Exit Program\n")

    choice = input("\nSelect an action by entering the corresponding number: ")
    while not choice.isdigit() or int(choice) not in range(1,6):
        choice = input("\nInvalid option. Please enter a number from 1 to 5: ")

    choice = int(choice)

    cancel = False

    if todolist.isEmpty() and (choice == 2 or choice == 3 or choice == 4):
        print("\nYou do not have any tasks in your To-Do\n")
        continue

    if choice == 1:
        newTask = input("\nTitle of new task: ")
        todolist.addTask(newTask)

    elif choice == 2:
        toDelete = input("\nNumber of task to be deleted: ")
        while not toDelete.isdigit() or int(toDelete) not in range(1,todolist.getSize()+1):
            toDelete = input("\nInvalid option. Please enter a number from 1 to " + str(todolist.getSize()) + ": ")
        toDelete = int(toDelete)
        todolist.removeTask(toDelete)

    elif choice == 3:
        cancel = False
        taskNum = input("\nNumber of task to be updated: ")
        while not taskNum.isdigit() or int(taskNum) not in range(1,todolist.getSize()+1):
            taskNum = input("\nInvalid option. Please enter a number from 1 to " + str(todolist.getSize()) + ": ")
        taskNum = int(taskNum)

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
            todolist.modifyTask(taskNum, operation, change)

    elif choice == 4:
        print("\nAre you sure you would like to clear your To-Do List?\nThis action cannot be reverted")
        num = input("(1) Yes\n(2) No\n\n")
        while not num.isdigit() or int(num) not in range(1,3):
            num = input("\nInvalid option. Please enter a number from 1 to 2: ")
        num = int(num)
        if num == 1:
            todolist.clearList()
          
    elif choice == 5:
        ok = False
        print("\nSaving . . .")
        time.sleep(3)
        print("Save Successful!\n")
        sys.exit()









       




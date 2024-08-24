from tabulate import tabulate

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
    def __init__(self, name = "To-Do List"):
        self.name = name
        self.taskList = []

    def addTask(self, taskName = ""):
        newTask = Task(taskName)
        self.taskList.append(newTask)

    def removeTask(self, taskName):
        for task in self.taskList:
            if task.name == taskName:
                self.taskList.remove(task)
                print("Task removed successfully!")
                break
        else:
            print("Error: Task not found.")

    def modifyTask(self, taskName, operation, change):
        for task in self.taskList:
            if task.name == taskName:
                if operation == "name":
                    task.changeName(change)
                    print("Task edited successfully!")
                elif operation == "description":
                    task.setDescription(change)
                    print("Task edited successfully!")
                elif operation == "status":
                    task.changeStatus(change)
                    print("Task edited successfully!")
                else:
                    print("Error: Invalid Operation")
                break
        else:
            print("Error: Task not found.")

    def printList(self):
        tasks = [[task.name, task.description, task.status] for task in self.taskList]
        headers = ["Name", "Description", "Status"]
        print()
        print()
        print(self.name)
        print()
        print(tabulate(tasks, headers = headers, tablefmt = "grid"))
        print()
        print()



choresList = ToDoList("Chores")

choresList.addTask("Clean room")
choresList.addTask("Sweep floors")
choresList.printList()
choresList.modifyTask("Clean room", "status", "Started")
choresList.printList()
choresList.modifyTask("Sweep floors", "description", """In kitchen before lunch\nand living room before saturday.\nand in bathroom too""")
choresList.printList()
       




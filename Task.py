# Task class file
from datetime import date
# Class for tasks
class Task:
    name = ""
    dateTask = date(1, 1, 1)
    prio = 0
    def __init__(self, name, dateTask, prio):
        self.name = name
        self.dateTask = dateTask
        self.prio = prio

    # Method that prints task info
    def printTaskInfo(self):
        print("Your task is:", self.name)
        print("It must be completed by:", self.dateTask)
        print("It has a priority level of:", self.prio)

    # Method that updates the task name to what is provided
    def updateName(self, newName):
        self.name = newName

    # Method that updates the task date to what is provided
    def updateDate(self, newDate):
        self.dateTask = newDate

    # Method that updates the task priority to what is provided
    def updatePrio(self, newPrio):
        self.prio = newPrio

    # Method that returns the name of the task
    def returnName(self):
        return self.name

    # Method that returns the date of the task
    def returnDate(self):
        return self.dateTask

    # Method that returns the priority of the task
    def returnPrio(self):
        return self.prio
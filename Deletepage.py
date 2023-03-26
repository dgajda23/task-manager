from Functions import *
from Task import *

# Method that displays the page for deleting a task
def displayDeletePage(service):
    # Getting the list of tasks from the provided month
    month = getMonth()
    listTasks = list(service.searchByMonth(month))
    printTasksByMonth(month, listTasks)
    taskToDelete = getTaskInfoNoMonth(month)

    # Asking for confirmation from the user before deleting
    taskToDelete.printTaskInfo()
    message = "Are you sure you want to delete this task?"
    if (confirmation(message) == "Yes"):
        service.deleteTask(taskToDelete.returnName(), taskToDelete.returnDate().month, taskToDelete.returnDate().day,
                            taskToDelete.returnDate().year, taskToDelete.returnPrio())
        input("Task deleted. Press enter to continue...")
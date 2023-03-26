# Home page of application
from Functions import *

# Method that displays the home menu of the application
def displayHomeMenu():
    # App name
    print(" ______  _____       ____    _____       ______  ______    ")
    print("/\__  _\/\  __`\    /\  _`\ /\  __`\    /\__  _\/\__  _\  ")
    print("\/_/\ \/\ \ \/\ \   \ \ \/\ \ \ \/\ \   \/_/\ \/\/_/\ \/  ")
    print("   \ \ \ \ \ \ \ \   \ \ \ \ \ \ \ \ \     \ \ \   \ \ \  ")
    print("    \ \ \ \ \ \_\ \   \ \ \_\ \ \ \_\ \     \_\ \__ \ \ \ ")
    print("     \ \_\ \ \_____\   \ \____/\ \_____\    /\_____\ \ \_\ ")
    print("      \/_/  \/_____/    \/___/  \/_____/    \/_____/  \/_/\n")                                                                                                            

    # Description
    print("Application that handles all your task managing needs!\n\n")
    print("Use the arrow keys to select an option!")
    options = ["Add a task", "View list of tasks", "Search tasks by month", "Quit"]
    title = "Select an option below and hit enter"
    return displayMenu(options, title)





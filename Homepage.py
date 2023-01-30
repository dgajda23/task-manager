from simple_term_menu import TerminalMenu

def displayHomeMenu():\
    # App name
    print(" ______  _____       ____    _____       ______  ______    ")
    print("/\__  _\/\  __`\    /\  _`\ /\  __`\    /\__  _\/\__  _\  ")
    print("\/_/\ \/\ \ \/\ \   \ \ \/\ \ \ \/\ \   \/_/\ \/\/_/\ \/  ")
    print("   \ \ \ \ \ \ \ \   \ \ \ \ \ \ \ \ \     \ \ \   \ \ \  ")
    print("    \ \ \ \ \ \_\ \   \ \ \_\ \ \ \_\ \     \_\ \__ \ \ \ ")
    print("     \ \_\ \ \_____\   \ \____/\ \_____\    /\_____\ \ \_\ ")
    print("      \/_/  \/_____/    \/___/  \/_____/    \/_____/  \/_/\n")
                                                          
                                                          


    # DESCRPTION HERE
    print("Application that handles all your task managing needs!\n\n")
    
    print("Use the arrow keys to select an option!")
    options = ["Add a task", "View list of tasks", "View calendar", "Search tasks by date", "Quit"]
    terminal_menu = TerminalMenu(options, title="Select an option below and hit enter")
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]





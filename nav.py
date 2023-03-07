import os


def main_menu_nav(name, display_main_menu, choice):
    while True:
        print(f"{name}, when ready, press 'Enter' to head over ".center(80))
        print("to the main menu: ".center(80))    
        choice = input("\n ".center(80)).capitalize()
        if not choice.strip():
            display_main_menu(name)  # display the main menu again
            os.system('clear')
            break
    return name






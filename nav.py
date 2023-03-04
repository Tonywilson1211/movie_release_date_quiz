def landing_page_nav(name, display_main_menu, choice):
    while True:
        print(f"{name}, when ready, press 'Enter' to head over to the main menu: ".center(80))    
        choice = input("\n ".center(80)).capitalize()
        if not choice.strip():
            display_main_menu(name)  # display the main menu again
            break
    return name
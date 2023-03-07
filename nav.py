def main_menu_nav(name, display_main_menu, choice):
    while True:
        print(f"{name}, when ready, press 'Enter' to head over ".center(80))
        print("to the main menu: ".center(80))    
        choice = input("\n ".center(80)).capitalize()
        if not choice.strip():
            display_main_menu(name)  # display the main menu again
            break
    return name


def get_clue_choice():
    """
    Get the user's choice on whether they want a clue.
    """
    error_message = ""
    while True:
        clue_choice = input(f"\033[F\033[K{error_message} \nWould "
                            "you like a clue? (Y or N): ").strip().upper()
        if clue_choice not in ['Y', 'N']:
            error_message = "\033[F\033[KInput not recognised. "\
                            "Please enter 'Y' or 'N'"
        else:
            error_message = ""
            break
    return clue_choice



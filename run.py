import json
import random
import os
import time


def print_slowly(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)
    print()


def load_questions():
    """
    Pull questions from movies.json file.
    """
    with open('movies.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)
    random.shuffle(questions)
    return questions


def print_question_header(question_num):
    """
    Print movie name and question number out of 10.
    """
    os.system('clear')
    print('''
           ██████╗ ██╗   ██╗███████╗███████╗███████╗
          ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝
          ██║  ███╗██║   ██║█████╗  ███████╗███████╗
          ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║
          ╚██████╔╝╚██████╔╝███████╗███████║███████║
           ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝
████████╗██╗  ██╗███████╗    ██╗   ██╗███████╗ █████╗ ██████╗
╚══██╔══╝██║  ██║██╔════╝    ╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗
   ██║   ███████║█████╗       ╚████╔╝ █████╗  ███████║██████╔╝
   ██║   ██╔══██║██╔══╝        ╚██╔╝  ██╔══╝  ██╔══██║██╔══██╗
   ██║   ██║  ██║███████╗       ██║   ███████╗██║  ██║██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
    ''')
    print(f"\n{'*' * 17} Question {question_num+1} of 5 {'*' * 18}")


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


def print_question_clue(question):
    """
    Prints the clue for the user when they ask for a clue.
    """
    print_slowly(f"\nClue: {question['clue']}\n\n\n")


def get_user_answer():
    """
    User inputs their answer into the terminal.
    """
    error_message = ""
    while True:
        answer = input(f"\033[F\033[K{error_message}Guess the "
                       "year (e.g. 1990): ").strip()
        if len(answer) != 4:
            error_message = "\033[F\033[KPlease enter a year as a "\
                            "4-digit number. e.g. 2004.\n"
        else:
            try:
                year = int(answer)
                if year < 1950 or year > 2024:
                    error_message = "\033[F\033[KInput not recognised. "\
                                    "Please enter a valid year between "\
                                    "1950 and 2024.\n"
                else:
                    return year
            except ValueError:
                error_message = "\033[F\033[KPlease enter a year as a "\
                            "4-digit number. e.g. 2004.\n"


def calculate_points(user_answer, correct_answer, clue_choice, name):
    """
    The user's answer is compared to the correct answer and the appropriate
    points are rewarded, along with a feedback message.
    """
    if user_answer == correct_answer:
        if clue_choice == 'N':
            points = 7
            feedback = f"\nYou got it {name}! And you got 2 bonus "\
                       "points for not using a clue!\n"
        else:
            points = 5
            feedback = f"\nYou got it {name}!"
    elif abs(user_answer - correct_answer) == 1:
        if clue_choice == 'N':
            points = 5
            feedback = f"So close {name}, but not quite! But you do get 2 "\
                       "bonus points for not using a clue!\n"
        else:
            points = 3
            feedback = f"\nSo close {name}, but not quite!\n"
    elif abs(user_answer - correct_answer) == 2:
        if clue_choice == 'N':
            points = 3
            feedback = f"\nNot bad {name}, but you can do better! "\
                       "But you do get 2 "\
                       "bonus points for not using a clue!\n"
        else:
            points = 1
            feedback = f"\nNot bad {name}, but you can do better!\n"
    else:
        points = 0
        feedback = f"\nSorry {name}, that's not correct.\n"
    return points, feedback


def get_user_choice():
    """
    Navigation for the user to either continue to the next question,
    return to the main menu or exit the programme.
    """
    while True:
        try:
            choice = input("Press '1' to continue playing\n"
                           "Press 'M' to return to main menu\n"
                           "Press 'E' to exit the "
                           "programme\nSelect Option: ").strip().upper()
            if choice not in ['1', 'M', 'E']:
                raise ValueError
            break
        except ValueError:
            print("Input not recognised. Please enter '1', 'M' or 'E'.")
    return choice


def end_game_get_user_choice():
    """
    Navigation for the user at the end of the quiz.
    """
    while True:
        try:
            choice = input("Press 'M' to return to main menu\n"
                           "Press 'E' to exit the "
                           "programme\nSelect Option: ").strip().upper()
            if choice not in ['M', 'E']:
                raise ValueError
            break
        except ValueError:
            print("Input not recognised. Please enter '1', 'M' or 'E'.")
    return choice


def game_summary(score, total_score, name):
    """
    Shows user their total score at the end of the game.
    """
    os.system('clear')
    print('''
    ██████╗ ███████╗███████╗██╗   ██╗██╗  ████████╗███████╗██╗
    ██╔══██╗██╔════╝██╔════╝██║   ██║██║  ╚══██╔══╝██╔════╝██║
    ██████╔╝█████╗  ███████╗██║   ██║██║     ██║   ███████╗██║
    ██╔══██╗██╔══╝  ╚════██║██║   ██║██║     ██║   ╚════██║╚═╝
    ██║  ██║███████╗███████║╚██████╔╝███████╗██║   ███████║██╗
    ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚══════╝╚═╝
    ''')
    print_slowly(f"\nCongratulations {name}, you have completed the quiz!")
    print_slowly("Let's take a look at how you got on....")
    percentage = round(score / total_score * 100)
    print_slowly(f"\nYour final score is {score} out of a "
                 f"posible {total_score}. That's {percentage}%!\n")
    print_slowly("Thanks for taking the time to play our "
                 f"quiz {name}, we hope you had fun!\n")


def play_game(name):
    """
    This function runs the game by loading questions from a JSON file,
    asking the user to guess the year a movie was released,
    and providing feedback on their answer. The function keeps track
    of the user's score, displays it at the end of the game,
    and allows the user to continue playing or return to the main menu.
    """
    score = 0
    num_of_questions = 5
    questions = load_questions()
    total_score = num_of_questions * 7
    for i, question in enumerate(questions[:num_of_questions]):
        print_question_header(i)
        title = question['title'].upper()
        print_slowly(f"\nMovie Title:   {title}\n\n")
        # get clue choice from user
        clue_choice = get_clue_choice()
        if clue_choice == 'Y':
            print_question_clue(question)
        # get answer from user
        answer = get_user_answer()
        points, feedback = calculate_points(
            answer, question['answer'], clue_choice, name)
        print(feedback)
        if answer == question['answer']:
            print_slowly(
                f"{question['title']} was indeed "
                f"released in {question['answer']}")
        else:
            print_slowly(f"{question['title']} was released"
                         f" in {question['answer']}")
        print_slowly(f"\nYou scored {points} points for this question.")
        score += points
        print_slowly(f"So far you have scored {score} points\n")
        if i == num_of_questions - 1:
            game_summary(score, total_score, name)
            end_choice = end_game_get_user_choice()
            if end_choice == 'M':
                display_main_menu(name)
            elif end_choice == 'E':
                print("Exiting program...We hope to see you again soon!")
                exit()
        choice = get_user_choice()
        if choice == '1':
            continue
        elif choice == 'M':
            display_main_menu(name)
        elif choice == 'E':
            print("Exiting program...We hope to see you again soon!")
            exit()


def display_main_menu(name):
    """
    Display main menu
    """
    os.system('clear')
    print('''
███╗   ███╗ █████╗ ██╗███╗   ██╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔══██╗██║████╗  ██║    ████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║███████║██║██╔██╗ ██║    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝
    ''')

    # loop until user chooses to exit
    menu_displayed = False

    while True:
        if not menu_displayed:
            print_slowly("\nMain Menu:\n")
            print_slowly("1. Start game")
            print_slowly("2. Quiz Guide")
            print_slowly("3. About the Developer")
            print_slowly("4. Exit program\n")
            menu_displayed = True

        # get user input
        choice = input("Select Option (1-4): ")

        # handle user choice
        if choice == '1':
            play_game(name)
            menu_displayed = False
        elif choice == '2':
            display_instructions(name)
            menu_displayed = False
        elif choice == '3':
            menu_displayed = False
        elif choice == '4':
            print("Exiting program...We hope to see you again soon!")
            exit()
        else:
            print("Invalid choice, please enter a number from 1 to 4.")


def display_instructions(name):
    """
    Displays instructions on how to play the game
    """
    os.system('clear')
    print('''

 ██████╗ ██╗   ██╗██╗███████╗     ██████╗ ██╗   ██╗██╗██████╗ ███████╗
██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝ ██║   ██║██║██╔══██╗██╔════╝
██║   ██║██║   ██║██║  ███╔╝     ██║  ███╗██║   ██║██║██║  ██║█████╗
██║▄▄ ██║██║   ██║██║ ███╔╝      ██║   ██║██║   ██║██║██║  ██║██╔══╝
╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝╚██████╔╝██║██████╔╝███████╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝  ╚═════╝ ╚═╝╚═════╝ ╚══════╝
    ''')
    print_slowly("************* THE AIM OF THE GAME ************\n".center(80))
    print("The aim of the game is to correctly guess the".center(80))
    print("release date of the movie.".center(80))
    print("Simple! (if you know the answer that is...)\n\n".center(80))
    print_slowly("*************** THE QUIZ FORMAT **************\n".center(80))
    print("When the quiz first begins you will see the name".center(80))
    print("of the movie. You will be invited to choose".center(80))
    print("to see a clue or not. Once you have made your ".center(80))
    print("choice you will be invited to guess the answer.\n".center(80))
    print("Once you have entered your answer you will see".center(80))
    print("if you were correct, the number of points scored,".center(80))
    print("and your total score so far. Once you have".center(80))
    print("answered 5 questions you will be taken to".center(80))
    print("the quiz summary screen and you can review".center(80))
    print("how well you did.\n\n".center(80))
    print_slowly("*************** HOW CLUES WORK ***************\n".center(80))
    print("Before you guess the year the movie was released".center(80))
    print("you will be asked if you want to see a clue.".center(80))
    print("You'll need to enter either 'Y' (yes) or 'N' (no)\n".center(80))
    print("All clues give you a good hint as to when the movie".center(80))
    print("was released. For example, if a movie was released in".center(80))
    print("2002 the clue would be 'Released in early 2000s'\n\n".center(80))
    print_slowly("******* HOW THE POINTS ARE CALCULATED ********\n".center(80))
    print("Enter the correct answer, you are receive 5 points.\n".center(80))
    print("If you are 1 year off the correct answer, you receive".center(80))
    print(" with 3 points.\n".center(80))
    print("If you are 2 years off the correct answer, you receive".center(80))
    print("with 1 point.\n".center(80))
    print("If you are 3 or more years away from the ".center(80))
    print("correct answer, you get 0 points.\n".center(80))
    print("If you guess within 2 years of the release date and".center(80))
    print("don't use a clue, you receive an additional 2 points.\n".center(80))
    print("You will be asked 5 questions, so the maximum".center(80))
    print("possible score is 35 points.".center(80))
    while True:
        choice = input("\nEnter '1' to return to the main menu: ")
        if choice.lower() == '1':
            display_main_menu(name)  # display the main menu again
            break


def landing_page():
    print('''
    ████████╗██╗  ██╗███████╗    ███╗   ███╗ ██████╗ ██╗   ██╗██╗███████╗
    ╚══██╔══╝██║  ██║██╔════╝    ████╗ ████║██╔═══██╗██║   ██║██║██╔════╝
       ██║   ███████║█████╗      ██╔████╔██║██║   ██║██║   ██║██║█████╗
       ██║   ██╔══██║██╔══╝      ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██║██╔══╝
       ██║   ██║  ██║███████╗    ██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ██║███████╗
       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚══════╝
                         ██████╗ ██╗   ██╗██╗███████╗██╗
                        ██╔═══██╗██║   ██║██║╚══███╔╝██║
                        ██║   ██║██║   ██║██║  ███╔╝ ██║
                        ██║▄▄ ██║██║   ██║██║ ███╔╝  ╚═╝
                        ╚██████╔╝╚██████╔╝██║███████╗██╗
                         ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚═╝
    ''')
    print("Hello and welcome to The Movie Quiz!".center(80))
    print("")
    print_slowly("The Quiz where your knowledge of movies and,".center(80))
    print_slowly("when they were released is put to the test!".center(80))
    print("")
    print("What is your name? ".center(80))
    name = input("\n ".center(76)).capitalize()
    print("")
    print(f"Welcome {name}!".center(80))
    print("")
    print_slowly("We have an impressive archive of over 135 movies".center(80))
    print_slowly("to test your knowledge, so with 5 questions ".center(80))
    print_slowly("per quiz, you are sure to have a varried".center(80))
    print_slowly("experience, everytime you play!".center(80))

    while True:
        choice = input(f"\n{name}, when ready,"
                       " press '1' then 'Enter' to head over to the"
                       " main menu: ".center(80))
        if choice.lower() == '1':
            display_main_menu(name)  # display the main menu again
            break
    return name


landing_page()
import json
import random
import os


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
    print("***************************************************")
    print("*                Guess The Year                   *")
    print("*                   the Movie                     *")
    print("*                 was Released!                   *")
    print("***************************************************\n")
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
    print(f"\nClue: {question['clue']}\n\n\n")


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


def calculate_points(user_answer, correct_answer, clue_choice):
    """
    The user's answer is compared to the correct answer and the appropriate
    points are rewarded, along with a feedback message.
    """
    if user_answer == correct_answer:
        if clue_choice == 'N':
            points = 7
            feedback = "\nYou got it! And you got 2 bonus "\
                       "points for not using a clue!\n"
        else:
            points = 5
            feedback = "\nYou got it!"
    elif abs(user_answer - correct_answer) == 1:
        if clue_choice == 'N':
            points = 5
            feedback = "\nClose, but not quite! But you do get 2 "\
                       "bonus points for not using a clue!\n"
        else:
            points = 3
            feedback = "\nClose, but not quite!\n"
    elif abs(user_answer - correct_answer) == 2:
        if clue_choice == 'N':
            points = 3
            feedback = "\nNot bad, but you can do better! But you do get 2 "\
                       "bonus points for not using a clue!\n"
        else:
            points = 1
            feedback = "\nNot bad, but you can do better!\n"
    else:
        points = 0
        feedback = "\nSorry, that's not correct.\n"
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


def game_summary(score, total_score):
    """
    Shows user their total score at the end of the game.
    """
    os.system('clear')
    print("***************************************************")
    print("*          MOVIE RELEASE-DATE QUIZ                *")
    print("*                  RESULTS!                       *")
    print("*          Let's see how you got on!              *")
    print("***************************************************")
    print("\nCongratulations you have completed the quiz!")
    print("Let's take a look at how you got on....")
    percentage = round(score / total_score * 100)
    print(f"\nYour final score is {score} out of a "
          f"posible {total_score}. That's {percentage}%!\n")
    print("Thanks for taking the time to play our "
          "quiz, we hope you have fun!\n")


def play_game():
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
        print(f"\nMovie Title:   {title}\n")
        print("")
        # get clue choice from user
        clue_choice = get_clue_choice()
        if clue_choice == 'Y':
            print_question_clue(question)
        # get answer from user
        answer = get_user_answer()
        points, feedback = calculate_points(
            answer, question['answer'], clue_choice)
        print(feedback)
        if answer == question['answer']:
            print(
                f"{question['title']} was indeed "
                f"released in {question['answer']}")
        else:
            print(f"{question['title']} was released in {question['answer']}")
        print(f"\nYou scored {points} points for this question.")
        score += points
        print(f"So far you have scored {score} points\n")
        get_user_choice()
        if i == num_of_questions - 1:
            game_summary(score, total_score)
            end_game_get_user_choice()


def display_main_menu():
    """
    Display main menu
    """
    os.system('clear')
    print("***************************************************")
    print("*          MOVIE RELEASE-DATE QUIZ                *")
    print("*        Movies from the 60s to 2022              *")
    print("*          How many will you know!?               *")
    print("***************************************************")

    # loop until user chooses to exit
    while True:
        print("\nMain Menu:\n")
        print("1. Start game")
        print("2. Quiz Guide")
        print("3. About the Developer")
        print("4. Exit program\n")

        # get user input
        choice = input("Select Option (1-4): ")

        # handle user choice
        if choice == '1':
            print("Starting game...good luck!")
            play_game()
        elif choice == '2':
            print("Opening Instructions...")
            display_instructions()
        elif choice == '3':
            print("Displaying help...")
        elif choice == '4':
            print("Exiting program...")
            exit()
        else:
            print("Invalid choice, please enter a number from 1 to 4.")


def display_instructions():
    """
    Displays instructions on how to play the game
    """
    os.system('clear')
    print("***************************************************")
    print("*                                                 *")
    print("*                QUIZ GUIDE                       *")
    print("*                                                 *")
    print("***************************************************")
    print("\n\n******** THE AIM OF THE GAME! ********\n\n")
    print("The aim of the game is to correctly guess the release date"
          " of the movie. Simple! (if you know the answer that is...)")
    print("\n\n******** THE QUIZ FORMAT ********\n\n")
    print("When the quiz first begins you will see the name of the movie,"
          " and you will be invited to choose to see a clue or not. Once"
          " you have made your choice you will be invited to guess the"
          " answer. Once you have entered your answer you will see"
          " if you were correct, the number of points scored, and your"
          " total score so far. Once you have answered 5 questions"
          " you will be taken to the quiz summary screen and you can review"
          " how well you did.\n")

    print("\n\n******** HOW CLUES WORK ********\n\n")
    print("Before you guess the year the movie was released"
          " you will be asked if you want to see a clue."
          " You'll need to enter either 'Y' (yes) or 'N' (no)")
    print("\nAll clues give you a good hint as to when the movie"
          " was released. For example, if a movie was released in"
          " 2002 then the clue would be 'Released in early 2000s'")
    print("\n\n******** HOW THE POINTS ARE CALCULATED ********\n\n")
    print("If you enter the correct answer, you are rewarded 5 points.\n")
    print("If you are 1 year off the correct answer, you are rewarded"
          " with 3 points.\n")
    print("If you are 2 years off the correct answer, you are rewarded"
          " with 1 point.\n")
    print("If you are 3 or more years away from the "
          "correct answer, you get 0 points.\n")
    print("If you guess within 2 years of the release date and"
          "don't use the clue option, you receive an additional 2 points.\n")
    print("You will be asked 5 questions, so the maximum"
          "possible score is 35 points.\n")
    while True:
        choice = input("\nEnter '1' to return to the main menu: ")
        if choice.lower() == '1':
            display_main_menu()  # display the main menu again
            break


def landing_page():
    name = input("Hello there! Great to see you here with us today."
                 "What's your name? ")
    print(f"Welcome {name}!")
    while True:
        choice = input("\nEnter '1' to head over to the main menu: ")
        if choice.lower() == '1':
            display_main_menu()  # display the main menu again
            break


landing_page()
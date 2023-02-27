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
    clue_choice = input("\nWould you like a clue? (y or n): ").strip().lower()
    while clue_choice not in ['y', 'n']:
        print("Input not recognised. Please enter 'y' or 'n'.")
        clue_choice = input("\nWould you like a clue? (y or n): ").lower()
    return clue_choice


def print_question_clue(question):
    """
    Prints the clue for the user when they ask for a clue.
    """
    print(f"Clue: {question['clue']}")


def get_user_answer():
    """
    User inputs their answer into the terminal.
    """
    while True:
        print("")
        answer = input("Guess the year (4 digits): ").strip()
        if len(answer) != 4:
            print("Please enter a 4-digit year.")
            print("")
            continue
        try:
            year = int(answer)
            if year < 1950 or year > 2025:
                print("Input not recognised. Please enter a valid year.")
                continue
            return year
        except ValueError:
            print("Please enter a valid year.")
            continue


def calculate_points(user_answer, correct_answer, clue_choice):
    """
    The user's answer is compared to the correct answer and the appropriate
    points are rewarded, along with a feedback message.
    """
    if user_answer == correct_answer:
        if clue_choice == 'n':
            points = 7
            feedback = "You got it! And you got 2 bonus points for not using a clue!"
        else:
            points = 5
            feedback = "You got it!"
    elif abs(user_answer - correct_answer) == 1:
        if clue_choice == 'n':
            points = 5
            feedback = "Close, but not quite! But you do get 2 bonus points for not using a clue!"
        else:
            points = 3
            feedback = "Close, but not quite!"
    elif abs(user_answer - correct_answer) == 2:
        if clue_choice == 'n':
            points = 3
            feedback = "Not bad, but you can do better! But you do get 2 bonus points for not using a clue!"
        else:
            points = 1
            feedback = "Not bad, but you can do better!"
    else:
        points = 0
        feedback = "Sorry, that's not correct."
    return points, feedback


def get_user_choice():
    """
    Navigation for the user to either continue to the next question, 
    return to the main menu or exit the programme.
    """
    choice = input("Press '1' to continue playing, press 'm' to return to main menu or press 'e' to exit the programme: ").strip().lower()
    while choice not in ['1', 'm', 'e']:
        print("Input not recognised. Please enter '1', 'm' or 'e'.")
        choice = input("Press '1' to continue playing, press 'm' to return to main menu or press 'e' to exit the programme: ").strip().lower()
    return choice


def game_summary(score, total_score):
    """
    Shows user their total score at the end of the game.
    """
    os.system('clear')
    percentage = round(score / total_score * 100)
    print("\nCongratulations! You have completed the game.")
    print(f"Your final score is: {score} out of {total_score}.")
    print(f"That's {percentage}%!")


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
        print(f"\n    Movie Title:   {title}")

        clue_choice = get_clue_choice()
        if clue_choice == 'y':
            print_question_clue(question)

        answer = get_user_answer()
        points, feedback = calculate_points(answer, question['answer'], clue_choice)
        print(feedback)
        if answer == question['answer']:
            print(f"{question['title']} was indeed released in {question['answer']}")
        else:
            print(f"{question['title']} was released in {question['answer']}")

        print(f"You scored {points} points for this question.")
        score += points
        print(f"Your score so far is: {score}\n")
        if i == num_of_questions - 1:
            game_summary(score, total_score)
        get_user_choice()
    

# display main menu
def display_main_menu():
    print("***************************************************")
    print("*                                                 *")
    print("*          MOVIE RELEASE-DATE QUIZ                *")
    print("*                                                 *")
    print("***************************************************")

    # loop until user chooses to exit
    while True:
        print("\nPlease choose an option:")
        print("1. Start game")
        print("2. How to play")
        print("3. Help")
        print("4. Exit program")

        # get user input
        choice = input("Enter option number (1-4): ")

        # handle user choice
        if choice == '1':
            print("Starting game...")
            play_game()
        elif choice == '2':
            display_instructions()  # call function to display instructions "page"
        elif choice == '3':
            print("Displaying help...")
            # TODO: add help information here
        elif choice == '4':
            print("Exiting program...")
            exit()  # exit the while loop
        else:
            print("Invalid choice, please enter a number from 1 to 4.")

# display instructions "page"
def display_instructions():
    os.system('clear')
    print("***************************************************")
    print("*                                                 *")
    print("*                INSTRUCTION                      *")
    print("*                                                 *")
    print("***************************************************")
    print("")
    print("1. You will be shown a movie title, and you need to guess the year it was released.")
    print("")
    print("2. If you guess correctly, you get 5 points.")
    print("")
    print("3. If you are 1 year off the correct answer, you get 3 points.")
    print("")
    print("4. If you are 2 years off the correct answer, you get 1 point.")
    print("")
    print("5. If you are 3 or more years away from the correct answer, you get 0 points.")
    print("")
    print("6. If you guess within 2 years of the release date and don't use the clue option, you receive an additional 2 points.")
    print("")
    print("7. You will be asked 10 questions, so the maximum possible score is 70 points.")
    
    # loop until user navigates back to main menu
    while True:
        choice = input("\nEnter '1' to return to the main menu: ")
        if choice.lower() == '1':
            display_main_menu()  # display the main menu again
            break


# call the main menu function to start the program
display_main_menu()

import os
import random

# function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# function to play the game
def play_game():

    questions = [
        {
            "title": "The Shawshank Redemption",
            "clue": "Released in the early 90s",
            "answer": 1994,
            "score": 0
        },
        {
            "title": "The Godfather",
            "clue": "Released in the early 70s",
            "answer": 1972,
            "score": 0
        },
        {
            "title": "The Dark Knight",
            "clue": "Released in the late 2000s",
            "answer": 2008,
            "score": 0
        },
        {
            "title": "Forrest Gump",
            "clue": "Released in the mid 90s",
            "answer": 1994,
            "score": 0
        },
        {
            "title": "Inception",
            "clue": "Released in the early 2010s",
            "answer": 2010,
            "score": 0
        },
        {
            "title": "The Matrix",
            "clue": "Released in the late 90s",
            "answer": 1999,
            "score": 0
        },
        {
            "title": "Goodfellas",
            "clue": "Released in the early 90s",
            "answer": 1990,
            "score": 0
        },
        {
            "title": "The Silence of the Lambs",
            "clue": "Released in the early 90s",
            "answer": 1991,
            "score": 0
        },
        {
            "title": "Pulp Fiction",
            "clue": "Released in the mid 90s",
            "answer": 1994,
            "score": 0
        },
        {
            "title": "The Lord of the Rings: The Return of the King",
            "clue": "Released in the early 2000s",
            "answer": 2003,
            "score": 0
        }
    ]


    print("Guess The Year the Film was Released!")
    score = 0
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1} of {len(questions)}:")
        print(question['title'])
        print("")
        clue_choice = input("Would you like a clue? (y or n): ")
        while clue_choice.lower() not in ['y', 'n']:
            print("Input not recognised. Please enter 'y' or 'n'.")
            clue_choice = input("Would you like a clue? (y or n): ")
            print("")
        if clue_choice.lower() == 'y':
            print(f"Clue: {question['clue']}")
        answer = int(input("Guess the year: "))
        if answer == question['answer']:
            if abs(answer - question['answer']) <= 1 and clue_choice.lower() == 'n':
                score += 7
                print("You got it! And with a bonus of 2 points for being correct and not using a clue!")
            else:
                score += 5
                print("You got it!")
        elif abs(answer - question['answer']) == 1:
            if clue_choice.lower() == 'n':
                score += 3
                print("Close, but not quite! But you do get 2 bonus points for not using a clue!")
            else:
                print("Close, but not quite!")
        elif abs(answer - question['answer']) == 2:
            if clue_choice.lower() == 'n':
                score += 1
                print("Not bad, but you can do better! But you do get 2 bonus points for not using a clue!")
            else:
                print("Not bad, but you can do better!")
        else:
            print("Sorry, that's not correct.")
            print(f"The correct answer is: {question['answer']}")
        print(f"You scored {score - sum([q['score'] for q in questions[:i]])} points for this question.")
        print(f"Your score so far is: {score}")
        print("")
        choice = input("Press '1' to continue playing, press 'm' to return to main menu or press 'e' to exit the programme: ")
        while choice.lower() not in ['1', 'm', 'e']:
            print("Input not recognised. Please enter '1', 'm' or 'e'.")
            choice = input("Press '1' to continue playing, press 'm' to return to main menu or press 'e' to exit the programme: ")
        if choice.lower() == 'm':
            return
        elif choice.lower() == 'e':
            exit()
    print("\nCongratulations! You have completed the game.")
    print(f"Your final score is: {score}")


# display main menu
def display_main_menu():
    print("***************************************************")
    print("*                                                 *")
    print("*               WELCOME TO MY GAME                *")
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
            break  # exit the while loop
        else:
            print("Invalid choice, please enter a number from 1 to 4.")

# display instructions "page"
def display_instructions():
    clear_console()  # clear the console
    print("INSTRUCTIONS:")
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
    print("7. You will be asked 10 questions, so the maximum possible score is 60 points.")
    
    # loop until user navigates back to main menu
    while True:
        choice = input("\nEnter '1' to return to the main menu: ")
        if choice.lower() == '1':
            clear_console()  # clear the console
            display_main_menu()  # display the main menu again
            break

# call the main menu function to start the program
display_main_menu()

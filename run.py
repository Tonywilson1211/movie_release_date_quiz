import json
import random


def play_game():
    with open('movies.json', 'r') as f:
        questions = json.load(f)
    random.shuffle(questions)
    print("Guess The Year the Film was Released!")
    score = 0
    for i, question in enumerate(questions[:5]):
        print(f"\nQuestion {i+1} of 5:")
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
            if clue_choice.lower() == 'n':
                points = 7
                print("You got it! And you got 2 bonus points for not using a clue!")
                print(f"The movie was indeed released in: {question['answer']}")
            else:
                points = 5
                print("You got it!")
                print(f"The movie was indeed released in: {question['answer']}")
        elif abs(answer - question['answer']) == 1:
            if clue_choice.lower() == 'n':
                points = 5
                print("Close, but not quite! But you do get 2 bonus points for not using a clue!")
                print(f"The correct answer is: {question['answer']}")
            else:
                points = 3
                print("Close, but not quite!")
                print(f"The correct answer is: {question['answer']}")
        elif abs(answer - question['answer']) == 2:
            if clue_choice.lower() == 'n':
                points = 3
                print("Not bad, but you can do better! But you do get 2 bonus points for not using a clue!")
                print(f"The correct answer is: {question['answer']}")
            else:
                points = 1
                print("Not bad, but you can do better!")
                print(f"The correct answer is: {question['answer']}")
        else:
            print("Sorry, that's not correct.")
            points = 0
            print(f"The correct answer is: {question['answer']}")
        print(f"You scored {points} points for this question.")
        score += points
        print(f"Your score so far is: {score}")
        print("")
        if i == 9:
            percentage = round(score/70*100, 2)
            print("\nCongratulations! You have completed the game.")
            print(f"Your final score is: {score} out of 70.")
            print(f"That's {percentage}%!")
            return
        else:
            choice = input("Press '1' to continue playing, press 'm' to return to main menu or press 'e' to exit the programme: ")
            while choice.lower() not in ['1', 'm', 'e']:
                print("Input not recognised. Please enter '1', 'm' or 'e'.")
                choice = input("Press '1' to continue playing, press 'm' to return to main menu or press 'e' to exit the programme: ")
            if choice.lower() == 'm':
                return
            elif choice.lower() == 'e':
                exit()


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
    print("7. You will be asked 10 questions, so the maximum possible score is 70 points.")
    
    # loop until user navigates back to main menu
    while True:
        choice = input("\nEnter '1' to return to the main menu: ")
        if choice.lower() == '1':
            display_main_menu()  # display the main menu again
            break

# call the main menu function to start the program
display_main_menu()

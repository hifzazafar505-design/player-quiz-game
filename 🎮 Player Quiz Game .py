# 📑 Is project mein aap use karenge:

# 📚 Concepts          | 🎯 Features

# Variables            | ▶️ Start Quiz
# Input                | 📋 Show Questions
# Lists                | 📊 Show Score
# Dictionary           | 🚪 Exit
# Loops
# Functions
# Conditions

# ======================================
# 🎮 Player Quiz Game
# ======================================

# Score Variable
Score = 0

# ======================================
# 📂 Question List
# --------------------------
Questions = [

    {
        "Question": "What is the capital of Pakistan?",
        "Answer": "Islamabad"
    },

    {
        "Question": "2 + 2 = ?",
        "Answer": "4"
    },

    {
        "Question": "Python is a ______ language.",
        "Answer": "Programming"
    }

]

# --------------------------
# 📋 Show Questions Function
# --------------------------
def Show_Question():

    if len(Questions) == 0:

        print("No Questions Found!")

    else:

        count = 1

        for Question in Questions:

            print("Question", count)

            print(Question["Question"])

            count += 1


# --------------------------
# ▶️ Start Quiz Function
# --------------------------
def Start_Quiz():

    global Score

    Score = 0

    for Question in Questions:

        print()

        print(Question["Question"])

        User_Answer = input("Enter your Answer: ")

        if User_Answer.lower() == Question["Answer"].lower():

            print("Correct Answer!")

            Score += 1

        else:

            print("Wrong Answer!")

            print("Correct Answer is:", Question["Answer"])


# --------------------------
# 📊 Show Score Function
# --------------------------
def Show_Score():

    print()

    print("Your Score is:", Score)

    print("Total Questions:", len(Questions))


while True:

    print()
    print("1. Show Questions")
    print("2. Start Quiz")
    print("3. Show Score")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Show_Question()

    elif choice == "2":
        Start_Quiz()

    elif choice == "3":
        Show_Score()

    elif choice == "4":
        print("Thanks for Playing!")
        break

    else:
        print("Invalid Choice!")
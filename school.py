import time
import os

PASS_SCORE = 35

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# -----------------------------
# Generic Quiz Engine
# -----------------------------
def run_quiz(title, questions):
    """
    title: name of the class
    questions: list of dicts:
        {
            "prompt": "text",
            "answer": correct_answer (string or int),
            "points": 10
        }
    """

    score = 0
    print(f"Welcome to {title} class!")
    print("\nYou will be given 5 questions worth 10 points each.")
    print("You need at least 35 points to pass.")
    ready = input("Are you ready? (y/n) ")

    if ready.lower() != "y":
        choice = input("\nOk. Would you like to {e}xit or {s}witch classes: ")
        if choice == "s":
            clear()
            mainProgram()
        else:
            print("Now exiting...")
            time.sleep(2)
        return

    print("\nGetting Ready...")
    time.sleep(2)
    clear()

    # Ask each question
    for q in questions:
        user_input = input(q["prompt"] + " ")

        # Convert to int if needed
        if isinstance(q["answer"], int):
            try:
                user_input = int(user_input)
            except:
                user_input = None
        else:
            user_input = user_input.lower().strip()

        # Check correctness
        if user_input == q["answer"]:
            score += q["points"]
        else:
            score -= 5

    # Summary
    clear()
    print(f"--- {title} Summary ---")
    print(f"Final Score: {score}")

    if score >= PASS_SCORE:
        print("Status: PASS")
    else:
        print("Status: FAIL")

    # Retry option
    retry = input("\nWould you like to retry this class? (y/n) ")
    if retry.lower() == "y":
        clear()
        run_quiz(title, questions)
        return

    print("\nReturning to main program...")
    time.sleep(2)
    clear()
    mainProgram()


# -----------------------------
# Class Question Sets
# -----------------------------

def algebra():
    questions = [
        {"prompt": "Solve: 2x = 10:", "answer": 5, "points": 10},
        {"prompt": "Solve: x + 7 = 12:", "answer": 5, "points": 10},
        {"prompt": "Solve: 3x = 21:", "answer": 7, "points": 10},
        {"prompt": "Solve: x - 4 = 6:", "answer": 10, "points": 10},
        {"prompt": "Solve: 5x = 25:", "answer": 5, "points": 10},
    ]
    run_quiz("Algebra", questions)


def english():
    happySynonym = [
        "glad","joyful","cheerful","content","pleased","elated","overjoyed",
        "thrilled","ecstatic","delighted","serene","satisfied","fulfilled",
        "at ease","giddy","buoyant","sunny","upbeat","jubilant","festive","merry"
    ]

    questions = [
        {"prompt": "Synonym of 'happy':", "answer": happySynonym, "points": 10},
        {"prompt": "Antonym of 'big':", "answer": "small", "points": 10},
        {"prompt": "Plural of 'child':", "answer": "children", "points": 10},
        {"prompt": "Correct spelling (recieve or receive):", "answer": "receive", "points": 10},
        {"prompt": "Opposite of 'fast':", "answer": "slow", "points": 10},
    ]

    # Special handling: allow list answers
    for q in questions:
        if isinstance(q["answer"], list):
            correct_list = q["answer"]
            q["answer"] = correct_list  # keep list

    run_quiz("English", questions)


def oceanography():
    questions = [
        {"prompt": "What is the largest ocean:", "answer": "pacific", "points": 10},
        {"prompt": "Salt water covers about what % of the earth:", "answer": 70, "points": 10},
        {"prompt": "What is the world's deepest trench:", "answer": "mariana", "points": 10},
        {"prompt": "What do sea animals breathe with:", "answer": "gills", "points": 10},
        {"prompt": "Which tool is used to measure water depth:", "answer": "sonar", "points": 10},
    ]
    run_quiz("Oceanography", questions)


def history():
    questions = [
        {"prompt": "First US President:", "answer": "george washington", "points": 10},
        {"prompt": "Where is the Great Wall located:", "answer": "china", "points": 10},
        {"prompt": "When did the US gain independence:", "answer": 1776, "points": 10},
        {"prompt": "When did the Civil War end:", "answer": 1865, "points": 10},
        {"prompt": "Where are the Pyramids located:", "answer": "egypt", "points": 10},
    ]
    run_quiz("History", questions)


def health():
    questions = [
        {"prompt": "How many bones are in the adult body:", "answer": 206, "points": 10},
        {"prompt": "Which organ pumps blood throughout the body:", "answer": "heart", "points": 10},
        {"prompt": "What does BMI stand for:", "answer": "body mass index", "points": 10},
        {"prompt": "What are muscles connected by:", "answer": "tendons", "points": 10},
        {"prompt": "What do we breathe in:", "answer": "oxygen", "points": 10},
    ]
    run_quiz("Health", questions)


# -----------------------------
# Main Program
# -----------------------------
def mainProgram():
    print("Welcome to JANOS Academy!")
    print("\nClasses Available:")
    print("(1) Algebra")
    print("(2) English")
    print("(3) Oceanography")
    print("(4) History")
    print("(5) Health")
    print("(-1) Exit")

    choice = input("\nChoose a class number: ")

    if not choice.isdigit() and choice != "-1":
        clear()
        print("Invalid input.")
        return mainProgram()

    choice = int(choice)

    clear()

    match choice:
        case 1: algebra()
        case 2: english()
        case 3: oceanography()
        case 4: history()
        case 5: health()
        case -1:
            print("Goodbye!")
            time.sleep(1)
        case _:
            print("Invalid choice.")
            time.sleep(1)
            clear()
            mainProgram()


mainProgram()

import random

# Define the set of questions and their answers
questions = {
    "Which Coding Language is Best?": "Python",
    "Which Framework is Best?": "Django",
    "Is Python is Best Language?": "Yes"
}

# Define the set of weapons
weapons = ["Machine gun", "Strom Breaker", "Power Stone"]

# Define the set of keys
keys = ["Gold key", "Silver key", "Bronze key"]

# Define the villain and their weakness
villain = {
    "name": "Thanos",
    "weakness": "Strom Breaker"
}

# Define the starting level and number of lives
level = 1
lives = 3

# Define a function to ask the user a question

def ask_question():
    question = random.choice(list(questions.keys()))
    answer = input(question + "\n")
    if answer.lower() == questions[question].lower():
        print("Correct!")
        pick_weapon()
    else:
        print("Incorrect! You lost a life.")
        global lives
        lives -= 1
        if lives == 0:
            print("Game over.")
            quit()
# function to pick a weapon
def pick_weapon():
    weapon = input("Pick a weapon from the following: " + ", ".join(weapons) + "\n")
    if weapon in weapons:
        print("You picked up a " + weapon + "!")
        pick_key()
    else:
        print("Invalid choice! Pick again.")
        pick_weapon()

# function to pick a key
def pick_key():
    key = input("Pick a key from the following: " + ", ".join(keys) + "\n")
    if key in keys:
        print("You picked up a " + key + "!")
        open_door(key)
    else:
        print("Invalid choice! Pick again.")
        pick_key()


# open the door
def open_door(key):
    if key == "Gold key":
        print("You opened the door!")
        global level
        level += 1
        if level == 2:
            print("Welcome to level 2. You gained an extra life!")
            global lives
            lives += 1
            fight_villain()
        else:
            print("Congratulations! You beat the game.")
            quit()
    else:
        print("The key didn't work. Pick another.")
        pick_key()

# function to fight the Thanos
def fight_villain():
    weapon = input("The " + villain["name"] + " has appeared! Pick a weapon: " + ", ".join(weapons) + "\n")
    if weapon == villain["weakness"]:
        print("You defeated the " + villain["name"] + " with your " + weapon + "!")
        ask_question_level2()
    else:
        print("Your weapon is not good. Pick another.")
        fight_villain()

# Ask the user a question in level 2
def ask_question_level2():
    question = random.choice(list(questions.keys()))
    answer = input(question + "\n")
    if answer.lower() == questions[question].lower():
        print("Congratulations! You Complete  the game.")
		Print("Thank you")
        quit()
    else:
        print("Incorrect! Try again.")
        ask_question_level2()

# Start the game
print("Welcome to the game. You have " + str(lives) + " lives.")
ask_question()

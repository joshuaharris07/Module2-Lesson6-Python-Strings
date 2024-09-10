# User Input Data Processor
# Objective: The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

def check_username():
    while True:
        username = input("Please enter your first and last name: ")
        split_username = username.split()
        if len(split_username) < 2: 
            print("Please enter both your first and last name.")
        else:
            for name in split_username:
                if len(name) < 2:
                    print("Please enter your full name, not just the initial.")
                    break
                elif split_username[-1] and len(name) > 1:
                    print(f"Thank you for putting in your name, {username}.")
                    return
        
check_username()
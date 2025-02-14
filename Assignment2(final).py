import hashlib


def main():
    print("Welcome to the Quiz Program!")
   
    while True:
        usrIpt = int(input('''Enter operation by selecting a number:
                1. Register
                2. Login
                3. Attempt Quiz
                4. Show Result
                5. Exit
                '''))

        if usrIpt == 1:
            register()
        elif usrIpt == 2:
            login()
        elif usrIpt == 3:
            attempt_quiz()
        elif usrIpt == 4:
            show_result()
        elif usrIpt == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Please enter a valid input number.")

# Utility function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Get the last ID from the file or start from 1
def get_last_id():
    try:
        with open('user.txt', 'r') as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                last_id = int(last_line.split()[0])
                return last_id
            else:
                return 0
    except (FileNotFoundError, IndexError, ValueError):
        return 0

def register():
    with open('user.txt', 'a') as users:
        user_id = get_last_id() + 1  

        while True:
            userInpt = input("Enter name: ")
            if len(userInpt) < 3:
                print("Name must be at least 3 characters.")
            else: 
                break

        while True:
            pwt = input("Enter password: ")
            if len(pwt) < 4:
                print("Password must be at least 4 characters.")
            else:
                hashed_pwt = hash_password(pwt)
                break

        while True:
            age = input("Enter your age in dd/mm/yy format: ")
            if len(age) < 8:
                print("Enter age properly in the format dd/mm/yy.")
            else: 
                break

        # Save user data
        users.write(f"{user_id} {userInpt} {hashed_pwt} {age}\n")
        print("User information saved successfully.")

def login():
    try:
        with open("user.txt", 'r') as users:
            found_line = None

            while True: 
                user_id = input("Enter user ID: ")
                found_line = None  

                users.seek(0)

                for line in users:
                    if line.startswith(f"{user_id} "):
                        found_line = line.strip()
                        break

                if found_line:
                    print("User ID found, proceeding to password check.")
                    stored_id, stored_user, stored_password, *_ = found_line.split()
                    pwt = input("Enter password: ")

                    if hash_password(pwt) == stored_password:
                        print("Login successful!")
                        return True
                    else:
                        print("Incorrect password. Please try again.")
                        return False
                else:
                    print("User ID not found. Please try again or register.")
                    continue

    except FileNotFoundError:
        print("No user records found. Please register first.")
        return False

def attempt_quiz():
    print("Quiz started!")
    questions = {
        "What is the time complexity of binary search? (a) O(n) (b) O(log n) (c) O(n^2)": "b",
        "Which data structure uses LIFO? (a) Queue (b) Stack (c) Linked List": "b",
        "Python is a type of: (a) Compiled language (b) Interpreted language (c) Both": "b"
    }
    score = 0

    for question, correct_ans in questions.items():
        answer = input(question + "\n").lower()
        if answer == correct_ans:
            score += 1

    with open("results.txt", "a") as results:
        results.write(f"User scored {score}/{len(questions)}\n")

    print(f"You scored {score}/{len(questions)}")

def show_result():
    try:
        with open("results.txt", "r") as results:
            print("Results:")
            for line in results:
                print(line.strip())
    except FileNotFoundError:
        print("No results found.")


main()
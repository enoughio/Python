print("""1 -> Registration
2 -> Login       
3 -> Forgot Password
4 -> Exit the service """)

user_names = []  # List of user names (for convenience, can be removed if unnecessary)
user_emails = []  # List of emails (for convenience, can be removed if unnecessary)
users_credentials = {("name.example", "email.example"): "password.example"}  # Dictionary with tuple keys


while True:
    user_choice = input("Enter your choice: ")

    if user_choice == '1':  # Registration
        name = input("Enter your username: ")
        email = input("Enter your email address: ")

        # Check if user already exists
        if any(email == user[1] for user in users_credentials.keys()):
            print("Email already registered. Please use another email.")
            continue

        if any(name == user[0] for user in users_credentials.keys()):
            print("Username already taken. Please use another username.")
            continue

        password = input("Enter your password: ")
        users_credentials[(name, email)] = password
        print("Registered successfully!")

    elif user_choice == '2':  # Login
        name_or_email = input("Enter your username or email: ")

        # Try to find the user by either username or email
        user_found = None
        for (name, email), stored_password in users_credentials.items():
            if name_or_email == name or name_or_email == email:
                user_found = (name, email)
                break

        if user_found:
            password = input("Enter your password: ")
            if password == users_credentials[user_found]:
                print("User logged in successfully!")
            else:
                print("Incorrect password.")
        else:
            print("Invalid username or email.")

    elif user_choice == '3':  # Forgot Password
        email = input("Enter your email address: ")

        # Try to find the user by email
        user_found = None
        for (name, email_key), stored_password in users_credentials.items():
            if email == email_key:
                user_found = (name, email_key)
                break

        if user_found:
            print(f"Your password is: {users_credentials[user_found]}")
        else:
            print("Email not found.")

    elif user_choice == '4':  # Exit
        print("Exiting the service. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option (1-4).")

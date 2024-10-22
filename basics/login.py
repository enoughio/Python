print("""1 -> Registration
         2 -> Login       
         3 -> Forgot Password
         4 -> Exit the service """)


user_names = [] # list of user names
user_emails = [] #list of emails
users_credientials = {("name.example, email.example"): "password.example"} # Dictionary with tuple keys


user_choice = input("Enter your choice")

if user_choice == '1':
        name = input("Enter your username: ")
        password =  input("Enter your password: ")
        email = input("Enter your email address: ")
        # user_names.append(name)
        users_credientials[(name, email)] = {password}
        print("registered successfully")

elif ( user_choice == '2'):

    nameoremail = input("Enter your username or email: ").lower().split()

    first = users_credientials.keys()  # thiis will give a list 

    if nameoremail in first[0] or nameoremail in first[1]:  # if (email, name) in auth_dict and auth_dict[(email, name)] == password
          password = input("enter you password")
          if(password == users_credientials[]):
                print("user loged in succesfully")
          else:
                print("wrong password")

    else:
        print("invalid username or email")


elif user_choice == '3':
elif user_choice == '4':

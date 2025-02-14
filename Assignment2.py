def main():
        print("welcome to quiz (: -")
   
        usrIpt = int(input('''Enter operation by selecting number 
                1. Register,
                2. login
                3. Atteempt quiz
                
                4. Show Result
                5. Exit
                '''))

        if(usrIpt == 1):
                register()
        elif(usrIpt == 2):
                login()
        elif(usrIpt == 3):
                input("""which one: a. DSA b.DBMS c.Python""")
                Attempt()
        elif(usrIpt == 4):
                showResult()
        elif(usrIpt == 5):
                exit()
        else:
            print("Please enter a valid input number")
        

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
        
        # a user data file
        users = open('user.txt', 'a')

        userInpt = ""
        user_id = get_last_id() + 1  

        while(True):
                userInpt = input("enter name: ")
                if(len(userInpt) < 3):
                        print("name must be of 3 character")
                else: 
                    break

        while(True):
                pwt = input("Enter password: ")
                if(len(pwt) < 4):
                        print("password must be of be 4 character")
                else: 
                    break


                # additional info
        while(True):
                age = input("Enter your age in dd/mm/yy: ")
                if(len(age) < 8):
                        print("enter age oproperly with symbals")
                else: 
                    break


        # saving data to file
        users.write(f"{user_id} {userInpt} {pwt}\n")

        users.close()
        print("User information saved successfully.")
  
# register()



def login():

       
        users = open("user.txt", 'r')
        found_line = None     # finds a line with same username

        while(True): 
                userInpt = input("Enter userId: ")
                found_line = None  

                users.seek(0)  # resset seek pointer

                for line in users:
                # Check if the line starts with the ID and username
                        if line.strip(' ').startswith(f"{userInpt}"):
                                found_line = line
                                break
                
                if found_line:
                        print("Username found, proceeding to password check.")
                        print("Stored user data for further password inquiry:", found_line)
                        # Adding password verification logic here
                        pwt = input("Enter password: ")
                        # if()
  
                        break 
                else:
                        print("Username not found. Please try again or register.")

        users.close()

                # if(found_line):
                #         pwt = input("Enter password: ")
                #         if()

                # else:
                #       print("user not found")
                #       exit()

        
        
                
        
login()
# register()







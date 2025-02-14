
def calci():
    #taking input from user
    num1 = int(input("enter 1st number : "))
    num2 = int(input("enter 2nd number : "))

    choice = int(input('Enter the opreation to perform 1- addituon, 2- substraction, 3- multiplication 4- division : '))

    if choice in [1,2,3,4]:  #validating  input
        if choice == 1:
            print(f"{num1}+{num2} = {num1 + num2}  ")  #addition
        elif choice == 2:
            print(f"{num1}-{num2} = {num1 - num2}  ")   #substraction
        elif choice == 3:
            print(f"{num1}*{num2} = {num1 * num2}  ")   #multiplication
        elif choice == 4:
            print(f"{num1}/{num2} = {num1 / num2}  ")    #division
    else:
        print("please enter a valid operation")


# calci()
#abstract class decorator








# function for greeting

def login(name, pwd, city="Bhopal"):
    username = "jhon"; password="1234"
    name = str(name)
    pwd = str(pwd)
    if name == username and pwd == password:
        return (f"hello {name} welocme to {city}")
        # exit(0)
        # return
    else:
        return ("invaldi username or password")
        # exit(1)
        # return



# username = input("Enter Username : ")
# password = input("Enter password : ")
# print(login(username, password))        #calling login



c = { (2,3): 1 , "c": 2, "b": 88 }

# for k, v in sorted(c.items()):
    # print(k,v)

# print()

print(c[(2,3)])
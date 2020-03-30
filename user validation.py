import random
import string

users = {}

x = 1
i = 1

def userData():
    users[i] = {}
    first = input("Enter your First Name: ")
    last = input("Enter your Last Name: ")
    email = input("Enter your E-mail: ")

    users[i]['first'] = first
    users[i]['last'] = last
    users[i]['email'] = email

    def ranString(stringLength = 5):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

    password = f"{first[0:2]}{last[-2:]}{ranString(5)}"
    users[i]['password'] = password
    def newPass():
        password = input("Enter new Password (password must not be less than 7 characters) : ")
        if len(password) < 7:
            print("Password must not be less than 7 characters")
            newPass()
        else:
            print(f"First Name: {first} \nLast name: {last} \nE-mail: {email} \nPassword: {password}")
            users[i]['password'] = password

    print("Your Password is: ", password)
    def valChoice():
        passChoice = input("Do you wish to keep the password. Enter 1 for yes or 2 to enter a new password: ")

        if passChoice == '1':
            print(f"First Name: {first} \nLast name: {last} \nPassword: {password}")
        elif passChoice == '2':
            newPass()
        else:
            print("Enter a valid choice")
            valChoice()

    valChoice()


while x == 1:
    userData()
    addChoice = input("\nEnter 1 to add User or 2 to end operation: ")
    i = i + 1
    if addChoice == '1':
        continue
    elif addChoice == '2':
        break


i = 1

while i <= len(users):
    print("\nUser ",i)
    print(f"First Name: {users[i]['first']} \nLast name: {users[i]['last']} \nE-mail: {users[i]['email']} \nPassword: {users[i]['password']}")
    i = i + 1

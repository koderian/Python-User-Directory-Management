# This is    a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import copy
import json

path_to_dict =  "./user_login_directory.json"


def password_set():
    global userPassword
    temp_password = None
    while temp_password is None:

        temp_password = input("Please enter a password\n")
        if temp_password == '':
            temp_password = None

        else:
            temp_password is True
            time.sleep(2)
            print("Valid!")
    passwordchck = None
    userPassword = None
    passwordchck = False
    reenter_Error = "Please confirm password\n"
    loop = 3
    while loop != int(0):
        passwordchck = input(reenter_Error)
        if passwordchck == temp_password:
            userPassword = copy.copy(passwordchck)
            print("Password successfully set!")
            return


        elif passwordchck != temp_password:
            reenter_Error = "Password does not match, please try again\n"
            loop = loop - int(1)
            print(str(loop) + " tries remaining!")

    if loop == 0:
        password_set()
1
password_set()
print(userPassword)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

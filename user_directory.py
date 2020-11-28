# This is    a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import copy
import json
from colorama import  Fore, Back, Style
import getpass
import console-menu
path_to_dict =  "./user_login_directory.json"


def user_menu():



def password_set():
    global userPassword
    temp_password = None
    while temp_password is None:

        temp_password = getpass.getpass(Fore.WHITE + "Please enter a password\n")
        if temp_password == '':
            print(Fore.RED + "Invalid password, please try again:")
            temp_password = None

        else:
            temp_password is True
            time.sleep(2)
            print("Valid!")
    passwordchck = None
    userPassword = None
    passwordchck = False
    reenter_Error = (Fore.WHITE + "Please confirm password\n")
    loop = 3
    while loop != int(0):
        passwordchck = getpass.getpass(reenter_Error)
        if passwordchck == temp_password:
            userPassword = copy.copy(passwordchck)
            print(Fore.WHITE + "Password successfully set!")
            return


        elif passwordchck != temp_password:
            reenter_Error = Fore.RED + "Password does not match, please try again:\n"
            loop = loop - int(1)
            print(str(loop) + " tries remaining!")

    if loop == 0:
        print("Reset failed")
        return  
password_set()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

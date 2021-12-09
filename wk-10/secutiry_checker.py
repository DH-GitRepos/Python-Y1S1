# PROJECT: (WK-10) Secure entry
# Solution written by Darren Halpin
# INFO: input "3" from the main menu to exit the program.

import simplejson
import os

USER_DB_FILE = "security_checker_users.json"


def show_main_menu():
    print("\nMAIN MENU")
    print("-" * 9)
    print("1. New user\n2. Existing user")

    try:
        menu_option = int(input("> "))
        if not menu_option < 4 or not menu_option > 0:
            print("ERROR: Enter a valid menu option (1-2)")
            show_main_menu()
        else:
            match menu_option:
                case 1:
                    menu_new_user()
                case 2:
                    menu_existing_user()
                case 3:
                    print("\nGoodbye.")
                    exit()

    except ValueError:
        print("ERROR: Enter a valid menu option (1-2)")
        show_main_menu()


def menu_new_user():
    print("\nADD NEW USER")
    print("-" * 12)

    # CHECK IF USER DATABASE EXISTS
    create_user_database_file()

    # CAPTURE USERNAME
    username = input("\nEnter new username\n> ")

    # CHECK USERNAME INPUT
    user_check = check_valid_username(username)

    while not user_check[0]:
        print(user_check[1])
        username = input("\nEnter new username\n> ")
        user_check = check_valid_username(username)

    print(user_check[1])

    # CAPTURE PASSWORD
    print("PASSWORD RULES:\nMust be at least 8 characters\nCannot begin or end with, or contain a space\n"
          "Cannot begin with a number")
    password = input("\nEnter new password\n> ")

    # CHECK PASSWORD INPUT
    # - check input not blank
    while password == "":
        print("ERROR: Password cannot be blank.")
        print("PASSWORD RULES:\nMust be at least 8 characters\nCannot begin or end with, or contain a space\n"
              "Cannot begin with a number")
        password = input("\nEnter new password\n> ")

    # - validate password rules
    while not check_valid_password(password):
        print("Password did not meet the required rules.")
        print("PASSWORD RULES:\nMust be at least 8 characters\nCannot begin or end with, or contain a space\n"
              "Cannot begin with a number")
        password = input("\nEnter new password\n> ")

    print("Password format OK.")

    # - get password 2nd input
    pass_1 = password
    pass_2 = input("\nRe-enter password\n> ")

    # - compare password inputs
    while not pass_1 == pass_2:
        print("ERROR: Passwords do not match.")
        pass_2 = input("Re-enter password\n> ")

    print("Passwords match.")

    # SAVE CREDENTIALS TO FILE
    if save_credentials(username, password):
        print("New user added successfully.\nYou can now log in.")
    else:
        print("Something went wrong, please try again.")

    # RETURN TO MAIN MENU
    show_main_menu()


def check_valid_username(usr):

    if usr == "":
        msg = "ERROR: Username cannot be blank."
        ret_vals = [False, msg]
        return ret_vals

    else:
        file_contents = check_file_contents_for_zero(USER_DB_FILE)
        if not file_contents:
            msg = "Username is available."
            ret_vals = [True, msg]

            return ret_vals

        else:
            try:
                with open(USER_DB_FILE) as json_in:
                    pwd_db = simplejson.load(json_in)

                    user_check = True

                    for key, value in pwd_db.items():
                        if key == usr:
                            user_check = False

                    if user_check:
                        msg = "Username is available."
                        ret_vals = [True, msg]

                    elif not user_check:
                        msg = "ERROR: Username already exists, please try again."
                        ret_vals = [False, msg]

                    return ret_vals

            except FileNotFoundError:
                msg = "ERROR: Unable to find user database, please try again."
                ret_vals = [False, msg]

                return ret_vals


def check_valid_password(pwd):

    check_1, check_2, check_3 = 0, 0, 0

    # CHECK 1 - password length
    password_length = len(pwd)
    if password_length < 8:
        check_1 = 0
        print("ERROR: Password is less than 8 characters")
    else:
        check_1 = 1

    # CHECK 2 - Check for spaces
    check_2 = 1
    for char in pwd:
        if char == " ":
            check_2 = 0
            print("ERROR: Password contains a space")
            break

    # CHECK 3 - first character not a number
    if not pwd[0].isdigit():
        check_3 = 1
    else:
        print("ERROR: First digit is a number")

    final_check = (check_1 + check_2 + check_3)

    if final_check == 3:
        return True
    else:
        return False


def save_credentials(usr, pwd):

    file_not_empty = check_file_contents_for_zero(USER_DB_FILE)

    if not file_not_empty:
        tmp_pwd_db = {usr: pwd}

        try:
            with open(USER_DB_FILE, 'w') as out_file:
                simplejson.dump(tmp_pwd_db, out_file, indent=2)

            return True

        except FileNotFoundError:
            print("ERROR: User database could not be accessed. Please Try again.")

            return False

    else:
        try:
            with open(USER_DB_FILE) as in_file:
                tmp_pwd_db = simplejson.load(in_file)

            tmp_pwd_db.update({usr: pwd})

            with open(USER_DB_FILE, 'w') as out_file:
                simplejson.dump(tmp_pwd_db, out_file, indent=2)

            return True

        except FileNotFoundError:
            print("ERROR: User database could not be accessed. Please Try again.")

            return False


def create_user_database_file():

    try:
        open(USER_DB_FILE, 'x')
        print("User database created successfully.")
        return True

    except FileExistsError:
        print("User database opened successfully.")
        return False


def menu_existing_user():
    print("\nUSER LOGIN")
    print("-" * 10)

    # CHECK IF USER DATABASE IS POPULATED
    database_populated = check_file_contents_for_zero(USER_DB_FILE)

    if database_populated:
        username = input("\nEnter username\n> ")
        password = input("Enter password\n> ")
        login_check_credentials(username, password)

    else:
        print("No users exist, please create a user first")
        show_main_menu()


def login_check_credentials(user, pwd):

    username_check = False
    password_check = False
    credentials_pair = []

    try:
        with open(USER_DB_FILE) as in_file:
            tmp_pwd_db = simplejson.load(in_file)

        # CHECK FOR USERNAME IN DATABASE
        for key, value in tmp_pwd_db.items():
            if key == user:
                username_check = True
                credentials_pair = [key, value]

            else:
                username_check = False

        if not username_check:
            print("Username/password incorrect, please try again.")
            show_main_menu()

        else:
            # CHECK PASSWORD
            # - check if account locked based on pwd set to "x" by login_fail()
            if credentials_pair[1] == "x":
                print("This account is locked. Please contact a system administrator.")
                show_main_menu()

            # - if not locked, check password
            elif pwd != credentials_pair[1]:
                for num in range(2):
                    print("Password incorrect.")
                    pwd = input("\nEnter password\n> ")
                    if pwd == credentials_pair[1]:
                        password_check = True
                        break
                    else:
                        password_check = False

                if password_check:
                    login_success()
                else:
                    login_fail(user)

            else:
                login_success()

    except FileNotFoundError:
        print("Unable to locate database.")
        show_main_menu()


def login_success():
    print("Welcome! You are now logged in.")
    exit()


def login_fail(lock_user):

    try:
        with open(USER_DB_FILE) as in_file:
            tmp_pwd_db = simplejson.load(in_file)

        tmp_pwd_db.update({lock_user: "x"})

        with open(USER_DB_FILE, 'w') as out_file:
            simplejson.dump(tmp_pwd_db, out_file, indent=2)

        print("Password entered incorrect 3 times, account locked.")
        print("Contact a system administrator to access your account.")
        show_main_menu()

    except FileNotFoundError:
        print("ERROR: User database could not be accessed. Please Try again.")
        return False


def check_file_contents_for_zero(fpath):

    try:
        # returns true if file is not empty
        return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

    except FileNotFoundError:
        print("Unable to locate database.")


# MAIN CODE EXECUTION
show_main_menu()

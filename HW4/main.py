from getpass import getpass
from users import User


while True:
    try:
        state = input("Press (0(Exit) - 1(Sign Up) - 2(Sign In)):   ")
    except NameError:
        print("\nInvalid input")
        continue
    if stat == "5":
        print(User.usernames, end="\n")
        for user_hash in User.hashes:
            print(user_hash)
        for i, j in User.user_info.items():
            print(j, i, sep="\t")

    elif state == "1":
        username = input("Enter Username: ")
        password = getpass("Enter Password: ")
        phone_number = input("Enter Phone number(Optional): ")
        User.signup(username, password, phone_number)
        User.password_check(password)
        print("\nSigning Up Completed! ")

    elif stat == "2":
        username = input("Enter Username: ")
        password = getpass("Enter Password: ")
        USER_OBJECT = User.sign_in_validation(username, password)
        print("\nSigning In Completed! ")

        while True:
            stat = input("Stat (1(Show User Information) - 2(Edit) - 3(Password Change) - 4(Back to Main Menu)):   ")

            if stat == "1":
                USER_OBJECT.representation()

            elif stat == "2":
                new_username = input("Enter New Username: ")
                new_phone_number = input("Enter New Phone Number")
                USER_OBJECT.edit_user(new_username, new_phone_number)
                print("\nUser Information has been Updated! ")

            elif stat == "3":
                old_pass = getpass("Enter Old Password: ")
                new_pass = getpass("Enter New Password: ")
                rep_new_pass = getpass("Enter New Password again: ")
                USER_OBJECT.passwd_change(old_pass, new_pass, rep_new_pass)
                print("\nYour Password has been changed! ")

            elif stat == "4":
                print("\nExiting User Panel...")
                break

            else:
                print("\nInvalid State! ")
                continue

    elif stat == "0":
        print("\nExiting the User Management Panel... ")
        break

    else:
        print("\nInvalid State! ")
        continue
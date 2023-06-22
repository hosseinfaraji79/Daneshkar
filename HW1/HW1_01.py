username = input("Enter username : ")
password = input("Enter password : ")

if username and password == "admin":
    print("welcome")
elif username == "admin":
    print("Wrong password")
else:
    print(f"Hello {username}")
    
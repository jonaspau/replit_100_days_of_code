def login():
    print("Welcome to the login page")
    print("Please enter your username and password")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "password":
        print("Login successful")
    else:
        login()


login()
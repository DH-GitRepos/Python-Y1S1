# PROJECT: (WK-04) Check Password
# Solution written by Darren Halpin

PASSWORD = "Rocket"

user_pwd = input("Please enter the password: ")

if user_pwd.casefold() == PASSWORD.casefold():
    print("Welcome, you are logged in.")
else:
    print("Invalid password.")


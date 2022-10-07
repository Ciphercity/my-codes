#SIMPLE python task
# name and password
print("Create account ")
username =input("Enter your username: ")
password =input("Enter your password: ")
print("new account created successfully")
print( username + " you can now log in")
username2 =input("Enter your username: ")
password2 =input("Enter your password: ")
if (username == username2)& (password == password2):
    print(" login successful")
else:
    print("invalid username or password")    
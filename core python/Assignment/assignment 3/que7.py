#7. Write a program to check if user has entered correct userid and password. 

correct_userid = "bobbypatil"
correct_password = "ompatil006"

user_id = input("enter the user id")
user_password =input("enter the password")

if(correct_userid == user_id):
    print("user id is correct")
    if(correct_password == user_password):
        print("password is correct")
    else:
        print("password is wrong")
else:
    print("wrong user id")
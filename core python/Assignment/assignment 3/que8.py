# 8. Write a program to prompt user to enter userid and password. After verifying 
# userid and password display a 4 digit random number and ask user to enter the 
# same. If user enters the same number then show him success message otherwise 
# failed. (Something like captcha)??

correct_userid =  "sohel"
correct_password = "om9090"

user_id = input("enter the id")
user_pass = input("enter the password")

if(correct_userid == user_id and correct_password == user_pass):
    print("login successfully")

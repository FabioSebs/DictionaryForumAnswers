#Import
from accept_login import acceptlogin
#Variables
dictofusers = {
    "User1" : "password1",
    "User2" : "password2",
    "User3" : "password3",
    "User4" : "password4"    
}

username = "User2"
password = "password2"

falseusername = "Fabio"
falsepassword = "qwerty"

#Main
if __name__ == "__main__":
    print(acceptlogin(dictofusers,username,password))
    print(acceptlogin(dictofusers,falseusername,password))
    print(acceptlogin(dictofusers,username,falsepassword))
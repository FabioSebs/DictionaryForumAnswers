def acceptlogin(users, username, password):
    if users.get(username , False) == False:
        return False
    else:
        if users.get(username) == password:
            return True
        else:
            return False
    
    
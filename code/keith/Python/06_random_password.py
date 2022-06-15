def logic(user, password, p_dict):
    if p_dict['username'] == user and p_dict['password'] == password:
       return True 
        
    else:
        return False



profile = {
    'username': 'rabbit',
    'password': 'love'
}

again = True
while again:

    username_attempt = input('Type in your username: ')
    password_attempt = input('Type in your password: ')

    result = logic(username_attempt, password_attempt, profile)

    if result == True:
        again = False 
        print('successfully logged in!')

    else:
         print('log in unsuccessful')        



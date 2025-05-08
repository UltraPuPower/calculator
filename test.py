users = [
    {'userName': 'Admin', 'userPassword': 'P@$$w0rd'},
    {'userName': 'User1', 'userPassword': 'password'}
]

def loginCheck(givenName, givenKey):
    loginValid = False
    for user in users:
        if givenName in user['userName'] and givenKey in user['userPassword']:
            loginValid = True
    if loginValid:
        return True
    else:
        return False
    
print(loginCheck('Admin', 'P@$$w0rd'))
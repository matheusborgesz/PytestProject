##criterios do nome de usuario##

def getUser():
    user = input("Digite o nome de usuario: ")
    return user

def userUppercase(user):
    if user[0].isupper():
        return True
    else:
        return False
    
def userLength(user):
    if len(user) > 30:
        return False
    else:
        return True

def userWhitespace(user):
    if ' ' in user:
        return False
    else:
        return True    
    
def userSpecialChars(user):
    specialChars = '!@#$%^&*()_+-=[]{}|;:,.<>/?'
    for char in user:
        if char in specialChars:
            return False
    return True

    
##Criterios senha##

def getPassword():
    password = input("Digite uma senha: ")
    return password

def passwordUppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def passwordSpecialChars(password):
    specialChars = '!@#$%^&*()_+-=[]{}|;:,.<>/?'
    for char in password:
        if char in specialChars:
            return True
    return False

def passwordLength(password):
    if len(password) < 10:
        return False
    else:
        return True
    
def passwordNumbers(password):
    num = '1234567890'
    for char in password:
        if char in num:
            return True
    return False

##Criterios mensagem##

def getMessage():
    message = input("Digite a sua mensagem: ")
    return message

def messageLength(message):
    if len(message) > 70:
        return False
    else:
        return True

import re
##função que define login do usuário##
user = input("Digite o nome de usúario: ")

regex = r'^[A-Z][a-zA-Z0-9]{0,29}$'

def checkUser(user):
    if re.search(regex, user):
        return True
    else:
        return False

print (checkUser(user))
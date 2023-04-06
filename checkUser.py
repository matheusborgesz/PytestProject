from user import *
import re

regex = "^(?!.*[_\W]).{1,30}$"

def checkUser(usuario):
    if usuario[0].isupper() and re.match(regex, usuario):
        print("Nome de usuário válido.")
        return True
    else:
        print("O nome de usuário não atende aos requisitos.")
        return False
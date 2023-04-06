import re

regex = "^(?!.*[_\W]).{1,30}$"

def user():
    while True:
        usuario = input("Digite o nome de usuário: ")
        checkUser(usuario)
        if usuario[0].isupper() and re.match(regex, usuario):
            break

user()
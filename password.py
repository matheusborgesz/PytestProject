import re 

regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$"

def password():
    while True:
        senha = input("Digite sua senha:")
        if checkPassword(senha):
            break

def checkPassword(senha):
    if re.match(regex, senha):
        print("Senha valida:")
        return True
    else:
        print("A senha informada não atende aos requisitos:")
        return False


password()
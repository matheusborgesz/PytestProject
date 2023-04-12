from criteriosLogin import *
from cryptographyFramework import *

#user
def validaUser():
    while True:
        user = getUser()
        if userUppercase(user) and userWhitespace(user) and userSpecialChars(user) and userLength(user):
            return user
        else:
            print("O nome de usuário deve ter a primeira letra maiúscula, sem caracteres especiais e sem espaços e no máximo 30 caracteres, tente novamente!")

user = validaUser()


#senha
def validaPassword():
    while True:
        password = getPassword()
        if passwordLength(password) and passwordSpecialChars(password) and passwordNumbers(password) and passwordUppercase(password):
            return password
        else:
            print("A senha deve ter pelo menos 10 caracteres, um caracter especial, um número, ao menos uma letra maiúscula e uma letra minúscula, tente novamente!")

password = validaPassword()

#message
def validaMessage():
    while True:
        message = getMessage()
        if messageLength(message):
            return message
        else:
            print("A mensagem deve ter no máximo 70 caracteres, tente novamente!")

message = validaMessage()

#main#

print("Usuario:", user)
print("Senha:", password)
print("Mensagem criptografada: ", message)

# savemessage

initializeWrite()
encryptedText = encryptMessage(user, password, message)
saveNewLine(encryptedText)

# printmessage

initializeRead()
line1 = readNextLine()
print(line1)
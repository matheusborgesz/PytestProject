from cryptographyFramework import *

initializeWrite()
user = "matheus"
password = "123456789"
encryptedText = encryptMessage(user, password, "SDKASJDKASFHJDGHDLGSGHJLSDGHSDOSDFKLSDFLKSDFLSKDJFSFJSDFLKKSDFLKJSDF")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "matheus borgesssdaldkalsdklafjaffaf")
saveNewLine(encryptedText)


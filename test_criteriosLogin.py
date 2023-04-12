from criteriosLogin import *

def test_userUppercase():
    assert userUppercase("Joao") == True
    assert userUppercase("joao") == False

def test_userLength():
    assert userLength("matheus") == True
    assert userLength("matheusssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss") == False

def test_userWhitespace():
    assert userWhitespace("pedro") == True
    assert userWhitespace("pedro oo") == False

def test_userSpecialChars():
    assert userSpecialChars("jaco") == True
    assert userSpecialChars("j@co") == False

def test_passwordUppercase():
    assert passwordUppercase("Matheus!sss55s") == True
    assert passwordUppercase("matheus!ss5ss") == False

def test_passwordSpecialChars():
    assert passwordSpecialChars("Matheus@12345") == True
    assert passwordSpecialChars("Matheus12345") == False

def test_passwordLength():
    assert passwordLength("Matheus@123456") == True
    assert passwordLength("Matheus@1") == False

def test_passwordNumbers():
    assert passwordNumbers("M@theus55555") == True
    assert passwordNumbers("Matheus@ssssss") == False

def test_messageLength():
    assert messageLength("oi") == True
    assert messageLength("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == False
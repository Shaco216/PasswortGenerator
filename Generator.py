import random
from InputModel import *

class Generator:
    inputModel = InputModel()
    passwordLength = 0
    passwordComplexibility = ["allCharacters", "noGermanCharacters", "noGermanChractersAndNoSpecialCharacters"]
    possibleCharacters = []

    def __init__(self):
        pass
    def SetPasswordLength(self, pwLength):
        self.passwordLength = int(pwLength)
    def SetComplexibility(self, complexibility):
        self.passwordComplexibility = complexibility
    def GeneratePassword(self, complexibility,newPW):
        self.possibleCharacters = self.inputModel.GetCharacters(complexibility)
        newPWstring = ""
        for pwLen in range(self.passwordLength):
            newPWstring= newPWstring + self.possibleCharacters[random.randint(0,len(self.possibleCharacters)-1)]
        newPW.set(newPWstring)
        return newPW



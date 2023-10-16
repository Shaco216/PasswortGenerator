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
    def GeneratePassword(self, complexibility):
        self.possibleCharacters = self.inputModel.GetCharacters(self.passwordComplexibility)
        newPW = ""
        for pwLen in range(self.passwordLength):
            newPW= newPW + self.possibleCharacters[random.randint(0,len(self.possibleCharacters)-1)]
        return newPW



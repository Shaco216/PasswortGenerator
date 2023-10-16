
class InputModel:
    alphabeth = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    germanCharacters = ["ö", "ä", "ü", "ß"]
    specialCharacters = ["!", "?", "+", "-", "*", "/", "§", "$", "%", "&", "(", ")", "[", "]", "{", "}", "~", ";", ",", ".", ":", ">", "<", "|", "°", '"', "#", "'", "^"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    copitalAlphabeth = []

    def __init__(self):
        for letter in self.alphabeth:
            self.copitalAlphabeth.append(letter.upper())
    def GetCharacters(self, complexity):
        if(complexity == 0):
            return self.alphabeth + self.germanCharacters + self.specialCharacters + self.numbers + self.copitalAlphabeth
        if(complexity == 1):
            return self.alphabeth + self.specialCharacters + self.numbers + self.copitalAlphabeth
        if(complexity == 2):
            return self.alphabeth + self.numbers + self.copitalAlphabeth
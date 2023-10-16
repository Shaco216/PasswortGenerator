
class InputModel:
    alphabeth = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    umlaute = ["ö","ä","ü","ß"]
    sonderzeichen = ["!","?","+","-","*","/","§","$","%","&","(",")","[","]","{","}","~",";",",",".",":",">","<","|","°",'"',"#","'","^"]
    zahlen = [0,1,2,3,4,5,6,7,8,9]
    grossesAlphabeth = []

    def __init__(self):
        for letter in self.alphabeth:
            self.grossesAlphabeth.append(letter.upper())
    
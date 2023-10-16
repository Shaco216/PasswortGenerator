from tkinter import *
from tkinter import ttk
from Generator import *

# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

masterWindow= Tk()
masterWindow.title = "Passwordgenerator"
#region specialMethods
def ShowNewComponents():
    for newComp in newComponentes:
        if newComp is type(Text):
            newComp.insert(newPW.get())
        newComp.pack()

#endregion
#region ViewProperties
pwGen = Generator()
complexity = StringVar()
complexity.set(pwGen.passwordComplexibility[0])
newPW = StringVar()
newPW.set = ""

#endregion

elementsHeight = 1

allComponents = []
newComponentes = []
allComponents.append(Label(masterWindow,text="Bitte Passwortlänge eingeben:"))
allComponents.append(Text(masterWindow, height=elementsHeight, width=3))
allComponents.append(Label(masterWindow,text="Bitte Komplexität wählen: "))
allComponents.append(OptionMenu(masterWindow, complexity, *pwGen.passwordComplexibility))
allComponents.append(Button(masterWindow, text="Create Password", command=lambda:
[pwGen.GeneratePassword(complexity,newPW), ShowNewComponents]))


newComponentes.append(Label(masterWindow, text="Hier ist ihr neues Passwort"))
newComponentes.append(Text(masterWindow, height=elementsHeight))


for component in allComponents:
    component.pack()

mainloop()
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

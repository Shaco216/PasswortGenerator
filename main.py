from tkinter import *
from tkinter import ttk
from Generator import *

# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

masterWindow= Tk()
masterWindow.title = "Passwordgenerator"

#region ViewProperties
pwGen = Generator()
complexity = StringVar()
complexity.set(pwGen.passwordComplexibility[0])
newPW = StringVar()

#endregion

elementsHeight = 2

allComponents = []
newComponentes = []
allComponents.append(Label(masterWindow,text="Bitte Passwortlänge eingeben:"))
allComponents.append(Text(masterWindow, height=elementsHeight))
allComponents.append(Label(masterWindow,text="Bitte Komplexität wählen: "))
allComponents.append(OptionMenu(masterWindow, complexity, *pwGen.passwordComplexibility))
allComponents.append(Button(masterWindow, text="Create Password", command=lambda:
[newPW.set(pwGen.GeneratePassword(complexity.get())), ShowNewComponents]))


newComponentes.append(Label(masterWindow, text="Hier ist ihr neues Passwort"))
newComponentes.append(Text(masterWindow))


for component in allComponents:
    component.pack()

mainloop()
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
def ShowNewComponents():
    for newComp in range(newComponentes):
        if(newComp == 1):
        newComp[newcom].pack

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# import du module Tkinter pour la création d'une fenêtre
from tkinter import *

fenetrePrincipale = Tk()

def getEntry():
    print(ChampChoiceTime.get())
    ResultatTime = Label(fenetrePrincipale, text = ChampChoiceTime.get()) 
    ResultatTime.pack()

fenetrePrincipale.geometry('500x500')
fenetrePrincipale.resizable(0, 0)
LabelChoiceTime = Label (fenetrePrincipale, text="Lancer le Chronométre")
ChampChoiceTime = Entry (fenetrePrincipale)
LaunchChrono = Button(fenetrePrincipale, text ="Lancer le Chronomètre", command=getEntry)

LabelChoiceTime.pack()
ChampChoiceTime.pack()
LaunchChrono.pack()

fenetrePrincipale.mainloop()
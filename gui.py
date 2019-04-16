from tkinter import *
import tkinter as tk

OPTIONS = [
"Προσαρμοσμένος πληθυσμός με προεπιλεγμένο παθογόνο παράγοντα",
"Προσαρμοσμένος πληθυσμός με προσαρμοσμένο παθογόνο παράγοντα",
]

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        window = Tk()
        window.title('Προσομοιωτής')
        window.geometry("600x600+10+10")
        self.population = Entry(window, text="Πληθυσμός", bd=5)
        self.population.place(x=20, y=50)
        self.populationLabel = Label(window, text="Πληθυσμός", bd=5)
        self.populationLabel.place(x=200, y=50)

        self.efpatheis = Entry(window, text="Ευπαθείς Πληθυσμός", bd=5)
        self.efpatheis.place(x=20, y=100)
        self.efpatheisLabel = Label(window, text="Ευπαθείς Πληθυσμός", bd=5)
        self.efpatheisLabel.place(x=200, y=100)

        self.initialyContaminated = Entry(window, text="Αρχικά Μολυσμένοι", bd=5)
        self.initialyContaminated.place(x=20, y=150)
        self.initialyContaminatedLabel = Label(window, text="Αρχικά Μολυσμένοι", bd=5)
        self.initialyContaminatedLabel.place(x=200, y=150)

        self.immune = Entry(window, text="Ανοσοποιημένοι", bd=5)
        self.immune.place(x=20, y=200)
        self.immuneLabel = Label(window, text="Ανοσοποιημένοι", bd=5)
        self.immuneLabel.place(x=200, y=200)

        self.simulationLength = Entry(window, text="Διάρκεια Προσομοίωσης", bd=5)
        self.simulationLength.place(x=20, y=250)
        self.simulationLengthLabel = Label(window, text="Διάρκεια Προσομοίωσης", bd=5)
        self.simulationLengthLabel.place(x=200, y=250)

        self.btn=Button(window, text="Run", command=self.buttonclick)
        self.btn.place(x=300, y=500)

        variable = StringVar(window)
        variable.set(OPTIONS[0])
        w = OptionMenu(window, variable, *OPTIONS)
        w.place(x=20, y=350)


    def buttonclick(self):
        print('hello')
        #here call epidhmia with arguments


app = Calculator()
app.mainloop()

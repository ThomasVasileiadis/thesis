from tkinter import *

class Calculator:
    window = Tk()
    population = Entry(window, text="Πληθυσμός", bd=5)
    population.place(x=20, y=50)
    populationLabel = Label(window, text="Πληθυσμός", bd=5)
    populationLabel.place(x=200, y=50)

    efpatheis = Entry(window, text="Ευπαθείς Πληθυσμός", bd=5)
    efpatheis.place(x=20, y=100)
    efpatheisLabel = Label(window, text="Ευπαθείς Πληθυσμός", bd=5)
    efpatheisLabel.place(x=200, y=100)

    initialyContaminated = Entry(window, text="Αρχικά Μολυσμένοι", bd=5)
    initialyContaminated.place(x=20, y=150)
    initialyContaminatedLabel = Label(window, text="Αρχικά Μολυσμένοι", bd=5)
    initialyContaminatedLabel.place(x=200, y=150)

    immune = Entry(window, text="Ανοσοποιημένοι", bd=5)
    immune.place(x=20, y=200)
    immuneLabel = Label(window, text="Ανοσοποιημένοι", bd=5)
    immuneLabel.place(x=200, y=200)

    simulationLength = Entry(window, text="Διάρκεια Προσομοίωσης", bd=5)
    simulationLength.place(x=20, y=250)
    simulationLengthLabel = Label(window, text="Διάρκεια Προσομοίωσης", bd=5)
    simulationLengthLabel.place(x=200, y=250)


    def buttonClick(self):
        print
        'click!'


    btn = Button(window, text="Ξεκινήστε την προσομοίωση", fg='black', command=buttonClick)
    btn.place(x=300, y=500)



    window.title('Προσομοιωτής')
    window.geometry("600x600+10+10")
    window.mainloop()



#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from decimal import *
from pathogono import pathDef

# Definition toy pathogonoy me kapoia vasika stoixeia
p1 = pathDef("Ιός του Ιλαρά", "Ιός", "11234", "Ιλαράς", 18, 8)
p2 = pathDef("Πρωτόζωο", "Ιός", "5855", "Ελονοσία", 5, 15)
p3 = pathDef("Βάκιλος του Γερσίν", "Βακτήριο", "632", "Πανούκλα", 16, 6)
p4 = pathDef("Πολιοϊός", "Ιός", "12079", "Πολιομυελίτιδα", 10, 12)


def popCreate(p):
    print("-----------------------------------")
    print("\nΠαθογόνο που επιλέχτηκε:")
    p.printPath()
    t = 10
    print("-----------------------------------")
    print("Δημιουργία δοκιμαστικού πλυθησμού.\n")
    n = int(input("Εισάγετε τον συνολικό αριθμό ατόμων στον πλυθησμό: "))  # n einai o plythismos
    s = int(input("Εισάγετε τον αριθμό των ευπαθών ατόμων: "))  # s einai o susceptible(eypathis) plythismos
    i = int(input("Εισάγετε τον αριθμό των αρχικά μολυσμένων ατόμων: "))  # i einai o infectious(molysmenos) plythismos
    r = int(input("Εισάγετε τον αριθμό των ανοσοποιημένων ατόμων: "))  # r einai o recovered/immune(anosopoihmenos) plythismos
    print("\nΟ δοκιμαστικός πλυθησμός αποτελείται από {0} ευπαθείς, {1} μολυσμένους,".format(str(s), str(i)))
    print("και {0} ανοσοποιημένους. \n".format(str(r)))
    t1 = int(input("Εισάγετε το μήκος προσομείωσης σε μέρες: "))  # t einai to time(meres) poy tha diarkesei h prosomoiwsh
    if t1 != 0:  # default mhkos se meres einai to 10 kai epilegetai me 0
        t = t1
        b = p.getB()
        y = 1 / p.getPeriod()
    print("-----------------------------------")
    # ektypwse ta apotelesmata
    print("Ημέρα 0: {0} ευπαθείς, {1} μολυσμένοι, {2} ανοσοποιημένοι, {3} συνολικά.".format(str(s), str(i), str(r),str(n)))
    # efarmogh toy SIR monteloy
    for day in range(1, t + 1):
        s1 = s
        i1 = i
        r1 = r
        if (s1 - ((b * s1 * i1) / n)) < 0:
            s = 0.0
        else:
            s = round((s1 - ((b * s1 * i1) / n)), 1)
            i = round((i1 + (((b * s1 * i1) / n) - (y * i1))), 1)
            r = n - s - i
            # ektypwse ta apotelesmata
        print("Ημέρα {0}: {1} ευπαθείς, {2} μολυσμένοι, {3} ανοσοποιημένοι, {4} συνολικά.".format(str(day), str(s),str(i), str(r),str(n)))
    r0 = float(p.getR0())
    ip = p.getPeriod()
    th = round((1 / r0), 3)
    si = round((th * n), 1)
    ii = n - si
    print("-----------------------------------")
    print("Στατιστικά στοιχεία: \n")
    print("Παθογόνο R0 σε πλήρως ευαίσθητο πληθυσμό: {0}".format(str(r0)))
    print("Παθογόνος περίοδος μολυσματικότητας: {0} ημέρες".format(str(ip)))
    print("Όριο ευαισθησίας: {0} άτομα".format(str(si)))
    print("Ανοσολογικά άτομα που χρειάστηκαν για την πρόληψη της επιδημίας: {0} άτομα".format(str(ii)))
    print("Όριο κατωφλιού: {0}".format(str(th)))
    print("-----------------------------------\n")


# arxiko menu epiloghs
print("Καλώς ήλθατε!\n")
print("1. Προσαρμοσμένος πλυθησμός με προεπιλεγμένο παθογόνο παράγοντα.")
print("2. Προσαρμοσμένος πλυθησμός με προσαρμοσμένο παθογόνο παράγοντα.")
print("3. Έξοδος.\n")
swch = int(input("Παρακαλώ επιλέξτε: "))
# an dialexthke to 1 tote
if swch == 1:
    print("-----------------------------------")
    print("Προεπιλεγμένα παθογόνα \n")
    print("Παρακαλώ επιλέξτε ένα παθογόνο της παρακάτω λίστας:\n")
    print("1.Ιλαρά")
    print("2.Πρωτόζωο")
    print("3.Βάκιλος του Γερσίν")
    print("4.Πολιοϊός")
    ps = int(input("Παρακαλώ επιλέξτε: "))
    if ps == 1:
        pc = p1
        popCreate(pc)
    # alliws, an dialexthke to 2 tote
    elif ps == 2:
        pc = p2
        popCreate(pc)
    elif ps == 3:
        pc = p3
        popCreate(pc)
    elif ps == 4:
        pc = p4
        popCreate(pc)

elif swch == 2:
    print("-----------------------------------")
    print("Προσαρμοσμένη λειτουργεία παθογόνου \n")
    name = input("Εισάγετε το όνομα του παθογόνου: ")
    pType = input("Εισάγετε τον τύπο του παθογόνου: ")
    taxID = input("Εισάγετε το αναγνωριστικό ταξινομικής ταυτότητας NCBI(αν υπάρχει): ")
    disease = input("Εισάγετε το όνομα της νόσου: ")
    R0 = input("Εισάγετε το R0 του παθογόνου παράγοντα: ")
    per = input("Εισάγετε την περίοδο μολυσματικότητας: ")
    pc = pathDef(name, pType, taxID, disease, R0, per)
    popCreate(pc)
    # alliws an dialexthke to 3 tote
elif swch == 3:
    print("")
    # diaforetika kapoio lathos egine
else:
    print("-----------------------------------")
    print("Έγινε κάποιο λάθος, παρακαλώ δοκιμάστε ξανά.")
    print("******************************************************************************")

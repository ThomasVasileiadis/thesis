#!/usr/bin/env python
import tkinter;
from pathogono import pathDef
from decimal import *
 #Definition toy pathogonoy me kapoia vasika stoixeia
p1 = pathDef("Ιός της Ιλάράς", "Ιός", "11234", "Ιλαράς", 18, 8)

def popCreate(p):
 print("-----------------------------------")
 print("\nΠαθογόνο που επιλέχτηκε:")
 p.printPath()
 t = 10
 print("-----------------------------------")
 print("Δημιουργία δοκιμαστικού πληθυσμού.\n")
 n = int(input("Εισάγετε τον συνολικό αριθμό ατόμων στο πληθυσμό: ")) # n einai o plythismos
 s = int(input("Εισάγετε τον αριθμό των ευπαθών ατόμων: ")) # s einai o susceptible(eypathis) plythismos
 i = int(input("Εισάγετε τον αριθμό των αρχικά μολυσμένων ατόμων: ")) # i einai o infectious(molysmenos) plythismos
 r = int(input("Εισάγετε τον αριθμό των ανοσοποιημένων ατόμων: ")) # r einai o recovered/immune(anosopoihmenos) plythismos
 print("\nO δοκιμαστικός πληθυσμός αποτελείται από {0} ευπαθείς, {1} μολυσμένους,".format(str(s), str(i)))
 print("and {0} ανοσοποιημένους. \n".format(str(r)))
 t1 = int(input("Εισάγετε το μήκος της προσομοίωσης σε μέρες: ")) # t einai to time(meres) poy tha diarkesei h prosomoiwsh
 if t1 != 0: #default mhkos se meres einai to 10 kai epilegetai me 0
  t = t1
  b = p.getB()
  y = 1/p.getPeriod()
 print("-----------------------------------")
 #ektypwse ta apotelesmata
 print("Ημέρα 0: {0} ευπαθείς, {1} μολυσμένοι, {2} ανοσοποιημενοι, {3} συνολικα.".format(str(s),str(i),str(r),str(n)))
 #efarmogh toy SIR monteloy
 for day in range(1,t+1):
  s1 = s
  i1 = i
  r1 = r
  if (s1 - ((b*s1*i1)/n)) < 0:
   s = 0.0
  else:
   s = round((s1 - ((b*s1*i1)/n)),1)
   i = round((i1 + (((b*s1*i1)/n) - (y*i1))),1)
   r = n - s - i
   #ektypwse ta apotelesmata
  print("Ημέρα {0}: {1} ευπαθείς, {2} μολυσμένοι, {3} ανοσοποιημενοι, {4} συνολικα.".format(str(day),str(s),str(i),str(r),str(n)))
 r0 = float(p.getR0())
 ip = p.getPeriod()
 th = round((1/r0),3)
 si = round((th*n),1)
 ii = n-si
 print("-----------------------------------")
 print("Στατιστικά στοιχεία: \n")
 print("Παθογόνο R0 σε πλήρως ευαίσθητο πληθυσμό: {0}".format(str(r0)))
 print("Παθογόνος περίοδος μολυσματικότητας: {0} ημέρες".format(str(ip)))
 print("Όριο ευαισθησίας: {0} άτομα".format(str(si)))
 print("Ανοσολογικά άτομα που χρειάστηκαν για την πρόληψη της επιδημίας: {0} άτομα".format(str(ii)))
 print("Όριο κατωφλιού: {0}".format(str(th)))
 print("-----------------------------------\n")
 


#arxiko menu epiloghs
print("Καλώς ήλθατε!\n")
print("1. Prosarmosmenos plythismos me proepilegmeno pathogono paragonta.")
print("2. Prosarmosmenos plythismos me Prosarmosmeno pathogono paragonta.")
print("3. Έξοδος.\n")
swch = int(input("Παρακαλώ επιλέξτε: "))
#an dialexthke to 1 tote
if swch == 1:
 print("-----------------------------------")
 print("        Proepilegmena pathogona \n")
 print("Parakalw epilekste ena pathogono ths parakatw listas:\n")
 print("1. Ιλαράς.")
 print("- Ena eksairetika metadidomeno pathogono.")
 ps = int(input("Παρακαλώ επιλέξτε: "))
 if ps == 1:
  pc = p1
  popCreate(pc)
 #alliws, an dialexthke to 2 tote
elif swch == 2:
 print("-----------------------------------")
 print("     Prosarmosmenh dhmioyrgia pathogonoy \n")
 name = raw_input("Eisagete to onoma toy pathogonoy: ")
 pType = raw_input("Eisagete ton typo toy pathogonoy: ")
 taxID = raw_input("Eisagete to anagnwristiko taksinomikhs taytothtas NCBI(an yparxei): ")
 disease = raw_input("Eisagete to onoma ths nosoy: ")
 R0 = raw_input("Eisagete to R0 toy pathogonoy paragonta: ")
 per = raw_input("Eisagete thn periodo molysmatikothtas: ")
 pc = pathDef(name,pType,taxID,disease,R0,per)
 popCreate(pc)
 #alliws an dialexthke to 3 tote
elif swch == 3:
 print("")
 #diaforetika kapoio lathos egine
else:
 print("-----------------------------------")
 print("Egine kapoio lathos, parakalw dokimaste ksana.")
 print("******************************************************************************")

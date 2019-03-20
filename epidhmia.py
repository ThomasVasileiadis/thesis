#!/usr/bin/env python
 
from pathogono import pathDef
from decimal import *
 #Definition toy pathogonoy me kapoia vasika stoixeia
p1 = pathDef("Ios toy Ilara", "Ios", "11234", "Ilaras", 18, 8)
 
def popCreate(p):
 print("-----------------------------------")
 print("\nPathogono poy epilextike:")
 p.printPath()
 t = 10
 print("-----------------------------------")
 print("Dhmioyrgia dokimastikoy plythismoy.\n")
 n = int(input("Eisagete ton synoliko arithmo atomwn sto plythismo: ")) # n einai o plythismos
 s = int(input("Eisagete ton arithmo twn eypathwn atomwn: ")) # s einai o susceptible(eypathis) plythismos
 i = int(input("Eisagete ton arithmo twn arxika molysmenwn atomwn: ")) # i einai o infectious(molysmenos) plythismos
 r = int(input("Eisagete ton arithmo twn anosopoihmenwn atomwn: ")) # r einai o recovered/immune(anosopoihmenos) plythismos
 print("\nO dokimastikos plythismos apoteleitai apo {0} eypatheis, {1} molysmenoys,".format(str(s), str(i)))
 print("and {0} anosopoihmenoys. \n".format(str(r)))
 t1 = int(input("Eisagete to mhkos prosomoiwshs se meres: ")) # t einai to time(meres) poy tha diarkesei h prosomoiwsh
 if t1 != 0: #default mhkos se meres einai to 10 kai epilegetai me 0
  t = t1
  b = p.getB()
  y = 1/p.getPeriod()
 print("-----------------------------------")
 #ektypwse ta apotelesmata
 print("Hmera 0: {0} eypatheis, {1} molysmenoi, {2} anosopoihmenoi, {3} synolika.".format(str(s),str(i),str(r),str(n)))
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
  print("Hmera {0}: {1} eypatheis, {2} molysmenoi, {3} anosopoihmenoi, {4} synolika.".format(str(day),str(s),str(i),str(r),str(n)))
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
print("1. Προσαρμοσμένος πλυθησμός με προεπιλεγμένο παθογόνο παράγοντα.")
print("2. Προσαρμοσμένος πλυθησμός με προσαρμοσμένο παθογόνο παράγοντα.")
print("3. Έξοδος.\n")
swch = int(input("Παρακαλώ επιλέξτε: "))
#an dialexthke to 1 tote
if swch == 1:
 print("-----------------------------------")
 print("Προεπιλεγμένα παθογόνα \n")
 print("Παρακαλώ επιλέξτε ένα παθογόνο της παρακάτω λίστας:\n")
 print("1.Ιλαρας.")
 print("- Ένα εξεραιτικά μεταδιδόμενο παθογόνο.")
 ps = int(input("Παρακαλώ επιλέξτε: "))
 if ps == 1:
  pc = p1
  popCreate(pc)
 #alliws, an dialexthke to 2 tote
elif swch == 2:
 print("-----------------------------------")
 print("Προσαρμοσμένη λειτουργεία παθογόνου \n")
 name = raw_input("Εισάγετε το όνομα του παθογόνου: ")
 pType = raw_input("Εισάγετε τον τύπο του παθογόνου: ")
 taxID = raw_input("Εισάγετε το αναγνωριστικό ταξινομικής ταυτότητας NCBI(αν υπάρχει): ")
 disease = raw_input("Εισάγετε το όνομα της νόσου: ")
 R0 = raw_input("Εισάγετε το R0 του παθογόνου παράγοντα: ")
 per = raw_input("Εισάγετε την περίοδο μολυσματικότητας: ")
 pc = pathDef(name,pType,taxID,disease,R0,per)
 popCreate(pc)
 #alliws an dialexthke to 3 tote
elif swch == 3:
 print("")
 #diaforetika kapoio lathos egine
else:
 print("-----------------------------------")
 print("Έγινε κάποιο λάθος, παρακαλώ δοκιμάστε ξανά.")
 print("******************************************************************************")

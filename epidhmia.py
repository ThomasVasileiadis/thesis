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
 print("Statistika stoixeia: \n")
 print("Pathogono R0 se plhrws eyaisthito plythismo: {0}".format(str(r0)))
 print("Pathogonos periodos molysmatikothtas: {0} hmeres".format(str(ip)))
 print("Orio eyaisthisias: {0} atoma".format(str(si)))
 print("Anosologika atoma poy xreiasthkan gia thn prolhpsh ths epidhmias: {0} atoma".format(str(ii)))
 print("Orio katwflioy: {0}".format(str(th)))
 print("-----------------------------------\n")
 


#arxiko menu epiloghs
print("Kalws hlthate!\n")
print("1. Prosarmosmenos plythismos me proepilegmeno pathogono paragonta.")
print("2. Prosarmosmenos plythismos me Prosarmosmeno pathogono paragonta.")
print("3. Eksodos.\n")
swch = int(input("Parakalw epilekste: "))
#an dialexthke to 1 tote
if swch == 1:
 print("-----------------------------------")
 print("        Proepilegmena pathogona \n")
 print("Parakalw epilekste ena pathogono ths parakatw listas:\n")
 print("1. Ilaras.")
 print("- Ena eksairetika metadidomeno pathogono.")
 ps = int(input("Parakalw epilekste: "))
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

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from decimal import *
 
 
class pathDef(object):
 def __init__(self, path_name, path_type, taxid, syndrome_name, R0, ip):
  self.path_name = path_name
  self.path_type = path_type
  self.taxid = taxid
  self.syndrome_name = syndrome_name
  self.R0 = int(R0)
  a = Decimal(ip)
  self.ip = round(a,2)
 
 def printPath(self):
     print("Όνομα: " + self.path_name)
     print("Τύπος: " + self.path_type)
     print("Αναγνωριστικό NCBI: " + self.taxid)
     print("Αιτιώδης παράγοντας της " + '"' + self.syndrome_name + '"')
     print("Μέση μολυσματική περίοδος: " + str(self.ip) + " ημέρες")
 
 def getR0(self):
  return self.R0
 
 def getB(self):
  b = self.R0 * (1/self.ip)
  return b
 
 def getPeriod(self):
  return self.ip
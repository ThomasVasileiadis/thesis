#!/usr/bin/env python
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
  print("Onoma: " + self.path_name)
  print("Typos: " + self.path_type)
  print("Anagnwristiko NCBI: " + self.taxid)
  print("Aitiwdhs paragontas ths " + '"' + self.syndrome_name + '"')
  print("Mesh molysmatikh periodos: " + str(self.ip) + " hmeres")
 
 def getR0(self):
  return self.R0
 
 def getB(self):
  b = self.R0 * (1/self.ip)
  return b
 
 def getPeriod(self):
  return self.ip
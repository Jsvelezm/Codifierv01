# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import re #this library is useful to work with regular expresions

# import xlrd
# import openpyxl
import pandas as pd # pandas if is necesary
import numpy as np # numpy if is necesary
import csv # useful to import csv files 
with open("prueba.txt") as f:
    reader = csv.reader(f, delimiter="\t") # this read a line and separate by colums 
    d = list(reader)



len(d[0][1])# return the number of letters on a string 
print(d[0][1]) # return the value stored in a the row 0 colum 1





len(d) # returns the length of the stored values 


jaime = [] #     this is the way to declare a list 

for i in range(len(d)):
    jaime.append(d[i][0])
    
print(jaime)    
 

print(d[0])
print (d[0][2])
print(d[1][0])
str = 'la cultura o la multicultura o la pluricultura o la pluriculturalidad o la cultúñera'
patron = re.compile(r"\w*cultú\w*", flags=re.IGNORECASE)
coinci = patron.findall(str)



def guarda(d, colum):    
    aux = []
    for i in range(len(d)):
        aux.append(d[i][colum])
    
    print(aux)    
    return aux

cosa = guarda(d,0)

gurada()



def npal (x,y):
   patron = re.compile(r"\w*cultú\w*", flags=re.IGNORECASE)
   coinci = patron.findall(str)
   return coinci





















print(len(coinci))
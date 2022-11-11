############## IMPORTS#################################
from CU import main
from translate import AtoTandAppend, TtoA, AtoTandWrite
from bios import inputascii, outputascii,pushtotxt, memorydump
import os
#######################################################

##########################################################

print("Welcome to my ternary code editor, I guess this is basically the equivilant to assembly? idrk im not sure")
print("---------------------------------------------------\n")

##########################################################

def menu():
  print("1. New file\n2. Print current file in assembly\n3. Print current file in ternary\n4. Append to end of current file\n5. Run current file\n6. More options\n7. Quit")
  option = int(input(">> ")) #at some point ill add vaildation here
  if option == 1:
    os.system("clear")
    AtoTandWrite()
  elif option == 2:
    os.system("clear")
    TtoA()
  elif option == 3:
    printternary()
  elif option == 4:
    os.system("clear")
    AtoTandAppend()
  elif option == 5:
    print("\nExecuted current file\n")
    main()
  elif option == 7:  
    quit()
  else:
    devmenu()

##########################################################

def printternary():
  os.system("clear")
  print("\n***********************")
  file = open("DataInstructions.ter")
  for line in file:
    line = line.strip("\n")
    print(line)
  print("***********************\n")

##########################################################
def devmenu():
  os.system("clear")
  print("1. Output Ascii chars\n2. Input Ascii codes\n3. Display memory changes\n4. Write assembly to file\n\n\n99. Go Back")
  option = int(input(">> "))
  if option == 1:
    os.system("clear")
    outputascii()
  elif option == 2:
    os.system("clear")
    inputascii()
  elif option == 3:
    os.system("clear")
    memorydump()
  elif option == 4:
    os.system("clear")
    pushtotxt()
  else:
    os.system("clear")
    menu()
  
##########################################################  
while True:
  print("\n")
  menu()
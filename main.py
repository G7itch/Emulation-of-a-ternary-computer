############## IMPORTS#################################
from CU import main
from translate import AtoTandAppend, TtoA, AtoTandWrite
#######################################################

##########################################################

print("Welcome to my ternary code editor, I guess this is basically the equivilant to assembly? idrk im not sure")
print("---------------------------------------------------------\n")

##########################################################

def menu():
  print("1. New file\n2. Print current file in assembly\n3. Print current file in ternary\n4. Append to end of current file\n5. Run current file\n6. Quit")
  option = int(input(">> ")) #at some point ill add vaildation here
  if option == 1:
    AtoTandWrite()
  elif option == 2:
    TtoA()
  elif option == 3:
    pt()
  elif option == 4:
    AtoTandAppend()
  elif option == 5:
    print("\nExecuted current file\n")
    main()
  else:  
    quit()

##########################################################

def pt():
  print("\n***********************")
  file = open("DataInstructions.ter")
  for line in file:
    line = line.strip("\n")
    print(line)
  print("***********************\n")

  
##########################################################
##########################################################  
while True:
  menu()
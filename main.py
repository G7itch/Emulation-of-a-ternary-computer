from runonce import main
from translate import AtoT, TtoA

print("Welcome to my ternary code editor, I guess this is basically the equivilant to assembly? idrk im not sure")
print("---------------------------------------------------------\n")

##########################################################

def menu():
  print("1. New file\n2. Print current file in assembly\n3. Print current file in ternary\n4. Append to end of current file\n5. Run current file\n6. Quit")
  option = int(input(">> ")) #at some point ill add vaildation here
  if option == 1:
    newfile()
  elif option == 2:
    TtoA()
  elif option == 3:
    pt()
  elif option == 4:
    addtofile()
  elif option == 5:
    main()
  else:  
    quit()

##########################################################

def newfile():
  pass

##########################################################

def pt():
  pass

##########################################################

def addtofile():
  pass

##########################################################
##########################################################  

menu()
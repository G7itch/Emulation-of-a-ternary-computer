########### IMPORTS ###########
from dectoter import DecToTer##
###############################
# ADD MORE OPERATIONS!!!!
###############################

############################################################
def add(one,two,sto):
  file = open("memory.ter", "r")
  content = file.readlines()
  num1 = (content[one].strip("\n"))
  num2 = (content[two].strip("\n"))
  
  res = (int(num1,3) + int(num2, 3)) #Converts from base 3 to base 10
  a = str(DecToTer(res))
  a = "0"*(8-len(a)) + a # pads the ternanry number so it has 8 bits
  
  file.close()
  
  file = open("memory.ter", "r")
  content = file.readlines()
  content[sto] = a + "\n" 
  file.close()
  
  file = open("memory.ter", "w")
  file.writelines(content)
  file.close()
############################################################

def sub(one,two,sto):
  file = open("memory.ter", "r")
  content = file.readlines()
  
  num1 = (content[one].strip("\n"))
  num2 = (content[two].strip("\n"))
  res = (int(num1,3) - int(num2, 3))
  
  if abs(res) != res:
    res = 0 #If subtraction gives a negative answer revert to "00000000"
    
  a = str(DecToTer(res))
  a = "0"*(8-len(a)) + a
  
  file.close()
  
  file = open("memory.ter", "r")
  content = file.readlines()
  content[sto] = a + "\n" 
  file.close()
  
  file = open("memory.ter", "w")
  file.writelines(content)
  file.close()
#############################################################
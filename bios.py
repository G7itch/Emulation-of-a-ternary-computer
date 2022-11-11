from translate import TtoA
from CU import main
#############################################################################

def inputascii():
  print("Enter number of characters to save")

#############################################################################

def outputascii():
  pass

#############################################################################

def memorydump():
  file = open("memory.ter","r")
  tempfile = open("memory.old","w")
  content = file.readlines()
  
  for line in content:
    tempfile.write(line) 
  file.close()
  tempfile.close()
  
  main()
  
  file1 = open("memory.ter","r")
  tempfile1 = open("memory.old","r")
  content = file1.readlines()
  content2 = tempfile1.readlines()
  for i in range(0,len(content2)-1):
    if content[i] != content2[i]:
      a = content[i].strip("\n")
      b = content2[i].strip("\n")
      print(i,"|",b,"->",a)
  
  file1.close()
  tempfile1.close()

#############################################################################

def pushtotxt():
  filename = input("Enter the filename to output to: ")
  file = open(filename + ".txt","w")
  tlist = TtoA()
  for line in tlist:
    file.write(line + "\n")
  file.close()
  
from dectoter import DecToTer

def add(one,two,sto):
  file = open("memory.ter", "r")
  content = file.readlines()
  num1 = (content[one].strip("\n"))
  num2 = (content[two].strip("\n"))
  res = (int(num1,3) + int(num2, 3))
  a = str(DecToTer(res))
  a = "0"*(8-len(a)) + a
  file.close()
  if sto >= len(content):
    file = open("memory.ter", "a")
    file.write("placeholder\n")
    file.close()
  
  file = open("memory.ter", "r")
  content = file.readlines()
  content[sto] = a + "\n"   
  file.close()
  
  file = open("memory.ter", "w")
  file.writelines(content)
  file.close()

def sub(one,two,sto):
  file = open("memory.ter", "r")
  content = file.readlines()
  num1 = (content[one].strip("\n"))
  num2 = (content[two].strip("\n"))
  res = (int(num1,3) - int(num2, 3))
  a = str(DecToTer(res))
  a = "0"*(8-len(a)) + a
  file.close()
  if sto >= len(content):
    file = open("memory.ter", "a")
    file.write("placeholder\n")
    file.close()
  
  file = open("memory.ter", "r")
  content = file.readlines()
  content[sto] = a + "\n"   
  file.close()
  
  file = open("memory.ter", "w")
  file.writelines(content)
  file.close()
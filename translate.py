from dectoter import DecToTer

def AtoTandAppend():
  print("\nAnything you add after the starred line will be appended to the existing program (press ENTER to quit)")
  TtoA()
  file = open("DataInstructions.ter", "at")
  datainstructions = []
  add = input("-> ")
  while add != "":
    datainstructions.append(add)
    add = input("-> ")
  
  for entry in datainstructions:
    entry = entry.split(" ")
    data,instruct = entry[1],entry[0]
    
    if instruct == "ADD":
      file.write("001\n")
      data = [int(i) for i in data.split(",")]
      for i in range(0,len(data)):
        a = str(DecToTer(data[i]))
        data[i] = "0"*(8-len(a)) + a
      b = "".join(map(str,data))
      b = b + "\n"
      file.write(b)
      
    elif instruct == "SUB":
      file.write("002\n")
      data = [int(i) for i in data.split(",")]
      for i in range(0,len(data)):
        a = str(DecToTer(data[i]))
        data[i] = "0"*(8-len(a)) + a
      b = "".join(map(str,data))
      b = b + "\n"
      file.write(b)
    
    elif instruct == "SET":
      file.write("000\n")
      data = int(data)
      a = str(DecToTer(data))
      data = "0"*(8-len(a)) + a
      b = data + "\n"
      file.write(b) 

      
  file.close()
  print("***********************")
  print("File appended to succesfully\n")
  
###########################################################
###########################################################
 
def AtoTandWrite():
  print("\nAnything you add after the starred line will be written to a new current program overriding the existing one (press ENTER to quit)")
  file = open("DataInstructions.ter", "w")
  datainstructions = []
  print("\n***********************")
  add = input("-> ")
  while add != "":
    datainstructions.append(add)
    add = input("-> ")
  
  for entry in datainstructions:
    entry = entry.split(" ")
    data,instruct = entry[1],entry[0]
    
    if instruct == "ADD":
      file.write("001\n")
      data = [int(i) for i in data.split(",")]
      for i in range(0,len(data)):
        a = str(DecToTer(data[i]))
        data[i] = "0"*(8-len(a)) + a
      b = "".join(map(str,data))
      b = b + "\n"
      file.write(b)
      
    elif instruct == "SUB":
      file.write("002\n")
      data = [int(i) for i in data.split(",")]
      for i in range(0,len(data)):
        a = str(DecToTer(data[i]))
        data[i] = "0"*(8-len(a)) + a
      b = "".join(map(str,data))
      b = b + "\n"
      file.write(b)

    elif instruct == "SET":
      file.write("000\n")
      data = int(data)
      a = str(DecToTer(data))
      data = "0"*(8-len(a)) + a
      b = data + "\n"
      file.write(b) 
      
  file.close()
  print("***********************")
  print("File written to succesfully\n") 

  
###########################################################
###########################################################
  
def TtoA():
  tlist = []
  print("\n***********************")
  file = open("DataInstructions.ter", "r")
  content = file.readlines()
  temp = []
  datainstructions = ["*" for i in range(len(content)//2)]
  #print(datainstructions)  

  for i in range(0,len(content)):
    content[i] = content[i].strip("\n")
  j = 0
  for i in range(0,len(content)-1):
    if i % 2 == 0:
      datainstructions[j] = str(content[i]) + " " + str(content[i+1])
      j += 1
  
  file.close()
  for entry in datainstructions:
    entry = entry.split(" ")
    data,instruct = entry[1],entry[0]
    if instruct == "001":
      instruct = "ADD"
      data = [data[i:i+8] for i in range(0, len(data), 8)]
      for i in range(0,len(data)):
        data[i] = int(data[i],3)
      
    elif instruct == "002":
      instruct = "SUB"
      data = [data[i:i+8] for i in range(0, len(data), 8)]
      for i in range(0,len(data)):
        data[i] = int(data[i],3)

    elif instruct == "000":
      instruct = "SET"
      data = [data[i:i+8] for i in range(0, len(data), 8)]
      for i in range(0,len(data)):
        data[i] = int(data[i],3)
    
    tlist.append(instruct + " " + ",".join(map(str,data)))  
    print(instruct,",".join(map(str,data)))
      
  print("***********************\n")
  return tlist
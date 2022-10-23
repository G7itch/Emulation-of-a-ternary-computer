def AtoT():
  pass

###########################################################
###########################################################
  
def TtoA():
  print("\n***********************")
  file = open("DataInstructions.ter", "r")
  content = file.readlines()
  temp = []
  datainstructions = []
  
  for i in range(1,len(content)+1):
    if i % 3 == 0:
      temp = []
    
    line = content[i-1].strip("\n")
    temp.append(line)
    
    if i % 2 == 0:
      test = " ".join(temp)
      datainstructions.append(test)
  
  for entry in datainstructions:
    entry = entry.split(" ")
    data,instruct = entry[0],entry[1]
    
    if data == "001":
      data = "ADD"
      instruct = [instruct[i:i+8] for i in range(0, len(instruct), 8)]
      for i in range(0,len(instruct)):
        instruct[i] = int(instruct[i],3)
      
    elif data == "002":
      data = "SUB"
      instruct = [instruct[i:i+8] for i in range(0, len(instruct), 8)]
      for i in range(0,len(instruct)):
        instruct[i] = int(instruct[i],3)
      
    print(data,",".join(map(str,instruct)))
        
  print("***********************\n")
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
      
    print(instruct,",".join(map(str,data)))
        
  print("***********************\n")
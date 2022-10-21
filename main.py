from Add import add

file = open("DataInstructions.ter", "r")
datainstruct = []
for count, line in enumerate(file):
  count += 1
  line = line.strip("\n")
  datainstruct.append(line)

file.close()

#print(datainstruct)

cnt = 1
commands = {
  "000" : "data",
  "001" : "add"
}


for count, ele in enumerate(datainstruct):
  if cnt % 2 == 1:
    instruct = ele
    #print(instruct)
    if instruct == "001":
      data = [datainstruct[count+1][i:i+8] for i in range(0, len(datainstruct[count+1]), 8)]
      one,two,sto = [(int(str(i),3)-1) for i in data]
      #print(one,two,sto)
      add(one,two,sto)
  else:
    pass
    #data = [ele[i:i+8] for i in range(0, len(ele), 8)]
    #print(data)
    #data = [(int(str(i),3)-1) for i in data]
    #print(data)
  cnt += 1  
######### IMPORTS #########
from ALU import add,sub,set#
###########################

#Command list for use in DataInstructions, just to keep track of everything

commands = {"000": "set memory location to 0",
            "001": "add",
            "002": "subtract"
           }

###########################################################################
###########################################################################
def main():
  file = open("DataInstructions.ter", "r")
  datainstruct = []
  for count, line in enumerate(file):
      count += 1
      line = line.strip("\n")
      datainstruct.append(line)
  
  file.close()
  ###########################################################################
  
  cnt = 1 #Dont know what this is or how it is different to "count" but ok
  
  ##########################################################################
  #################THE CODE BELOW WAS WRITTEN YONDERS AGO, #################
  #################IDK HOW IT WORKS OR WHAT I WAS THINKING #################
  #################BUT IT WORKS MOST OF THE TIME           #################
  ##########################################################################
  
  for count, ele in enumerate(datainstruct):
      if cnt % 2 == 1:
          instruct = ele #Not sure why this is here
          data = [
              datainstruct[count + 1][i:i + 8]
              for i in range(0, len(datainstruct[count + 1]), 8) #splits into 3x ternary byte
          ]
          if instruct == "001":
              one, two, sto = [(int(str(i), 3) - 1) for i in data] #
              add(one, two, sto)
          elif instruct == "002":
              one, two, sto = [(int(str(i), 3) - 1) for i in data]
              sub(one, two, sto)
          elif instruct == "000":
            one = int("".join(map(str,[(int(str(i), 3) - 1) for i in data])))
            set(one)
  
      else:
          pass
      cnt += 1

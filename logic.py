def tnand(x,y):
  x,y = int(x), int(y)
  match x:
    case 0:
      return 2
    case 1:
      match y:
        case 0:
          return 2
        case _:
          return 1
    case 2:
      return abs(2-y)

def tinv(x):
  x = int(x)
  if x == 0:
    return 2
  elif x == 2:
    return 0
  else:
    return 1

def txor(x,y):
  x, y = int(x),int(y)
  match x:
    case 0:
      return y
    case 1:
      if y == 0:
        return 1
      elif y == 1:
        return 0
      else:
        return 2
    case 2:
      return 2


#I didnt write this, idk who did but its not my fault if it breaks

def DecToTer(num):
    quotient = num/3
    remainder = num%3
    if quotient == 0:
        return ""
    else:
        return DecToTer(int(quotient)) + str(int(remainder))
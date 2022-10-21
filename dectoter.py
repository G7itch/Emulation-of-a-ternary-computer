def DecToTer(num):  #2
    quotient = num/3    #3
    remainder = num%3
    if quotient == 0:   #4
        return ""
    else:
        return DecToTer(int(quotient)) + str(int(remainder))
def findvalue(mydict, val):
    listofkeys = []
    
    for x in mydict:
        if mydict[x] == val:
            listofkeys.append(x)
    
    return listofkeys
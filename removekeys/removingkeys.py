def removekeys(mydict, keylist):
    newdict = {}
    newdict2 = {}
    for x in mydict:
        for y in range(len(keylist)):
            if x == keylist[y]:
                newdict[x] = mydict[x]
        if mydict.get(x) != newdict.get(x):
            newdict2[x] = mydict[x]

    return newdict2    
    
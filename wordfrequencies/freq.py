def wordfrequencies(mylist):
    mydict = {}
    
    for x in mylist:
        mydict.setdefault(x , mylist.count(x))
    
    return mydict
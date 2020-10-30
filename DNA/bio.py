def kmercounts(dna:str , k:int):
    mydict = {}
    
    for x in range(len(dna)):
        kmer = dna[x , k+x ]
        mydict.setdefault(x+1 , kmer)
    
    return mydict
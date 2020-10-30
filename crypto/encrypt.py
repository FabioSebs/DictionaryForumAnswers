def code(key , phrase):
    encoded = []
    
    for x in range(len(phrase)):
        for y in key:
            if phrase[x] == key[y]:
                encoded.append(y)  
         
    return encoded       

                
                
        
    
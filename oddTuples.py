def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    oddTuple = ()
    for i in range(0,len(aTup)+1):
        if i%2!=0:
            oddTuple += (aTup[i-1],)
    return oddTuple
    
    

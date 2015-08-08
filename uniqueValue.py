def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    List=[]
    for x in aDict.keys():
        Temp = aDict.values()
        Temp.remove(aDict[x])
        if aDict[x] in Temp:
            continue
        else: 
            List.append(x)
    List.sort()
    return List

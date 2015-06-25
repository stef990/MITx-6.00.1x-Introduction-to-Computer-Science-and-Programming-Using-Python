 # Paste your code into this box 
longest=''
current=''
#Use two place holders, one for the current sequence we are building
#and one for keeping track of what we think is the longest sequence
for x in s:
    if(current==''): #start building sequence
        current=x
    elif(current[-1]<=x): #if previous character in current sequence is less, than added following character in s
            current+=x
    elif(current[-1]>x): #if this condition is met sequence is stopped
        if(len(longest)<len(current)):#this is our newest longest sequence
            longest=current
            current=x#restart current sequence
        else: #this is not the longest sequence
            current=x
if(len(current)>len(longest)): # if the last sequence we ran is the longest, reassign
    longest=current
print(longest) 

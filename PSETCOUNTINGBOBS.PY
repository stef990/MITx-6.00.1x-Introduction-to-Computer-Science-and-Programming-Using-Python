 # Paste your code into this box 
numBob = 0
for x in range(len(s)):
    if s[x:x+3] =='bob':
        numBob+=1
print 'Number of times bob occurs is: ' + str(numBob)

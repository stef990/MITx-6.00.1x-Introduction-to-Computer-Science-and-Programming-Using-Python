for y in range (10,1000,10):
    #balance = 3329
    #annualInterestRate = 0.2
    unpaidbalance = balance
    for x in range(1,13):
        unpaidbalance = (unpaidbalance - y)
        unpaidbalance = unpaidbalance + (unpaidbalance*(annualInterestRate/12))
    if(unpaidbalance<=0):
        print('Lowest Payment: ') +'%i'%(y)
        break

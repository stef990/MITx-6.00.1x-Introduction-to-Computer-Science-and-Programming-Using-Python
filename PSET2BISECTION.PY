#balance = 999999
#annualInterestRate = 0.18
MIR = annualInterestRate/12
LB = balance/12
UB = (balance*(1+(annualInterestRate/12))**12)/12
MP = (LB+UB)/2
Error = 0.01 #smallest unit

unpaidbalance = balance

while unpaidbalance >Error:
    MP = (UB+LB)/2
    for x in range(1,13):
        unpaidbalance = (unpaidbalance - MP)
        unpaidbalance = unpaidbalance + (unpaidbalance*(MIR))
    if(unpaidbalance<0):
        UB = MP
        unpaidbalance = balance
    elif(unpaidbalance>Error):
        LB =MP
        unpaidbalance = balance
print('Lowest Payment: ') +'%.2f'%(MP)

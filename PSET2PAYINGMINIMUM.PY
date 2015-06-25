# Paste your code into this box
totMMP=0
for x in range(1,13):
    print('Month: '+str(x))
    MMP = balance*monthlyPaymentRate
    totMMP +=MMP
    print('Minimum monthly payment:')+'%.2f'%(MMP)
    unpaidbalance = balance - MMP
    balance =unpaidbalance + (unpaidbalance*(annualInterestRate/12))
    print('Remaining balance: ')+'%.2f'%(balance)
print('Total Paid: ') + '%.2f'%(totMMP)
print('Remaining balance: ') + '%.2f'%(balance)

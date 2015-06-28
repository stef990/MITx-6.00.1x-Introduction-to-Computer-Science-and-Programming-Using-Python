print('Please think of a number between 0 and 100!')

epsilon = 1
low = 0
high = 100
ans = (high + low)/2

while ans >= epsilon:
    print('Is your secret number ' + str(ans) + ' ?')
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low"), 
    print("Enter 'c' to indicate I guessed correctly."),
    n = raw_input()
    if (n=='h'):
        high=ans
        low = low
        ans = (high + low)/2
    elif(n=='l'):
        high=high
        low = ans
        ans = (high + low)/2
    elif(n=='c'):
        break
    else:
        print('Sorry, I did not understand your input.')
        #print('Is your secret number ' + str(ans) + ' ?')      
        ans = (high + low)/2
print('Game over. Your secret number was: ' + str(ans))

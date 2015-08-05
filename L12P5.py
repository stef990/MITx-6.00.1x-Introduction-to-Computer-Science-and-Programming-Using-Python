def genPrimes():
    Prime = []
    number = 1
    while True:
        number += 1
        for p in Prime:
            if number%p == 0 :
                break
        else:
            Prime.append(number)
            yield number
            
x = 0 
for n in genPrimes():
	x+=1
	print x, n

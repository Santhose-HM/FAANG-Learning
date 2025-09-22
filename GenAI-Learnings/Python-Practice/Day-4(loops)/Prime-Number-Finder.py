for num in range(1,201):
    if num > 1:
        isPrime = True
        for i in range(2,num):
            if num%i==0:
                isPrime = False
                break
        if isPrime:
            print(num,end=",")

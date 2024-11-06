def is_prime(num):
    if(num == 0 or num == 1 or num < 0):
        return False
    else:
        isPrime = True
        n = num//2
        for i in range(2,n+1,1):
            if(num%i == 0):
                return False
        return True
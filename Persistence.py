def persistence(n):
    
    num = 1
    mul = 0
    
    while len(str(n)) > 1:
        num = 1
        for i in str(n):
            num = num * int(i)
        n = num
        mul = mul + 1
    return mul
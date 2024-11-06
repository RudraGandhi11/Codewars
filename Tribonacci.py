def tribonacci(signature, n):
    series_list = signature
    for i in range(2,n-1,1):
        series_list.append(series_list[i]+series_list[i-1]+series_list[i-2])
    return series_list[0:n:1]
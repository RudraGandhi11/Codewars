def find_uniq(arr):
    counter = {}
    
    for i in arr:
        if(i in counter.keys()):
            counter[i] = counter[i] + 1
        else:
            counter[i] = 1
    
    for i in counter:
        if(counter[i] == 1):
            return i
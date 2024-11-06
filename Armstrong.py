def narcissistic( value ):

    new_value = 0
    temp_value = value
    check_value = value
    length = 0
    
    while temp_value > 0:
        length = length + 1
        temp_value = temp_value//10
        
    while value > 0:
        remainder = value%10
        value = value//10
        new_value = remainder**length + new_value
        
    if new_value == check_value:
        return True
    else:
        return False
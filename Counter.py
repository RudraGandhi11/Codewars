def find_it(seq):
    num_counter_dict = {}
    for i in seq:
        if(i in num_counter_dict.keys()):
            num_counter_dict[i] = num_counter_dict[i] + 1
        else:
            num_counter_dict[i] = 1
    for i in num_counter_dict:
        if(num_counter_dict[i]%2 == 1):
            return i
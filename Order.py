def order(sentence):
    
    new_sent = ""
    words = sentence.split(' ')
    num_in_word = []
    words_dict = {}
    
    for i in words:
        for j in i:
            if(j in ['1','2','3','4','5','6','7','8','9']):
                num_in_word.append(int(j))
                words_dict[int(j)] = i
    
    for i in range(len(num_in_word)-1,0,-1):
        for j in range(i):
            if(num_in_word[j] > num_in_word[j+1]):
                temp = num_in_word[j+1] 
                num_in_word[j+1] = num_in_word[j]
                num_in_word[j] = temp
                
    for i in num_in_word:
        new_sent = new_sent + words_dict[i] + ' '
    
    return new_sent.strip()
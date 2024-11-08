""" Simple, given a string of words, return the length of the shortest word(s).
 
String will never be empty and you do not need to account for different data types.  """

def shortest_string(sentence):
    words = sentence.split(' ')
    shortest = words[0]
    for i in words:
        if(len(i)<len(shortest)):
            shortest = i
    return shortest

print(shortest_string('hi my name is rudra 1'))
print(shortest_string('adhjb aiwdh aiwbai dasha dwig s fe diuah idua'))
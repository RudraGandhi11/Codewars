""" An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case. 

Example: (Input --> Output) 

"Dermatoglyphics" --> true 

"aba" --> false 

"moOse" --> false (ignore letter case)  """

def isogram(word):
    word1 = word.lower()
    counter = {}
    for i in word1:
        if(i in counter.keys()):
            return False
        else:
            counter[i] = 1
    return True

print(isogram("Dermatoglyphics"))
print(isogram("aba"))
print(isogram("moOse"))
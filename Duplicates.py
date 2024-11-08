""" Count the number of Duplicates 
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example: 

"abcde" -> 0 # no characters repeats more than once 

"aabbcde" -> 2 # 'a' and 'b' 

"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`) 

"indivisibility" -> 1 # 'i' occurs six times 

"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice 

"aA11" -> 2 # 'a' and '1' 

"ABBA" -> 2 # 'A' and 'B' each occur twice  """

def duplicates(word):
    word1 = word.lower()
    counter = {}
    counter_letter = 0
    for i in word1:
        if(i in counter.keys()):
            counter[i] = counter[i] + 1
        else:
            counter[i] = 1
    
    for v in counter.values():
        if(v>1):
            counter_letter = counter_letter + 1
    return counter_letter

print(duplicates("abcde"))
print(duplicates("aabbcde"))
print(duplicates("aabBcde"))
print(duplicates("indivisibility"))
print(duplicates("Indivisibilities"))
print(duplicates("aA11"))
print(duplicates("ABBA"))
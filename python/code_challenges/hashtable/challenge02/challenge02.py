# Write here the code challenge solution

from collections import Counter
 
# Python program to find the first
# repeated character in a string
def firstRepeatedWord(sentence):
 
    # splitting the string
    lis = list(sentence.split(" "))
     
    # Calculating frequency of every word
    frequency = Counter(lis)
     
    # Traversing the list of words
    for i in lis:
       
        # checking if frequency is greater than 1
         
        if(frequency[i] > 1):
            # return the word
            return i
        else : return "No Repetition"
 
 
if __name__ == "__main__":

    sentence = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    print(firstRepeatedWord(sentence))

    sentence = "I am learning programming at ASAC."
    print(firstRepeatedWord(sentence))

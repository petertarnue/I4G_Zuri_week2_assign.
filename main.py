# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram():
    # [assignment] Add your code here
    
    # Ask the user for their word input
    word = input("Enter a word \n")

    # Ask the user for the word that they want to check if it is an anagram
    anagram = input("Enter a another word to see if it is an angram \n")
    
    # check if the lenght of the word and anagram are the same
    if len(word) == len(anagram):

        # change word and anagram to a unique case
        lowercase_word = word.lower()
        lowercase_anagram = anagram.lower()

        # sort word and anagram
        sorted_word = sorted(lowercase_word)
        sorted_anagram = sorted(lowercase_anagram)

        # check if char in words are the same
        if sorted_word == sorted_anagram:
            # return True if the characters in the words are the same
            return True
        # return False if the characters in the words are not the same    
        return False
    else:
        # return False if the length of the words are not equal
        return False


print(find_anagram())



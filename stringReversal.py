# Homework 7: String Manipulation
[White Python]
10/09/2023

### Exercise 1:

def reverseVerticalPrint(word):
    letters = ""
    for i in word:
        letters = i + letters
    print(letters)


def stringReversal(word1,word2):
    if len(word1) != len(word2):
        return False

    for i in range(len(word1)):
        if word1[i] != word2[len(word2) - 1 - i]:
            return False
    
    return True


def isPalindrome(word):
    return stringReversal(word,word)
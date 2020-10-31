# first challenge
def palindrome(str):
    j = len(str) - 1
    for i in str:
        if i != str[j]:
            return False
        j -= 1
    return True

print(palindrome("aadaa"))


if text[i]!=text[len(text)-i-1]:
    return False

# Is Palindrome
# --------------------------------------------------------------------------------
# Strings like "Able was I, ere I saw Elba" or "Madam, I'm Adam" could be considered palindromes,
#  because (if we ignore spaces, punctuation and capitalization) the letters are the same from front and back. 
# Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar", 
# return true. Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.
# def IsPalindrome(string):
#     newString=""
#     for i in range(len(string)-1,-1,-1):
#         newString+=string[i]
#     if newString==string:
#         return True
#     else:
#         return False
# print(IsPalindrome("hello"))

# Longest Palindrome
# --------------------------------------------------------------------------------
# For this challenge, we will look not only at the entire string, but also substrings within it. For a string,
#  return the longest palindromic substring. Given "what u


# def LongestPalindrome(string):
#     count = 0 
#     newString=""
#     # stringList=[]
#     LongPalindrome = ""
#     for i in string:
#         if i != ' ':
#             newString += i
#         elif i == ' ':
#             # stringList.append(newString)
#             print("String : ", newString)
#             print("newStrin", newString)
#             if palindrome(newString):
#                 print("here inside firts if")
#                 if len(newString) > count:
#                     count = len(newString)
#                     LongPalindrome = newString
#                     print("here inside the inner if")
#         print(newString)
#         newString=""
#     print(LongPalindrome)  


# LongestPalindrome("what up, dada ?")
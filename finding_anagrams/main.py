# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram():
    # [assignment] Add your code here
    #Take user input
    user_input1=input("Enter first string:  ")
    user_input2=input("Enter second string:   ")

    #sort strings alphabetically
    sorted_str1=sorted(user_input1)
    sorted_str2=sorted(user_input2)

    #compare strings to check if they are anagram of each other
    if sorted_str1 == sorted_str2:
        print("Inputted strings are anagram of each other")
        #return True
    else:
        print("Inputted strings are not anagram of each other")
        #return False
find_anagram()

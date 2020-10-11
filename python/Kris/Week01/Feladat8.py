def palindrome(input):
    length = len(input)
    palindromes = []
    for i in range(1,length+1):
        min = 0
        while (min+i) < length+1:
            print(input[min:(min+i)])
            if(input[min:(min+i)] == input[min:(min+i)][::-1]) and len(input[min:(min+i)]) >= 3:
                palindromes.append(input[min:(min+i)])
            min = min+1
    return palindromes

print(palindrome("dog goat dad duck doodle never"))
print(palindrome("racecar"))

"""
string_to_search = "Jakakaj"
string_to_search2 ="dog goat dad duck doodle never"
string_to_search3 ="apple"
string_to_search4 =""
def isPalindrome(string_to_manipulate):
    length = len(string_to_manipulate)
    palindromes = []
    substrings = []
for i in range(length):
        for j in range(i, length - 2):
          substrings += [string_to_manipulate[i:j+3]]
    for string in substrings:
        string = string.lower()
        if(string == string[::-1]):
            palindromes += [string]
print(isPalindrome(string_to_search))
print(isPalindrome(string_to_search2))
print(isPalindrome(string_to_search3))
print(isPalindrome(string_to_search4))
"""

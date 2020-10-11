def GetMostCommonLetters( text):
    dictionary = {}
    for char in text.replace(" ", ""):
        if char in dictionary :
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    dictionary = sorted(dictionary, key=dictionary.get, reverse=True)
    mostCommonCharacters = "The most common characters in descending order are: "
    for index in range(0,3):
        mostCommonCharacters += f"{dictionary[index]} "
    return mostCommonCharacters

# vagy

def most_recent_char(my_string):
    most_recent_char = []
    my_string = my_string.lower()
    my_tuple = tuple(my_string)
    my_dictionary = dict()
    for char in my_tuple:
        if char in my_dictionary:
            continue
        else:
            my_dictionary[char] = my_tuple.count(char)
    values = list(my_dictionary.values())
    values.sort(reverse=True)
    for i in range(0,3):
        for char, frequency in my_dictionary.items():
            if(frequency == values[i]):
                most_recent_char.append(char)
                break  
    return most_recent_char

# vagy

"""
from collections import Counter
def mostComonCharacters(inputStr):
    characters = inputStr.lower()
    dictionary = {}
    for letters in characters:
        if letters in dictionary:
            dictionary[letters] += 1
        else:
            dictionary[letters] = 1
    topThree = Counter(dictionary).most_common(3)
    for i in topThree: 
        print(i[0]," :",i[1]," ")
name = "blabla"
mostComonCharacters(name)
"""

def count_letters(text):
    count = {}
    for letter in text:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    output = []
    while len(output) < 3:
        max_count = 0
        letter = ''
        for key, value in count.items():
            if max_count < value:
                max_count = value
                letter = key
        output.append(letter)
        del count[letter]
    return output

print(count_letters('abcabcffffgh'))
numbers = [8, 42, 144, 2020]

for i, number in enumerate(numbers):
    print(i)
    print(number)

for i, char in enumerate('apple'):
    print(i, char)

elements = {'H': 1, 'He': 2, 'Li': 3}

for key, value in elements.items():
    print(key, value)

n0, n1, *rest = numbers

print(n0, n1, rest)
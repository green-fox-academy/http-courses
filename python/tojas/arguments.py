i = 0
s = 'hello'
numbers = [1,2,3]

def take_args(i, s, numbers):
    i += 1
    s += 'ka'
    numbers.append(4)

take_args(i, s, numbers)
print(i)
print(s)
print(numbers)
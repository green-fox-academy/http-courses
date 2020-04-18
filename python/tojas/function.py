x = 5

def hello(name):
    global x
    x = 6
    print('Hello: ' + name)
    print(x)

hello('Tojas')
print(x)

def add(a, b):
    summa = a + b
    return summa
    print('en meg itt vagyok')

print(add(4, 5))

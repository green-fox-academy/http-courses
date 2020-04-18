n = 3
if n > 4:
    print('nagyobb mint negy')
elif n > 2:
    print('nagyobb mint ketto');
else:
    print('kissebb vagy egyenlo mint ketto')
print('vege az ifnek')

n2 = 0

while n2 < 10:
    print(n2)
    if (n2 == 4):
        break
    n2 += 1
else:
    print('vege a while-nak')

numbers = [1,2,3,4]

for number in numbers:
    print(number)

for i in range(100,0,-7):
    print(i)
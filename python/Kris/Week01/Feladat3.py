for i in range(1, 101):
    if (i % 3 == 0) and (i % 7 == 0):
        print("PiffPuff")
    elif i % 3 == 0:
        print("Piff")
    elif i % 7 == 0:
        print("Puff")
    else:
        print(i)

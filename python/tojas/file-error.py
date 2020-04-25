try:
    print('elotte')
    #print(1 / 0)
    file = open('text.txt', 'r')
    print('utana')
    #[1,2][4]
    raise Exception('na')
    file.read()
    file.close()
except FileNotFoundError:
    print('ajjaj nem sikerult a filet megynyitni...')
except ZeroDivisionError:
    print('ne ossza\' nullaval nem vagy csaknorisz')
except Exception as e:
    print(e)
    print('ma nem is tudom mi tortent')
else:
    print('else')
finally:
    print('vege')
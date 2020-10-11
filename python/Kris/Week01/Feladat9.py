def isArmstrongNumber(inputNumber):
    order = len(str(inputNumber))
    sum = 0
    temp = inputNumber
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if inputNumber == sum:
        print(inputNumber,"is an Armstrong number")
    else:
        print(inputNumber,"is not an Armstrong number")
isArmstrongNumber(54748)
isArmstrongNumber(153)
isArmstrongNumber(54)

"""
def isArmstrongNumber(number_to_check):
    number_list = str(number_to_check)
    summary = 0
    for number in number_list:
        summary += int(number)**len(number_list)
    return(number_to_check == summary)
"""

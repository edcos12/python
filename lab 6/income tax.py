income = int(input('income: '))

def getincometax():
    global percent
    if income < 11850:
        percent = 0
        tax = 0

    elif 11850 < income < 34500:
        percent = 20
        tax = income * 0.2

    elif 34500 < income < 150000:
        percent = 40
        tax = income * 0.4

    else: 
        percent = 45
        tax = income * 0.45

    take_home = income - tax
    return take_home

print('take home pay after taxes is', getincometax(), 'at a rate of', percent, '%')

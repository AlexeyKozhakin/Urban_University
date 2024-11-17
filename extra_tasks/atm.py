corret_pin = '9681'

count = 0

while True:
    pin = input()
    if len(pin)!=4:
        print('INVALID PIN FORMAT')
    elif pin == corret_pin:
        print('CORRECT PIN')
        break
    elif len(pin)==4 and pin != corret_pin:
        print('INCORRECT PIN')
        count += 1
        if count==3:
            print('BANK CARD HELD')
            break
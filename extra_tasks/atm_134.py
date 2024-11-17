# correct_pin = '9681'
#
# i = 0
#
while True:
    pin = input()
    if pin == correct_pin:
        print('CORRECT PIN')
        break
    elif len(pin)!=4:
        print('INVALID PIN FORMAT')
    else:
        print('INCORRECT PIN')
        i += 1
        if i==3:
            print('BANK CARD HELD')
            break



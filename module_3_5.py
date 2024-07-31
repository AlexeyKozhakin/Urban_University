num = []
def get_multiplied_digits(number):
    global num
    str_number = str(number)
    if len(str_number)==1:
        print(number, end='=')
        num.append(number)
        return number
    else:
        first = int(str_number[0])
        num.append(first)
        print(first, end='x')
        #print('str_number[1:] = ', str_number[1:])
        new_number = int(str_number[1:])
        #print('new_number = ', new_number)
        return first*get_multiplied_digits(new_number)


result = get_multiplied_digits(40203)
print(result)
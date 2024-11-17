


a = 1
b = 2

try:
    c = a / b
    print(c)

except (TypeError,
        ZeroDivisionError):
    print('Деление на строку или деление на 0')


except ZeroDivisionError:
    print('Деление на 0')

except:
    print('Какая-то ошибка')

else:
    print('При успешном выполнении')

finally:
    print('Выполняется всегда')

def divide(first, second):

    return 'Ошибка' if second == 0 else first/second

if __name__ == '__main__':
    print('Переменная name в файле fake_math:',__name__)
    print('Test функцции в fake_math:',divide(10,2))
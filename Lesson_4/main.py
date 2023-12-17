while True:
    try:
        a = int(input('Введіть перше число:'))
    except ValueError:
        print('Введено некоректне число! Спробуйте ще раз.')
    else:
        break

b = int(input('Введіть друге число:'))

try:
    print(a / b)
except TypeError:
    print('Некорректний тип параметрів')
except ZeroDivisionError:
    print('Division by zero')
except Exception as error:
    print('Щось пішло не так!')
    print(f'{type(error)} {error}')

print('End of program')
print('Hello world!')
name = input('Введи своє ім\'я: ')
print('Ви ввели імя ' + name)
print('Ви ввели імя ', name)
print(f'Ви ввели імя {name}')

country = input('З якої ти країни: ')
if country == 'Україна':
  print('Привіт, земляче!')
elif country == 'Росія':
  print('Геть з України!')
elif country == 'США':
  print('Welcome to Ukraine!')
else:
  print('Вітаю в Україні!')

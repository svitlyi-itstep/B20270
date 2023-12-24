from car import Car

car1 = Car(fuel=20)

print(car1)

distances_list = [5, 20, 5, 100, 100, 6, 4]

for distance in distances_list:
    traveled_distance = car1.drive(distance)
    print(f'Машинка проїхала {traveled_distance} км.')
    print(car1)
    if car1.fuel == 0:
        print('Паливо закінчилося')
        break
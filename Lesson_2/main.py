from character import Character
from Lesson_3.berserk import Berserk

player1 = Berserk('Vasya')
player2 = Character('Petya', damage=5)
print(player1, end='\n\n')
print(player2)
print()

player1.take_damage(50)

p1_damage = player1.attack(player2)
print(f'{player1.name} атакував '
      f'{player2.name} і наніс '
      f'{p1_damage} шкоди')
print()
print(player1, end='\n\n')
print(player2)
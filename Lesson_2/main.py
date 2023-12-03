from character import Character

player1 = Character('Vasya')
player2 = Character('Petya', damage=5)
print(player1, end='\n\n')
print(player2)
print()

p1_damage = player1.attack(player2)
print(f'{player1.name} атакував '
      f'{player2.name} і наніс '
      f'{p1_damage} шкоди')
print()
print(player1, end='\n\n')
print(player2)
# 1. Копирование
import pickle
import copy


class Car:
    pass


car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)
car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)

# 2. Запись и загрузка
print()

# Ваш список любимых вещей
favorites = ['Python', 'Selenium', 'GitHub', 'Music', 'Battlefield 6']

# Сохраняем список в файл favorites.dat
with open('./data/favorites.dat', 'wb') as f:
    pickle.dump(favorites, f)

with open('./data/favorites.dat', 'rb') as f:
    favorites = pickle.load(f)
    print(favorites)

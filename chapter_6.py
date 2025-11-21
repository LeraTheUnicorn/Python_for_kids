# 1. Цикл с приветом

for x in range(0, 20):
    print('привет %s' % x)
    if x < 9:
        break

# 2. Четные числа

age = 5
if age % 2 == 0:
    for x in range(1, age + 1):
        if x % 2 == 0:
            print(x)
else:
    for x in range(1, age + 2):
        if x % 2 != 0:
            print(x)

# 2. Четные числа ВАРИАНТ 2
print('')
age = 8
[print(num) for num in ((x for x in range(1, age + 1) if x % 2 == 0) if age % 2 == 0 else (x for x in range(1, age + 2) if x % 2 != 0))]


#3. Пять любимых ингредиентов
print('')
ingredients = ['слизни', 'пиявки', 'катышки из пупка гориллы', 'брови гусеницы', 'пальцы многоножки']
[print(f"{i+1}. {ingredient}") for i, ingredient in enumerate(ingredients)]

#4. Ваш лунный вес
print('')
earth_weight = float(input("Введите свой вес на Земле (кг): "))
moon_factor = 0.165

for year in range(1, 16):
    current_earth_weight = earth_weight + (year - 1)  # прибавляем каждый год по 1 кг
    moon_weight = current_earth_weight * moon_factor
    print(f"Год {year}: Лунный вес = {moon_weight:.2f} кг")


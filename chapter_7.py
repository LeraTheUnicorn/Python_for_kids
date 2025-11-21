# 1. Функция лунного веса
def moon_weight(earth_weight, moon_factor):
    """Печатает вес на Луне для каждого года в течение 15 лет."""
    for year in range(1, 16):
        current_earth_weight = earth_weight + (year - 1)  # прибавляем каждый год по 1 кг
        moon_weight = current_earth_weight * moon_factor
        print(f"Год {year}: Лунный вес = {moon_weight:.2f} кг")


moon_weight(30, 0.25)


# 2. Функция лунного веса и количество лет
def moon_weight_for_years(earth_weight, moon_factor, time):
    """Печатает вес на Луне для каждого года в течение указанных лет."""
    for year in range(1, time + 1):
        current_earth_weight = earth_weight + (year - 1)  # прибавляем каждый год по 1 кг
        moon_weight = current_earth_weight * moon_factor
        print(f"Год {year}: Лунный вес = {moon_weight:.2f} кг")


print()
moon_weight_for_years(90, 0.25, 5)


# 3. Программа для лунного веса
def calculate_moon_weight_interactive():
    """Печатает вес на Луне для каждого года в течение указанных лет."""
    earth_weight = float(input("Введите свой вес на Земле (кг): "))
    moon_factor = float(input("Введите ежегодный прирост вашего веса: "))
    time = int(input("Введите время на Луне (года): "))
    for year in range(1, time + 1):
        current_earth_weight = earth_weight + (year - 1)  # прибавляем каждый год по 1 кг
        moon_weight = current_earth_weight * moon_factor
        print(f"Год {year}: Лунный вес = {moon_weight:.2f} кг")

print()
calculate_moon_weight_interactive()


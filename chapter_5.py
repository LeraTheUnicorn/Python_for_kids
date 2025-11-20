age = 13
if age > 20:
    print('Как-то вы староваты!')

age = 25
if age > 20:
    print('Как-то вы староваты!')
    print('Что вы здесь делаете?')
    print('Почему не стрижете газон или не перекладываете бумажки?')

age = 10
if age >= 10:
    print('\nВы слишком стары для моих шуток!')

age = 10
if age == 10:
    print('\nЧто нельзя съесть на завтрак? Обед и ужин!')

print("\nХотите услышать грязную шутку?")

age = 12
if age == 12:
    print("Свинья шлепнулась в грязь!")
else:
    print("Тсс! Это секрет.")

print('\n')
age = 12
if age == 10:
    print("Что выйдет, если клюква наденет штаны?")
    print("Брюква!")
elif age == 11:
    print("Что сказала зеленая виноградина синей виноградине?")
    print("Дыши! Дыши!")
elif age == 12:
    print("Что сказал 0 числу 8?")
    print("Привет, ребята!")
elif age == 13:
    print("Что такое: на потолке сидит и хохочет?")
    print("Муха-хохотуха!")
else:
    print("Что-что?")

print('\nОБЪЕДИНЕНИЕ УСЛОВИЙ:')
if age == 10 or age == 11 or age == 12 or age == 13:
    print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
else:
    print('Что-что?')


if age >= 10 and age <= 13:
    print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
else:
    print('Что-что?')


print('\nNone value:')
myval = None
print(myval)

myval = None
if myval == None:
    print("В переменной myval ничего нет\n")

age = 10
if age == 10:
    print("Как лучше общаться с монстром?")
    print("Издалека!\n")


# TASK 1
print('TASK 1:')
money = 2000
if money > 1000:
    print("Я богат!")
else:
    print("Я не богат!")
    print("Может, когда-нибудь потом…")

# TASK 2
twinkies = 50
if 100 > twinkies :
    print('Слишком мало бисквитиков')
elif 500 < twinkies:
    print('Слишком слишком много бисквитиков')

# TASK 3
money = 100
if money in [100,500]:
    print('Значнеие в диапазоне от 100 до 500')
elif money in [1000, 5000]:
    print('Значнеие в диапазоне от 1000 до 5000')

# TASK 4
ninjas = 5
if 30 < ninjas <= 50:
    print('Их слишком много')
elif 10 < ninjas <= 30:
    print('Будет непросто, но я с ними разделаюсь')
elif ninjas <= 10:
    print('Я одолею этих ниндзя!')
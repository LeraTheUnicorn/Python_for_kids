fred = "\nПочему у горилл большие ноздри? Потому что у них толстые пальцы!"
print(fred)

fred = "\nЧто это: розовое и пушистое? Розовый пушистик!"
print(fred)

fred = '''\nЧто едят на полдник динозавры ?
ТиРекс-кекс'''
print(fred)

single_quote_str = '\n"Тут что-то не так, не будь я д\'Артаньян", — подумал он.'
print(single_quote_str)

double_quote_str = "\n\"Тут что-то не так, не будь я д'Артаньян\", — подумал он."
print(double_quote_str)


myscore = 1000
message = '\nМой счет: %s очков'
print(message % myscore)

joke_text = '\n%s: приспособление для поиска мебели в темноте'
bodypart1 = 'Коленка'
bodypart2 = 'Лодыжка'
print(joke_text % bodypart1)

nums = '\nЧто сказало число %s числу %s? Славный поясок!'
print(nums % (0, 8))


print(f'\n10 * a : {10 * 'a'}\n')

spaces = ' ' * 25
print('%s Задний переулок 12' % spaces)
print('%s Трясогузочья пустошь' % spaces)
print('%s Западный Всхрапшир' % spaces)
print()
print()
print('Уважаемый Сэр,')
print()
print('Хочу сообщить вам, что кое-где на крыше уборной')
print('недостает кусков черепицы.')
print('Думаю, прошлой ночью их сдуло внезапным порывом ветра.')
print()
print('С почтением')
print('Малькольм Конфузли')


print(f'\n1000 * слякоть : "{1000 * 'слякоть'}')

wizard_list = 'Паучьи лапки, жабий палец, глаз тритона, крыло, летучей мыши, жир слизня, перхоть змеи'
print(f'\nwizard_list: {wizard_list}')


wizard_list = [
    'паучьи лапки',
    'жабий палец',
    'глаз тритона',
    'крыло летучей мыши',
    'жир слизня',
    'перхоть змеи']
print(f'\nwizard_list : {wizard_list}')


print(f'\nwizard_list[2]: {wizard_list[2]}')

wizard_list[2] = 'язык улитки'
print(f'\nnew wizard_list: {wizard_list}')

print(f'\nwizard_list[2:5]: {wizard_list[2:5]}')

numbers_and_strings = [7, 'раз', 'отпей', 1, 'раз', 'отъешь']
print(f'\nnumbers_and_strings: {numbers_and_strings}')

print('\nnumbers and strings lists in the list:')
numbers = [1, 2, 3, 4, 5]
strings = ['хватит', 'циферки', 'считать']
mylist = [numbers, strings]
print(mylist)

print('\nLIST APPEND: + медвежий коготь')
wizard_list.append('медвежий коготь')
print(wizard_list)

wizard_list.append('мандрагора')
wizard_list.append('болиголов')
wizard_list.append('болотный газ')

print('\nNEW LIST:')
print(wizard_list)

print('\nDELETE ELEMENT:')
del wizard_list[5]
print(wizard_list)

del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
print(wizard_list)

print('\nCONCATENATE LISTS:')
list1 = [1, 2, 3, 4, 5]
list2 = ['я', 'забрался', 'под', 'кровать']
print(list1 + list2)

list1 = [1, 2, 3, 4]
list2 = ['я', 'мечтаю', 'о', 'пломбире']
list3 = list1 + list2
print(list3)

list1 = [1, 2]
print(list1 * 5)

print('\nFIRST TUPLE:')
fibs = (0, 1, 1, 2, 3)
print(fibs[3])


print('\nDICTIONARY:')
favorite_sports = {'Ральф Уильямс': 'Футбол',
                   'Майкл Типпетт': 'Баскетбол',
                   'Эдвард Элгар': 'Бейсбол',
                   'Ребекка Кларк': 'Нетбол',
                   'Этель Смит': 'Бадминтон',
                   'Фрэнк Бридж': 'Регби'}
print(favorite_sports)
print('\nРебекка Кларк ?')
print(favorite_sports['Ребекка Кларк'])

del favorite_sports['Этель Смит']
print('\nDELETE Этель Смит')
print(favorite_sports)

favorite_sports['Ральф Уильямс'] = 'Хоккей на льду'
print(favorite_sports)

print('\nHOMEWORK PERT 3:')

print('\nTASK#1: Любимые вещи')
games = ['Hide and Seek']
foods = ['сыр', 'каша']
print(favorites := games + foods)

print('\nTASK#2: Подсчет воинов')
house_count = 3
house_warriors_count = 25
tunnels_count = 2
tunnel_warriors_count = 20
print(
    f'Total count: {
        house_count *
        house_warriors_count +
        tunnels_count *
        tunnel_warriors_count}')

print('\nTASK#3: Приветствие')
name = 'Брандо'
surname = 'Икетт'
message = 'Привет, %s %s!'
print(message % (name, surname))

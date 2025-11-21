#1. Таинственный код
a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)

#2. Зашифрованное сообщение
text = "этот если способ вы плохо это подходит читаете для что-то шифрования пошло важных не сообщений так"
words = text.split()
print()
for i in range(0, len(words), 2):
    print(words[i])

#3. Копирование файла
print()
# Имя исходного файла
source_name = "./data/source.txt"
# Имя файла-копии
copy_name = "./data/copy.txt"

# Копирование данных
with open(source_name, 'r', encoding='utf-8') as source_file:
    data = source_file.read()
with open(copy_name, 'w', encoding='utf-8') as copy_file:
    copy_file.write(data)

# Проверка результата
with open(copy_name, 'r', encoding='utf-8') as check_file:
    print(check_file.read())

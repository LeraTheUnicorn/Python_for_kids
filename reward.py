import os
import glob


def get_rubles_word(n):
    if 10 <= n % 100 <= 20:
        return 'рублей'
    elif n % 10 == 1:
        return 'рубль'
    elif 2 <= n % 10 <= 4:
        return 'рубля'
    else:
        return 'рублей'


n_display = 18  # общее количество глав
chapters = [f for f in glob.glob('chapter_*.py') if os.path.getsize(f) > 0]
n = len(chapters)  # реальное n для итогового расчета

results = list((lambda n_display, n: ((t, sum(2 ** i for i in range(t)))
               for t in range(1, max(n_display, n) + 1)))(n_display, n))

# Вывод первых n_display значений
print(f'{"ch":<4} {"reward":<8}')
for t, res in results[:n_display]:
    print(f'{t:<4} {res:<8}')

# Итоговый результат для n
result_n = next(res for t, res in results if t == n)
print(f"\nВыдайте награду: {result_n} {get_rubles_word(result_n)}")

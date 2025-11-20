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


chapters = [f for f in glob.glob('chapter_*.py') if os.path.getsize(f) > 0]
n = len(chapters)

x = 1
result = 1
for t in range(2, n + 1):
    x *= 2
    result += x

print(f"\nВыдайте награду: {result} {get_rubles_word(result)}")




x = 1
result = 1
print(x, '=> ', result)
for t in range(2, 19):
    x *= 2
    result += x
    print(t, '=> ', result)

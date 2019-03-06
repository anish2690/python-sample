i = 0
for i in range(5):
    print(i)

x = 0

for x in ('a', 'b', 'c', 4):
    print(x)

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

for i in range(5):
    if i == 3:
        break
    print(i)
for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print(' multiples of 7 found')
        break
    else:
        print(' no multiples of 7 range')

for i in range(5):
    print('--------------------------')
    try:
        10 / (i-3)
    except ZeroDivisionError:
        print(' Divided by 0')
        continue
    finally:
        print('always')

s = 'hello'
i = 0
for c in s:
    print(c, i)
    i += 1


for i in range(len(s)):
    print(i, s[i])

s = 'hello world'

for i, c in enumerate(s):
    print(i,  c)

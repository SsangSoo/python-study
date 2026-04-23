n = 'Kim'
text = '308276567'
x = 50
y = 100


# 출력1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x + y))
print(ex1)


# 출력2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n = n, s = text, sum = x + y)
print(ex2)


# 출력3
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)

# 구분기호
m = 100000000

print(f'm : {m:,}')
print()


# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽

t = 20
print(f"t : {t:10}")
print(f"t center : {t:^10}")
print(f"t center : {t:<10}")
print(f"t center : {t:>10}")

print()
print()

print(f"t center : {t:-^10}")
print(f"t center : {t:-#10}")

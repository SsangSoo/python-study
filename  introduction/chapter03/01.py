# 파이썬 완전 기초
# Print 사용법


# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")
print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')
print()

# end

print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')
print()

# file
import sys
print('Learn Python', file=sys.stdout) # 콘솔에 출력
print()

# format 사용(d : 3, s : 'python', f : 3.1445454)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()


# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) # pytho
print('%5s' % ('pythonstudy')) # pythonstudy
print('{:10.5}'.format('pythonstudy')) # pytho


# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))


# %f
print('%f' % (3.143434343434))
print('{:f}'.format(3.143434343434))
print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))




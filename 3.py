def f_sum(n1, n2, n3):
    return n1, n2, n3

n1 = int(input('1: '))
n2 = int(input('2: '))
n3 = int(input('3: '))

print(f'Сумма 2-х максимальных аргументов равна: {n1 + n2 + n3 - min([n1, n2, n3])}')

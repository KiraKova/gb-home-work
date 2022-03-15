def m_dl(a, b):
    if a != 0 and b != 0:
        del1 = a / b
        return del1
    elif a == 0 and b == 0:
        print('0 на 0 будет бесконечно малая')
    elif a == 0:
        print('0 на число делить нельзя')
    else:
        print('На 0 делить нельзя')


g = m_dl(a=int(input('Введите 1 число, кроме 0: ')), b=int(input('Введите 2 число, кроме 0: ')))

print(g)

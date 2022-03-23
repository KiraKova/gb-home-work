my_file = open('test.txt', 'w', encoding='utf-8')
line = input('Введите символы, пустая строка завершить програму \n')
while line:
    my_file.writelines(line)
    line = input('Введите символы, пустая строка завершить програму \n')
    if not line:
        break

my_file.close()
my_file = open('test.txt', 'r', encoding='utf-8')
content = my_file.readlines()
print(content)
my_file.close()

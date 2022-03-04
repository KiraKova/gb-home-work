# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
m = [123, 43.5, True, [1, 2, 3], (1, 2, 3), False, "Привет"]
print(type(0),type(1),type(2),type(3),type(4),type(5),type(6))



# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
#При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

element_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
element = 0
while i < element_count:
    my_list.append(input("Введите значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2
print(my_list)




#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень)
# Напишите решения через list и dict.

sesons_list = ['winter', 'spring', 'summer', 'autumn']
sesons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}

mounth = int(input('Введите месяц по номеру: '))
if mounth == 12 or mounth == 1 or mounth == 2:
    print(sesons_dict.get(1))
    print(sesons_list[0])

elif mounth == 3 or mounth == 4 or mounth == 5:
    print(sesons_dict.get(2))
    print(sesons_list[1])

elif mounth == 6 or mounth == 7 or mounth == 8:
    print(sesons_dict.get(3))
    print(sesons_list[2])

elif mounth == 9 or mounth == 10 or mounth == 11:
    print(sesons_dict.get(4))
    print(sesons_list[3])


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

word = input('Введите слова с пробелами')
my_word = []
n = 1
for i in range(word.count(" ") + 1):
    my_word = word.split()
    if len(str(my_word)) <= 10:
        print(f"{n} {my_word[i]}")
        n +=1
    else:
        print(f"{n}{my_word [i] [0:10]}")
        n += 1






# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
#У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

ret = [7, 5, 3, 3, 2]
my_r = int(input("Введите вашу оценку, если хотите выйти наберите 11: "))
print(ret)
while my_r != 11:
    for i in range(len(ret)):
        if ret[i] == my_r:
            ret.insert(i+1, my_r)
            break
        elif ret[0] < my_r:
            ret.insert(0, my_r)
        elif ret[-1] > my_r:
            ret.append(my_r)
        elif ret[i] > my_r and ret[i+1] < my_r:
            ret.insert(i+1, my_r)
            break

    print(f"Рейтинг - ", ret)
    my_r = int(input("Введите вашу оценку, если хотите выйти наберите 11: "))



# 6* Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения. Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
#
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

products = []
for i in range(1, 4):
    print(f"Заполняем информацию по {i}-му товару")
    product_name = input("Название: ")
    product_price = int(input("Цена: "))
    product_count = int(input("Количество: "))
    product_measure =  input("Единица измерения: ")
    products.append((i, {'название': product_name, 'цена': product_price, 'количество': product_count, 'eд': product_measure}))

print(f"Исходный список товаров: \n{products}")

product_names = []
product_prices = []
product_counts = []
product_measures = []
for i in products:
    product_names.append(i[1].get('название'))
    product_prices.append(i[1].get('цена'))
    product_counts.append(i[1].get('количество'))
    product_measures.append(i[1].get('eд'))

report = {
    'название': list(set(product_names)),
    'цена': list(set(product_prices)),
    'количество': list(set(product_counts)),
    'eд': list(set(product_measures))
}

print(f"Отчет по списку товаров: \n{report}")
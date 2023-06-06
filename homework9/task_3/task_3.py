# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

purchases_list = []
purchases = 0
with open("test_file/task_3.txt", "r", encoding='utf-8') as file:
    for p in file.readlines():
        if p != "\n":
            purchases += int(p)
        else:
            purchases_list.append(purchases)
            purchases = 0

purchases_list.sort(reverse=True)
three_most_expensive_purchases = purchases_list[0] + purchases_list[1] + purchases_list[2]

assert three_most_expensive_purchases == 202346

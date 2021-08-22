from functools import reduce

#есть два списка
test_1 = [1,2,3,4,5,6]
test_2 = [3,4,5,6,7,8]

# FIRST

#1 написать мап функцию- с использование лямбда-выражения для умножения кадго значения  test_1 на 2 в 1 строку
print(list(map(lambda x: x * 2, test_1)))
#2 через функцию map перемножить test_1 и test_2 поэлементно
print(list(map(lambda x, y: x * y, test_1, test_2)))
#3 через функцию filter вернуть все элементы test_2 которые делятся целочисленно на 3
print(list(filter(lambda x: x % 3 == 0, test_2)))
#4 через функцию reduce вернуть cумму всех элементов списка test1 + test2 (должно получиться 54)
print(reduce(lambda acc, val: acc + val, test_1 + test_2))
#5 через zip объеденить оба списка
print(list(zip(test_1, test_2)))

# SECOND

#есть список
test_d = 'Однажды1 в студеную2 зимнюю пору3'
#1 написать мап функцию для перевода всех букв в строке в большие в 1 строку
print(''.join(list(map(lambda x: x.upper(), test_d))))
#2 через функцию filter вернуть список гласных букв
print(list(filter(lambda x: x.lower() in ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я'], test_d)))
# 3 через функцию reduce вернуть cумму всех цифр списка test_d (6)
print(reduce(lambda acc, val:  acc + int(val) if val.isnumeric() else acc, test_d, 0))
#4 через zip объеденить оба списка, один из которых в обратном порядке test_d
print(list(zip(test_d, reversed(test_d))))

# Python. HW_1.
# Part_1
#
# 1) Создать переменную типа String
name = 'Olga'

# 2) Создать переменную типа Integer
age = 23

# 3) Создать переменную типа Float
weight = 50.3

# 4) Создать переменную типа Bytes
two_bytes = bytes(2)

# 5) Создать переменную типа List
new_codes = ['1234', '5678', '4321', '8765', '0987']

# 6) Создать переменную типа Tuple
old_codes = ('2222', '1111', '4444', '3333')

# 7) Создать переменную типа Set
fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}

# 8. Создать переменную типа Frozen set
basket = frozenset(fruits)

# 9) Создать переменную типа Dict
person = {'name': 'Masha', 'age': 25}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print('name=', name, type(name))
print('age=', age, type(age))
print('weight=', weight, type(weight))
print('two_bytes', two_bytes, type(two_bytes))
print('new_codes=', new_codes, type(new_codes))
print('old_codes=', old_codes, type(old_codes))
print('fruits', fruits, type(fruits))
print('basket=', basket, type(basket))
print('person=', new_codes, type(person))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
boy = 'Vasya'
girl = 'Katya'
boy_and_girl = boy + girl

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print('name,age', name, age)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print ('name+age', name + str(age))

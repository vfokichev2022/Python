# Python. HW_1.
# Part_1
#
# 1) ������� ���������� ���� String
name = 'Olga'

# 2) ������� ���������� ���� Integer
age = 23

# 3) ������� ���������� ���� Float
weight = 50.3

# 4) ������� ���������� ���� Bytes
two_bytes = bytes(2)

# 5) ������� ���������� ���� List
new_codes = ['1234', '5678', '4321', '8765', '0987']

# 6) ������� ���������� ���� Tuple
old_codes = ('2222', '1111', '4444', '3333')

# 7) ������� ���������� ���� Set
fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}

# 8. ������� ���������� ���� Frozen set
basket = frozenset(fruits)

# 9) ������� ���������� ���� Dict
person = {'name': 'Masha', 'age': 25}

# 10) ������� � ������� ��� ���� ������������� ���������� � ����������� ���� ������.
print('name=', name, type(name))
print('age=', age, type(age))
print('weight=', weight, type(weight))
print('two_bytes', two_bytes, type(two_bytes))
print('new_codes=', new_codes, type(new_codes))
print('old_codes=', old_codes, type(old_codes))
print('fruits', fruits, type(fruits))
print('basket=', basket, type(basket))
print('person=', new_codes, type(person))

# 11) ������� 2 ���������� String, ������� ���������� � ������� ��������������� ��� ����������. ������� � �������.
boy = 'Vasya'
girl = 'Katya'
boy_and_girl = boy + girl

# 12) ������� � ���� ������ ���������� ���� String � Integer ��������� �,� (�������)
print('name,age', name, age)

# 13) ������� � ���� ������ ���������� ���� String � Integer ��������� �+� (����)
print ('name+age', name + str(age))

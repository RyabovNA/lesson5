tuple_ = [1, 2], 3, 4, 'Nikolay'
immutable_var = tuple_
print('Immutable tuple:', immutable_var)
# tuple_[2] = 67 - Изменить элемент кортежа по индексом 2 не получится, т.к. он является не изменяемым. Элемент под индексом можно изменить - он изменяемый.
mutable_list = [67, 'Stas', 'Chelyabinsk']
mutable_list[1] = 'Nikolay'
print('Mutable list:', mutable_list)
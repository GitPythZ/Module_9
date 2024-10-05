lst_int_ = [6, 20, 15, 9]  # коллекция для работы функций.


def apply_all_func(int_list, *functions):
    """Функция должна вызывать каждую функцию к переданному списчку int_list.
    Возвращать словарь, где ключом будет название вызванной функции,
    а значением - её результат работы со списком int_list;
    int_list - список из чисел (int, float);
    *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел);
    """
    result = {}
    for func in functions:
        func_posible = func(int_list)
        result.update({func.__name__: func_posible})
    return result


test1 = apply_all_func(lst_int_, max, min)
print(test1)
test2 = apply_all_func(lst_int_, min, max, len, sum, sorted)
print(test2)

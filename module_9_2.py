first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


def len_first_strings(first_strings):
    """Функция возвращает список first_result, содержащий строки >= 5."""
    first_result = []
    for word in first_strings:
        if len(word) >=5:
            first_result.append(len(word))
        else:
            continue
    return first_result


print(len_first_strings(first_strings))

# или короткий вариант
first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)


def size_substring(first_strings, second_strings):
    """Функция возвращает кортеж, состоящий из строк равной длины каждого из списка."""
    second_result = []
    for first_word in first_strings:
        for second_word in second_strings:
            if len(first_word) == len(second_word):
                second_result.append((first_word, second_word))
            else:
                continue
    return second_result


print(size_substring(first_strings, second_strings))

# или короткий вариант
second_result = [(x,y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)


def generation_dict(first_strings, second_strings):
    """Функция возвращает словарь, где ключ - строка, значение - длина строки.
       Условие: словарь пополняется строками, которые имеют четную длину;
       Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings;
    """
    # конкатенирвоать списки можно было методом extend, += или просто сложением двух списков,
    # но решил перебрать циклом.
    new_lst = []
    dictionary = {}
    for i in first_strings:
        new_lst.append(i)
    for j in second_strings:
        new_lst.append(j)
    for x in new_lst:
        if len(x) % 2 == 0:
            dictionary.update({x: len(x)})
    return dictionary


print(generation_dict(first_strings, second_strings))

# или короткий вариант
third_result = [{x: len(x)} for x in (first_strings + second_strings) if len(x) % 2 == 0]
print(third_result)
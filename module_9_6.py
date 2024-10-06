def all_variants(text):
    """Функция-генератор, которая принимает строку text, а возвращает объект-генератор.
       Каждая итерация возвращает подпоследовательности строки;
    """
    _len_substring = 0
    while _len_substring < len(text):
        i = text[_len_substring]
        yield i
        _len_substring += 1

    x = 0
    y = 1
    for i in range(len(text)):
        while x < len(text) and y < len(text):
            i = text[x]
            j = text[y]
            yield i + j
            x += 1
            y += 1

    yield text


a = all_variants("Gendalf")
for _ in a:
    print(_)
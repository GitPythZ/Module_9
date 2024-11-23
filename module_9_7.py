def is_prime(func):
    """Проверяет число, которое возвращает ф-я sum_three, является ли оно "простым" или 'составным'.
       Декоратор возвращает функцию, поэтому создаю вложенную структуру;
    """
    def wrapper(*args):
        result_func = func(*args)
        for i in range(2, result_func + 1):
            if result_func % i == 0:
                prime_check = f"{result_func} - 'составное' число."
            else:
                prime_check = f"{result_func} - 'простое' число."
            return prime_check

    return wrapper


@is_prime
def sum_three(one, two, three):
    """Складывает три числа.
    """
    return one + two + three


s = sum_three(1, 1, 1)
print(s)

s2 = sum_three(2, 2, 2)
print(s2)

s3 = sum_three(1, 5, 2)
print(s3)

s4 = sum_three(1, 5, 5)
print(s4)

s5 = sum_three(5, 5, 5)
print(s5)

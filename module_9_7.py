def is_prime(func):
    """Проверяет число, которое возвращает ф-я sum_three, является ли оно "простым" или 'составным'.
       Декоратор возвращает функцию, поэтому создаю вложенную структуру;
    """
    def wrapper(*args):
        result_func = func(*args)
        for i in range(2, result_func):
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



result = sum_three(2, 3, 6)
print(result)
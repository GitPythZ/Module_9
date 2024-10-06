import random
from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'
                           # Lambda-функция
print(list(map(lambda x, y: x == y, first, second)))


                           # Замыкания


def get_advanced_writer(file_name):
    """
        Функция get_advanced_writer возвращает функцию write_everything.
    """
    def write_everything(*data_set):
        """*data_set - параметр принимающий неограниченное количество данных любого типа.
        Функция write_everything добавляет в файл file_name все данные из data_set, в том же виде;
        """
        with open(file_name, "a", encoding="utf-8") as file:
            for i in data_set:
                file.write(f"\n{i}")

    return write_everything


write = get_advanced_writer('get_advanced_file.txt')
write("Это строчка", ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


                        # Метод Call
class Mystic_Ball:
    def __init__(self, *words):
        """
        Атрибут words хранит коллекцию строк.
        """
        self.words = words

    def __call__(self):
        """
        Случайным образом выбирает слово из words и возвращает его.
        :return:
        """
        return random.choice(self.words)


first_ball = Mystic_Ball('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


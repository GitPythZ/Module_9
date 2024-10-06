# Задача "Range - это просто":
class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start: int, stop: int, step=1):
        """
        Класс итератор обладает атрибутами start: stop: step: pointer.\
        """
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step == 0:
            raise StepValueError("Шаг не может быть равен 0")

    def __iter__(self):
        """
        Сбрасывает pointer на старт и возвращает объект итератора.
        """
        self.pointer = self.start
        return self

    def __next__(self):
        """Увеличивает pointer на step.
           В зависимости от знака атрибута step итерация завершается,
           либо когда pointer станет больше stop, либо меньше stop;
        """
        if self.pointer > self.stop and self.step > 0:
            raise StopIteration()
        elif self.pointer < self.stop and self.step < 0:
            raise StopIteration()
        self.pointer += self.step
        return self.pointer - self.step


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
iter2 = Iterator(-5, 1)
for i in iter2:
    print(i, end=' ')
print()
iter3 = Iterator(6, 15, 2)
for i in iter3:
    print(i, end=' ')
print()
iter4 = Iterator(5, 1, -1)
for i in iter4:
    print(i, end=' ')
print()
iter5 = Iterator(10, 1)
for i in iter5:
    print(i, end=' ')
print()
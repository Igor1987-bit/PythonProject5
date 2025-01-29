# Задача "Нужно больше этажей" на основе предыдущей задачи
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        title = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return title

    # Создаём условия по дополнению класса House следующими специальными методами:
    def __eq__(self, other):  # 1
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):  # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        # убеждаемся в принадлежности второго элемента к определенным в классе типам данных
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):  # убедимся в принадлежности количества этажей к типу int
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):  # просто вызван магический метод __add__
        return self.__add__(value)

    def __iadd__(self, value):  # iadd - предположил что первый символ метода "i" -
        # проверка на int
        if isinstance(value, int):
            self.number_of_floors += value
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК АКация', 20)

# Вывод результатов:
print(h1)
print(h2)
print(h1 == h2, '- изначально разное количество этажей')
h1.__add__(10)
print(h1 == h2, '- Надстроили "ЖК Эльбрус" 10  этажей, одинаковое количество этажей:',
      h1.number_of_floors, ' и ', h2.number_of_floors)
h1.__add__(10)
print(h1 == h2, '- Надстроили "ЖК Эльбрус" 10  этажей, стало больше количество этажей:',
      h1.number_of_floors, ' и ', h2.number_of_floors)
h2.__add__(10)
print(h1 == h2, '- Надстроили "ЖК АКация" 10  этажей, одинаковое количество этажей:',
      h1.number_of_floors, ' и ', h2.number_of_floors)
# поочередно сравниваем количества этажей
print("\nПоочередно сравниваем количества этажей:")
print(h1 < h2, '- \033[1m "условие меньше"\033[0m...', h1.number_of_floors, ' и ', h2.number_of_floors)
print(h1 <= h2, '- \033[1m "условие меньше и равно"\033[0m...', h1.number_of_floors, ' и ',
      h2.number_of_floors)
print(h1 > h2, '- \033[1m "условие больше"\033[0m...', h1.number_of_floors, ' и ', h2.number_of_floors)
print(h1 >= h2, '- \033[1m "условие больше и равно"\033[0m...', h1.number_of_floors, ' и ',
      h2.number_of_floors)
print(h1 != h2, '- \033[1m "условие не равно"\033[0m...', h1.number_of_floors, ' и ',
      h2.number_of_floors)
print('И... наконец:')
print(h1 == h2, f' - \033[1m "РАВНО"...\033[0m', h1.number_of_floors, ' и ',
      h2.number_of_floors)
print('Смотрим работу __radd__ и __iadd__:')
h2 = 10 + h2  # __radd__
print(h1, h2)
h1 += 10  # __iadd__
print(h1, h2)
# console
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК АКация, кол-во этажей: 20
# False - изначально разное количество этажей
# True - Надстроили "ЖК Эльбрус" 10  этажей, одинаковое количество этажей: 20  и  20
# False - Надстроили "ЖК Эльбрус" 10  этажей, стало больше количество этажей: 30  и  20
# True - Надстроили "ЖК АКация" 10  этажей, одинаковое количество этажей: 30  и  30
# 
# Поочередно сравниваем количества этажей:
# False -  "условие меньше"... 30  и  30
# True -  "условие меньше и равно"... 30  и  30
# False -  "условие больше"... 30  и  30
# True -  "условие больше и равно"... 30  и  30
# False -  "условие не равно"... 30  и  30
# И... наконец:
# True  -  "РАВНО"... 30  и  30
# Смотрим работу __radd__ и __iadd__:
# Название: ЖК Эльбрус, кол-во этажей: 30 Название: ЖК АКация, кол-во этажей: 40
# Название: ЖК Эльбрус, кол-во этажей: 40 Название: ЖК АКация, кол-во этажей: 40

# 0.  Импорт функции sleep() из модуля time
import time #
# 1. Создайте класс House.
class House():
    # 2. Внутри класса House определите метод __init__, в который передадите название и
    # кол-во этажей.
    def __init__(self, name, number_of_floors):
        #3. Внутри метода __init__ создайте атрибуты объекта self.name и
        # self.number_of_floors, присвойте им переданные значения.
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        # 4. Создайте метод go_to с параметром new_floor и напишите логику внутри него на
        #  основе описания задачи.
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor):
                print(floor, '- этаж. Едем пока ещё.')
                time.sleep(1)
            print(f'{new_floor}-й этаж. Отлично! Приехали как заказывали')
        else:
            time.sleep(2)
            print(f'ОЙ! {new_floor}-й этажа в "{self.name}" ещё не успели построить')
    def __str__(self):
        return f'Строение \033[1m "{self.name}"\033[0m, кол-во этажей: {self.number_of_floors}.'

# 5. Создайте объект класса House с произвольным названием и количеством этажей.
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
# 6. Вызовите метод go_to у этого объекта с произвольным числом.
print(f'\n')
print(str(h1))
h1.go_to(5)
print(f'\n')
print(str(h2))
h2.go_to(10)

# consol:
# 
# Строение  "ЖК Горский", кол-во этажей: 18.
# 1 - этаж. Едем пока ещё.
# 2 - этаж. Едем пока ещё.
# 3 - этаж. Едем пока ещё.
# 4 - этаж. Едем пока ещё.
# 5-й этаж. Отлично! Приехали как заказывали
# 
# 
# Строение  "Домик в деревне", кол-во этажей: 2.
# ОЙ! 10-й этажа в "Домик в деревне" ещё не успели построить


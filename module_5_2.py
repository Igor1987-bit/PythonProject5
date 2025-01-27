# Необходимо дополнить класс House следующими специальными методами:
class House:
    def  __init__(self, name, number_of_floors, single_number = 0):
        self.name = name
        self.number_of_floors = number_of_floors
        # это якобы надстроили чердак
        self.single_number = single_number

    # возвращает кол-во этажей здания self.number_of_floors.
    def __len__(self):
        return self.number_of_floors + self.single_number

    # возвращает строку: "Название: <название>, кол-во этажей: <этажи>"
    def __str__(self):
        return (f'Название: \033[1m "{self.name}"\033[0m, количество этажей:'
                f' {self.number_of_floors}')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация ', 20, 1)

# __str__ - возвращает строку с запрограммированной информацией о здании
print(h1)
print(h2)

# __len__ - возвращает запрошенный и __len__ числовой параметр записи
print(h1.name, 'комплекс:')
print(str(len(h1)) + ' - это без чердака')
print(h2.name, 'комплекс:')
print(str(len(h2)) + ' - это  с чердаком')

# consol:
# Название:  "ЖК Эльбрус", количество этажей: 10
# Название:  "ЖК Акация ", количество этажей: 20
# ЖК Эльбрус комплекс:
# 10 - это без чердака
# ЖК Акация  комплекс:
# 21 - это  с чердаком

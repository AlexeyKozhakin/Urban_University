class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for self.number_of_floors in range(1, new_floor ):
                print(self.number_of_floors)
        else:
            print("Такого этажа не существует")


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            return self.number_of_floors + other
        elif isinstance(other, House):
             return self.number_of_floors + other.number_of_floors

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return  self + other


# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# str
print(h1)
print(h2)

# # len
# print(len(h1))
# print(len(h2))

# eq
h1 = h2 + 20
print(h1)
# print(h1 == 10)
#
# h1 = h2 + h1 # add
# print(h1)
# print(h1 == h2)
# print(h1+h2)
#
#
# print(h1 > h2) # gt
# print(h1 >= h2) # ge
# print(h1 < h2) # lt
# print(h1 < 3) # lt
# print(h1 <= h2) # le
# print(h1 != h2) # ne